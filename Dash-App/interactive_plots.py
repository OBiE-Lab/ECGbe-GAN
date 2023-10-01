import os
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.subplots as sp
import plotly.graph_objs as go
import numpy as np
import pandas as pd

# Define a new set of more descriptive names for each EMG sensor
better_muscle_names = ['Right Erector Spinae', 'Left Erector Spinae', 'Right Internal Oblique',
                       'Left Internal Oblique', 'Right Latissimus Dorsi', 'Left Latissimus Dorsi', 'Right Rectus Abdominis',
                       'Left Rectus Abdominis', 'Right External Oblique', 'Left External Oblique']


def extractdf(data_path):
    df_dict = {}
    for entry in os.scandir(data_path):
        if entry.name.endswith('.csv'):
            # Extract participant identifier and movement from the filename
            participant, movement = os.path.splitext(entry.name)[0].split('_')
            if movement not in df_dict:
                df_dict[movement] = {}
            df_dict[movement][participant] = pd.read_csv(entry.path)

    return df_dict


path = "../Data/Experimental Predictions/"
data_dict = extractdf(path)

app = dash.Dash(__name__)
server = app.server

app.layout = html.Div([
    dcc.Dropdown(
        id='movement-dropdown',
        options=[{'label': movement, 'value': movement}
                 for movement in data_dict.keys()],
        value='Sit-to-Stand'
    ),
    dcc.Dropdown(
        id='method-dropdown',
        options=[{'label': method, 'value': method}
                 for method in ['Raw', 'HPF', 'ECGbe-GAN', 'Supervised']],
        value=['Raw', 'ECGbe-GAN'],
        multi=True
    ),
    dcc.Graph(id='emg-plot')
])


@app.callback(
    Output('emg-plot', 'figure'),
    [Input('movement-dropdown', 'value'),
     Input('method-dropdown', 'value')]
)
def update_figure(selected_movement, selected_methods):
    method_colors = {
        'Raw': 'black',
        'ECGbe-GAN': '#1E90FF',
        'HPF': '#ff7f0e',
        'Supervised': '#2ca02c'
    }

    fig = sp.make_subplots(
        rows=5,
        cols=2,
        subplot_titles=[
            f"{selected_movement} - {sensor}" for sensor in better_muscle_names],
        vertical_spacing=0.05,
        horizontal_spacing=0.05,
        specs=[[{}, {}]] * 5,
    )

    for method in selected_methods:
        df = data_dict.get(selected_movement, {}).get(method, None)
        if df is None:
            continue

        t = np.arange(len(df)) / 1920
        for c, (i, j) in enumerate([(i, j) for i in range(5) for j in range(2)]):
            showlegend_flag = (i, j) == (0, 0)
            fig.add_trace(go.Scatter(x=t, y=df.iloc[:, c], name=method, legendgroup=method, line=dict(
                color=method_colors[method], width=1.5), showlegend=showlegend_flag), row=i+1, col=j+1)

    fig.update_layout(
        height=1200,
        width=1000,
        legend=dict(orientation="h", yanchor="bottom", y=1.02,
                    xanchor="right", x=1, font=dict(size=12)),
        plot_bgcolor="white",
        margin=dict(l=10, r=10, t=100, b=50, autoexpand=True),
    )
    return fig


if __name__ == '__main__':
    app.run_server(debug=True, port=8051)
