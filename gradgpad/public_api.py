import os

CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))

modules = []
classes = []

__all__ = modules + classes

GRADGPAD_PATH = os.path.abspath(os.path.dirname(__file__))
GRADGPAD_SCORES_PATH = f"{GRADGPAD_PATH}/data/scores/"

os.environ["GRADGPAD_PATH"] = GRADGPAD_PATH
os.environ["GRADGPAD_SCORES_PATH"] = GRADGPAD_SCORES_PATH
