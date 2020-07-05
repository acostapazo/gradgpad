from typing import Dict, Any

from gradgpad.annotations.attributes.attributes import Attributes
from gradgpad.annotations.dataset_name import DatasetName


class Annotation:
    def __init__(
        self,
        id: str,
        media: str,
        dataset: DatasetName,
        spai: Dict[str, Any],
        attributes: Attributes,
    ):
        self.id = id
        self.media = media
        self.dataset = dataset
        self.spai = spai
        self.attributes = attributes

    @staticmethod
    def from_item(item):
        return Annotation(
            id=item.id,
            media=item.media,
            dataset=DatasetName.from_item(item),
            spai={
                "classical": int(item.label),
                "specific": int(item.info.get("common_pai", -1)),
                "type": int(item.info.get("type_pai", -1)),
            },
            attributes=Attributes.from_item(item),
        )

    @staticmethod
    def from_dict(kdict):
        return Annotation(
            id=kdict.get("id"),
            media=kdict.get("media"),
            dataset=DatasetName(kdict.get("dataset")),
            spai=kdict.get("spai"),
            attributes=Attributes.from_dict(kdict.get("attributes")),
        )

    def to_dict(self):
        return {
            "id": self.id,
            "media": self.media,
            "dataset": self.dataset.value,
            "spai": self.spai,
            "attributes": self.attributes.to_dict(),
        }
