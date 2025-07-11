# Gas-stove-on-with-or-without-vessel-using-YOLO11-model
Object detection using YOLO model for a custom Dataset
PROBLEM STATEMENT:
People sometimes forget to switch off the gas stove and leave it unattended. This may lead to a fire accident, and a life-threatening one.
 As an AI Engineer,  propose a solution to predict whether the gas stove is on with or without a vessel


TECH STACK USED<img width="895" height="193" alt="image" src="https://github.com/user-attachments/assets/4b06f752-f3ea-44fa-93a8-fa83787c2909" />

LABELSTUDIO – Open source tool used for image labelling and to download the respective annotation files to run the model
ULTRALYTICS – to run YOLO V11 model
YOLO V11 – to train the custom dataset
Python 3.12
Pytorch – CUDA 12.6 (for enabling GPU option)
Anaconda prompt– To train, validate and deploy the model using python code

DATA PREPARATION<img width="1083" height="193" alt="image" src="https://github.com/user-attachments/assets/a284f848-361e-4bab-a3f8-290d6e5a4b9c" />
A custom dataset consisting of 70-plus images (including real-time and collected online) is used to train the model, as there is scarce availability of images globally for the chosen problem statement.
After collecting the data, it is labelled using LabelStudio to generate annotations/labels, which are used for YOLO models
Sample of the input images for Gas stove on without vessel or with vessel as depicted on the right

OUTCOME<img width="548" height="193" alt="image" src="https://github.com/user-attachments/assets/f9d0c086-120f-43fb-a3bf-ddd73bbaff96" />
Our model can identify gas stove on_with vessel with confidence score of 88
Can identify gas stove on_without vessel with confidence score of 63
Improvements can be done to increase the predictions using large amount of datasets and better model for prediction
<img width="2154" height="222" alt="image" src="https://github.com/user-attachments/assets/58df091f-464c-4d39-93a1-ccb7718d2a73" />





