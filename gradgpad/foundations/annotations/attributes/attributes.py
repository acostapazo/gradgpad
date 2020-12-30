from gradgpad.foundations.annotations.attributes.personal_attributes import (
    PersonAttributes,
)
from gradgpad.foundations.annotations.attributes.conditions_attributes import (
    ConditionsAttributes,
)


class Attributes:
    def __init__(self, person: PersonAttributes, conditions: ConditionsAttributes):
        self.person = person
        self.conditions = conditions

    @staticmethod
    def from_item(item):
        return Attributes(
            person=PersonAttributes.from_item(item),
            conditions=ConditionsAttributes.from_item(item),
        )

    @staticmethod
    def from_dict(kdict):
        return Attributes(
            person=PersonAttributes.from_dict(kdict.get("person")),
            conditions=ConditionsAttributes.from_dict(kdict.get("conditions")),
        )

    def to_dict(self):
        return {
            "person": self.person.to_dict(),
            "conditions": self.conditions.to_dict(),
        }
