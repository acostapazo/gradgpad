class ConditionsAttributes:
    def __init__(self, lighting: int, capture_device: int):
        self.lighting = lighting
        self.capture_device = capture_device

    @staticmethod
    def from_item(item):
        return ConditionsAttributes(
            lighting=int(item.info.get("common_lighting", -1)),
            capture_device=int(item.info.get("common_capture_device", -1)),
        )

    @staticmethod
    def from_dict(kdict):
        return ConditionsAttributes(
            lighting=kdict.get("lighting"), capture_device=kdict.get("capture_device")
        )

    def to_dict(self):
        return {"lighting": self.lighting, "capture_device": self.capture_device}
