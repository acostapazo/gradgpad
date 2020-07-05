class PersonAttributes:
    def __init__(self, gender: int, skin_tone: int, age: int):
        self.gender = gender
        self.skin_tone = skin_tone
        self.age = age

    @staticmethod
    def from_item(item):
        return PersonAttributes(
            gender=int(item.info.get("gender", -1)),
            skin_tone=int(item.info.get("skin_tone", -1)),
            age=int(item.info.get("age", -1)),
        )

    @staticmethod
    def from_dict(kdict):
        return PersonAttributes(
            gender=kdict.get("gender"),
            skin_tone=kdict.get("skin_tone"),
            age=kdict.get("age"),
        )

    def to_dict(self):
        return {"gender": self.gender, "skin_tone": self.skin_tone, "age": self.age}
