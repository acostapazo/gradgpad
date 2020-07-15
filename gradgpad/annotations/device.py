from enum import Enum
from typing import List


class Device(Enum):
    DIGITAL_CAMARA = "digital_camara"
    MOBILE_TABLET = "mobile_tablet"
    WEBCAM = "webcam"

    @staticmethod
    def options() -> List:
        return [Device.DIGITAL_CAMARA, Device.MOBILE_TABLET, Device.WEBCAM]
