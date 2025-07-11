from ultralytics import YOLO

# Load a model
model = YOLO("yolo11m.pt")  # load an official model
model = YOLO("yolo11_gasdetection.pt")  # load a custom model

# Validate the model
metrics = model.val(workers=0)  # no arguments needed, dataset and settings remembered
metrics.box.map  # map50-95
metrics.box.map50  # map50
metrics.box.map75  # map75
metrics.box.maps  # a list contains map50-95 of each category
print(metrics.box.map50)
print(metrics.box.map)