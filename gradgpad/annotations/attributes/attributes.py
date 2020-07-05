from gradgpad.annotations.attributes.personal_attributes import PersonAttributes
from gradgpad.annotations.attributes.scenario_attributes import ScenarioAttributes


class Attributes:
    def __init__(self, person: PersonAttributes, scenario: ScenarioAttributes):
        self.person = person
        self.scenario = scenario

    @staticmethod
    def from_item(item):
        return Attributes(
            person=PersonAttributes.from_item(item),
            scenario=ScenarioAttributes.from_item(item),
        )

    @staticmethod
    def from_dict(kdict):
        return Attributes(
            person=PersonAttributes.from_dict(kdict.get("person")),
            scenario=ScenarioAttributes.from_dict(kdict.get("scenario")),
        )

    def to_dict(self):
        return {"person": self.person.to_dict(), "scenario": self.scenario.to_dict()}
