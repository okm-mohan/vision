class ObjectTracker:
    """Simple contract ready to replace with ByteTrack in Phase 3."""
    def update(self, detections):
        for index, detection in enumerate(detections, 1): detection.tracking_id = f'{detection.label[:1].upper()}{index:03}'
        return detections
