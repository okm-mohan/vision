"""Phase 2 YOLO adapter. Install opencv-python and ultralytics to enable."""
from dataclasses import dataclass
@dataclass
class Detection:
    label: str; confidence: float; box: tuple[int, int, int, int]; tracking_id: str | None = None
class YOLODetector:
    supported_classes = {'person','bicycle','car','motorcycle','bus','truck','dog','cat'}
    def __init__(self, model_name: str = 'yolo11n.pt'): self.model_name, self.model = model_name, None
    def start(self):
        from ultralytics import YOLO
        self.model = YOLO(self.model_name)
    def detect(self, frame):
        if self.model is None: raise RuntimeError('Detector not started')
        result = self.model(frame, verbose=False)[0]
        return [Detection(result.names[int(b.cls[0])], float(b.conf[0]), tuple(map(int,b.xyxy[0].tolist()))) for b in result.boxes if result.names[int(b.cls[0])] in self.supported_classes]
