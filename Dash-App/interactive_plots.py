import os
import dash
from dash import dcc
from dash import html
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
    file_list, df_list = [], []  # initialize lists
    for filename in sorted(os.listdir(data_path)):
        f = os.path.join(data_path, filename)
        if os.path.splitext(filename)[1] == '.csv':
            # get the identifier of the participant from the file
            current_file = os.path.splitext(filename)[0]
            file_list.append(current_file)
            tmp_df = pd.read_csv(f)
            df_list.append(tmp_df)

    return df_list, file_list


# Specify paths
path = "../Data/Experimental Predictions/"

# Extract the data as dataframes stored into lists
data_list, file_list = extractdf(path)

# print("Files in the dataset:", file_list)

app = dash.Dash(__name__)
server = app.server

# Define the app layout
app.layout = html.Div([
    dcc.Dropdown(
        id='movement-dropdown',
        options=[{'label': movement, 'value': movement} for movement in [
            'Sagittal Flexion', 'Seated Task', 'Sit-to-Stand', 'Standing Neutral']],
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
        'ECGbe-GAN': '#1E90FF',  # Dodger Blue
        'HPF': '#ff7f0e',   # Orange
        'Supervised': '#2ca02c'   # Green
    }

    # Filter out dataframes corresponding to selected movement
    all_name_df_pairs = {name.split('_')[0]: df for name, df in zip(
        file_list, data_list) if name.split('_')[1] == selected_movement}

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
        df = all_name_df_pairs.get(method, None)
        if df is None:
            continue

        color = method_colors[method]
        # Define time-axis
        t = np.arange(len(df))/1920
        c = 0

        for i in range(5):
            for j in range(2):
                fig.update_xaxes(matches='x', row=i+1, col=j+1)

                showlegend_flag = True if (i, j) == (0, 0) else False

                fig.add_trace(go.Scatter(x=t, y=df.iloc[:, c], name=method, legendgroup=method, line=dict(
                    color=color, width=1.5), showlegend=showlegend_flag), row=i+1, col=j+1)

                xaxis_title = "Time (s)" if i == 4 else None
                yaxis_title = "Amplitude (mV)" if j == 0 else None

                fig.update_xaxes(title_text=xaxis_title, row=i+1, col=j+1, showgrid=True, gridwidth=1, gridcolor="LightGrey",
                                 title_standoff=10, tickfont=dict(size=10), title_font=dict(size=12))  # Update title_font for x-axis
                fig.update_yaxes(title_text=yaxis_title, row=i+1, col=j+1, showgrid=True, gridwidth=1, gridcolor="LightGrey",
                                 title_standoff=10, tickfont=dict(size=10), title_font=dict(size=12))  # Update title_font for y-axis

                c += 1

    fig.update_layout(
        height=1200,
        width=1000,
        legend=dict(orientation="h", yanchor="bottom", y=1.02,
                    xanchor="right", x=1, font=dict(size=12)),
        plot_bgcolor="white",
        # set l and r to center the plot
        margin=dict(l=10, r=10, t=100, b=50, autoexpand=True),
    )
    return fig


if __name__ == '__main__':
    app.run_server(debug=True, port=8051)
