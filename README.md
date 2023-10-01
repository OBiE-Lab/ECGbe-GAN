# ECGbe-GAN: A novel deep learning approach for eliminating ECG inteference from EMG data  
## Authors
**Lucas Haberkamp** 
1. Naval Medical Research Unit - Dayton, Wright-Patterson Air Force Base, OH, USA 
2. Oak Ridge Institute for Science and Education, Oak Ridge, TN, USA 
3. Leidos, Reston, VA, USA 
  
**Charles A. Weisenbach** 
1. Naval Medical Research Unit - Dayton, Wright-Patterson Air Force Base, OH, USA
2. Oak Ridge Institute for Science and Education, Oak Ridge, TN, USA 

**Peter Le** 
4. Air Force Research Laboratory, 711th Human Performance Wing, Wright-Patterson Air Force Base, OH, USA

## Abstract
This paper introduces ECGbe-GAN, a novel deep learning framework specifically designed to filter electrocardiographic (ECG) interference from electromyographic (EMG) data. ECGbe-GAN does not require prior knowledge of an uncorrupted EMG signal for training, a common road-block for developing denoising deep learning models. Using adversarial training, ECGbe-GAN can learn solely from prior knowledge of EMG segment locations with significant ECG interfer-ence. We evaluated ECGbe-GAN using a synthetic and experimental dataset, comparing it to a high pass filter (4th-order Butterworth 30-Hz high pass filter) and a supervised deep learning model. For the synthetic dataset, ECGbe-GAN surpassed the high pass filter (SNR: +10.44 dB, MedFreqRMSE: –5.72 Hz) and performed similarly to the supervised deep learning model (SNR: –0.31 dB, MedFreqRMSE: –0.08 Hz). Quantifying the results of the experimental dataset was not possible due to absence of an uncorrupted baseline EMG signal. However, visual examination revealed ECGbe-GAN's superior performance in filtering ECG from EMG across all sensors. Both high pass filtering and supervised deep learning approaches failed to remove many QRS com-plexes and distorted the EMG signal. Overall, by successfully removing ECG interference from all EMG sensors, ECGbe-GAN enhances signal quality, potentially leading to more dependable bio-mechanical interpretations in future studies.

## Contact
For any further inquiries or discussions related to this work, please reach out to the primary correspondent: lucas.haberkamp.ctr@us.af.mil

## Acknowledgements
The views expressed in this article reflect the results of research conducted by the authors and do not necessarily reflect the official policy or position of the Department of the Navy, Department of the Air Force, Department of Defense, nor the United States Government.  
Peter Le is an employee of the U.S. Government. This work was prepared as part of his offi-cial duties. Title 17 U.S.C. 105 provides that copyright protection under this title is not available for any work of the U.S. Government. Title 17 U.S.C. 101 defines a U.S. Government work as work prepared by a military service member or employee of the U.S. Government as part of that person's official duties.  
The authors are thankful for the technical assistance provided by Alannah Gernon who was instrumental during data collection.  

## Funding
This work was funded by the Defense Health Agency, Joint Program Committee-5 (JPC-5), work unit number (H2101).  
