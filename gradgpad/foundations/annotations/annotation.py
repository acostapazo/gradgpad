import json
from typing import Dict, Any

from gradgpad.foundations.annotations.attributes.attributes import Attributes
from gradgpad.foundations.annotations.dataset_name import DatasetName


class Annotation:
    def __init__(
        self,
        id: str,
        media: str,
        dataset: DatasetName,
        categorization: Dict[str, Any],
        attributes: Attributes,
    ):
        self.id = id
        self.media = media
        self.dataset = dataset
        self.categorization = categorization
        self.attributes = attributes

    # @staticmethod
    # def from_item(item):
    #     return Annotation(
    #         id=item.id,
    #         media=item.media,
    #         dataset=DatasetName.from_item(item),
    #         categorization={
    #             "coarse_grained_pai": int(item.label),
    #             "fine_grained_pai": int(item.info.get("common_pai", -1)),
    #             "pas_type": int(item.info.get("type_pai", -1)),
    #         },
    #         attributes=Attributes.from_item(item),
    #     )

    @staticmethod
    def from_dict(kdict):
        return Annotation(
            id=kdict.get("id"),
            media=kdict.get("media"),
            dataset=DatasetName(kdict.get("dataset")),
            categorization=kdict.get("categorization"),
            attributes=Attributes.from_dict(kdict.get("attributes")),
        )

    def to_dict(self):
        return {
            "id": self.id,
            "media": self.media,
            "dataset": self.dataset.value,
            "categorization": self.categorization,
            "attributes": self.attributes.to_dict(),
        }

    def __repr__(self):
        return f"Annotation: {json.dumps(self.to_dict(), indent=4, sort_keys=True)}"
