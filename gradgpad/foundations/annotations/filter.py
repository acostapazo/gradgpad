from gradgpad.foundations.annotations.dataset import Dataset
from gradgpad.foundations.annotations.person_attributes import Sex, Age, SkinTone
from gradgpad.foundations.annotations.scenario import Scenario


class Filter:
    def __init__(
        self,
        scenario: Scenario = None,
        sex: Sex = None,
        age: Age = None,
        skin_tone: SkinTone = None,
        dataset: Dataset = None,
        random_values: int = None,
        pseudo_random_values: int = None,
    ):
        self.scenario = scenario
        self.sex = sex
        self.age = age
        self.skin_tone = skin_tone
        self.dataset = dataset
        self.random_values = random_values
        self.pseudo_random_values = pseudo_random_values
