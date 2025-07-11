#validation.metrics

from ultralytics import YOLO

model=YOLO("yolo11_gasstove_best.pt")

model.export(format="onnx")