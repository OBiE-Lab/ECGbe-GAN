# ECGbe-GAN:A novel deep learning approach for eliminating ECG inter-ference from EMG data
## Authors
- **Lucas Haberkamp** 
  - Naval Medical Research Unit - Dayton, Wright-Patterson Air Force Base, OH, USA 
  - Oak Ridge Institute for Science and Education, Oak Ridge, TN, USA 
  - Leidos, Reston, VA, USA 
  - *Correspondence:* [lucas.haberkamp.ctr@us.af.mil](mailto:lucas.haberkamp.ctr@us.af.mil)
  
- **Charles A. Weisenbach** 
  - Naval Medical Research Unit - Dayton, Wright-Patterson Air Force Base, OH, USA 
  - Oak Ridge Institute for Science and Education, Oak Ridge, TN, USA 

- **Peter Le** 
  - Air Force Research Laboratory, 711th Human Performance Wing, Wright-Patterson Air Force Base, OH, USA

## Abstract
This paper introduces ECGbe-GAN, a novel deep learning framework specifically designed to filter electrocardiographic (ECG) interference from electromyographic (EMG) data. ECGbe-GAN overcomes the common roadblock for developing denoising deep learning models by not requiring prior knowledge of an uncorrupted EMG signal for training. Through adversarial training, ECGbe-GAN learns from only the knowledge of EMG segment locations with significant ECG interference. 

An evaluation using both synthetic and experimental datasets was conducted, comparing ECGbe-GAN to a high pass filter (4th-order Butterworth 30-Hz high pass filter) and a supervised deep learning model. Results from the synthetic dataset demonstrated ECGbe-GAN's superiority over the high pass filter and comparable performance to the supervised model. While the experimental dataset did not have an uncorrupted baseline EMG signal for precise quantification, visual assessments clearly showed ECGbe-GAN's exceptional performance in filtering out ECG from EMG across all sensors, where other models failed or distorted the data. 

In essence, ECGbe-GAN holds promise for enhanced signal quality and can be pivotal for more reliable biomechanical interpretations in future research.

## Key Points

- ECGbe-GAN specifically filters ECG interference from EMG data without needing uncorrupted EMG signal knowledge.
- Adversarial training approach utilized.
- Outperforms high pass filters and comparable to supervised deep learning models in synthetic datasets.
- Visual analysis showcases superiority in experimental dataset filtering.

## Contact
For any further inquiries or discussions related to this work, please reach out to the primary correspondent: [Lucas Haberkamp](mailto:lucas.haberkamp.ctr@us.af.mil).

## Acknowledgements
This research was supported and facilitated by:
- Naval Medical Research Unit - Dayton
- Oak Ridge Institute for Science and Education
- Leidos
- Air Force Research Laboratory, 711th Human Performance Wing

---

**NOTE**: This README provides an overview of the ECGbe-GAN paper. For comprehensive details and insights, it is recommended to go through the original paper.
