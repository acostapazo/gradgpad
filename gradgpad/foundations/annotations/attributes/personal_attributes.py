class PersonAttributes:
    def __init__(self, sex: int, skin_tone: int, age: int):
        self.sex = sex
        self.skin_tone = skin_tone
        self.age = age

    @staticmethod
    def from_item(item):
        return PersonAttributes(
            sex=int(item.info.get("sex", -1)),
            skin_tone=int(item.info.get("skin_tone", -1)),
            age=int(item.info.get("age", -1)),
        )

    @staticmethod
    def from_dict(kdict):
        return PersonAttributes(
            sex=kdict.get("sex"), skin_tone=kdict.get("skin_tone"), age=kdict.get("age")
        )

    def to_dict(self):
        return {"sex": self.sex, "skin_tone": self.skin_tone, "age": self.age}
