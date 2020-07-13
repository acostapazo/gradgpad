from gradgpad.annotations.dataset import Dataset
from gradgpad.annotations.person_attributes import Gender, Age, SkinTone


class Filter:
    def __init__(
        self,
        gender: Gender = None,
        age: Age = None,
        skin_tone: SkinTone = None,
        dataset: Dataset = None,
        random_values: int = None,
        pseudo_random_values: int = None,
    ):
        self.gender = gender
        self.age = age
        self.skin_tone = skin_tone
        self.dataset = dataset
        self.random_values = random_values
        self.pseudo_random_values = pseudo_random_values
