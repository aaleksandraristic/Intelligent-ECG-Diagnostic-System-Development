# Intelligent ECG Diagnostic System based on CNN Models

The primary objective of this research project is to design a robust diagnostic system capable of classifying ECG images of cardiovascular disorders based on ECG recordings. The proposed CNN models, VGG and ResNet, were trained on the dataset to learn distinctive features from the complex ECG waveforms. The research explored the efficacy of these architectures in capturing intricate patterns and subtle abnormalities present in the ECG images.

**Dataset:**
- ECG images from patients diagnosed with both cardiac conditions and COVID-19 
- 1937 distinct patient records, gathered using the 'EDAN SERIES-3 ECG Device deployed in Cardiac Care and Isolation Units [3] across various healthcare institutions in Pakistan.
- do not contain any personal information about patients.
- Resource: https://data.mendeley.com/datasets/gwbz3fsgp8/1 


**Methods: CNN Architectures**

This study utilized two prominent **Convolutional Neural Network (CNN) architectures, VGG and ResNet**, to develop an intelligent ECG diagnostic system for classifying ECG images into cardiovascular disorder categories.

**1. VGG16 (Visual Geometry Group) Network:**

VGG is renowned for its simplicity and effectiveness in image classification. It consists of several convolutional layers followed by max-pooling layers and fully connected layers.

**2. ResNet50 (Residual Network):**

ResNet addressed the problem of vanishing gradients in deep networks by introducing skip connections or residual blocks, making it suitable for capturing complex patterns in ECG images.

**Methodology**

**1. Data Preprocessing:** ECG images were standardized and resized to a uniform size suitable for input to the CNN models.

**2. Data Augmentation:** Techniques like rotation, horizontal flipping, and zooming were applied to augment the dataset, enhancing model generalization.

**3. Model Training:** VGG and ResNet models were initialized with pre-trained weights and fine-tuned on the ECG dataset.

**4. Model Evaluation:** The models were evaluated using accuracy, sensitivity, specificity, and F1-score to assess diagnostic performance. 

**Expected Outcome:**

The expected outcome of this research is a sophisticated diagnostic tool that can aid healthcare professionals in rapidly and accurately identifying normal cardiac patterns, abnormalities, and potential myocardial disorders from 12-lead ECG images. The findings from this research lay the foundation for future enhancements, including the integration of real-time monitoring capabilities and the expansion of the dataset to further refine and generalize the diagnostic system. 


[Intelligent 12-lead ECG Diagnostic System Development - Final Presentation.pptx](https://github.com/user-attachments/files/15909110/Intelligent.12-lead.ECG.Diagnostic.System.Development.-.Final.Presentation.pptx)
