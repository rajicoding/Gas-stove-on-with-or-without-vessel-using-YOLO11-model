# Gas-stove-on-with-or-without-vessel-using-YOLO11-model
Object detection using YOLO model for a custom Dataset
PROBLEM STATEMENT:
People sometimes forget to switch off the gas stove and leave it unattended. This may lead to a fire accident, and a life-threatening one.
 As an AI Engineer,  propose a solution to predict whether the gas stove is on with or without a vessel


TECH STACK USED
LABELSTUDIO – Open source tool used for image labelling and to download the respective annotation files to run the model
ULTRALYTICS – to run YOLO V11 model
YOLO V11 – to train the custom dataset
Python 3.12
Pytorch – CUDA 12.6 (for enabling GPU option)
Anaconda prompt– To train, validate and deploy the model using python code

DATA PREPARATION
A custom dataset consisting of 70-plus images (including real-time and collected online) is used to train the model, as there is scarce availability of images globally for the chosen problem statement.
After collecting the data, it is labelled using LabelStudio to generate annotations/labels, which are used for YOLO models
Sample of the input images for Gas stove on without vessel or with vessel as depicted on the right

OUTCOME
Our model can identify gas stove on_with vessel with confidence score of 88
Can identify gas stove on_without vessel with confidence score of 63
Improvements can be done to increase the predictions using large amount of datasets and better model for prediction





