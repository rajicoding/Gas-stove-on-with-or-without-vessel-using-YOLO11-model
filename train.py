from ultralytics import YOLO

model=YOLO("yolo11m.pt")	

model.train(data="Gasstove_Detection.yaml", imgsz = 640, 
	batch=8, epochs=60, workers=0, device=0)