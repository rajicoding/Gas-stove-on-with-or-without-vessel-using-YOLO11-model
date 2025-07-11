from ultralytics import YOLO

model= YOLO("yolo11_gasdetection.pt")

model.predict(source="val_3.jpg", show = True, save=True, conf=0.6, 
	line_width=2)

