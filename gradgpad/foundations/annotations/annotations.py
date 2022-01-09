import json
from typing import List

from gradgpad.foundations.annotations.annotation import Annotation
from gradgpad.foundations.annotations.correspondences import ANNOTATION_CORRESPONDENCES
from gradgpad.foundations.annotations.stats.calculate_pai_stats import (
    calculate_pai_stats,
)
from gradgpad.public_api import GRADGPAD_PATH


class Annotations:
    def __init__(
        self,
        annotated_samples: List = [],
        correspondences: dict = ANNOTATION_CORRESPONDENCES,
    ):
        self.annotated_samples = annotated_samples
        self.correspondences = correspondences

    # @staticmethod
    # def from_items(items):
    #     annotations = Annotations()
    #     for item in items:
    #         annotations.add_item(item)
    #     return annotations

    @staticmethod
    def from_dict(kdicts):
        kannotations = [
            Annotation.from_dict(kdict) for kdict in kdicts.get("annotations")
        ]
        return Annotations(kannotations)

    @staticmethod
    def load(filename: str):
        with open(filename, "r") as f:
            kdict = json.load(f)
        return Annotations.from_dict(kdict)

    # def add_item(self, item):
    #     self.annotated_samples.append(Annotation.from_item(item))

    def to_dict(self):
        return {
            "annotations": [
                annotation.to_dict() for annotation in self.annotated_samples
            ],
            "num_annotations": len(self.annotated_samples),
            "correspondences": self.correspondences,
        }

    def get_annotations_from_ids(self, ids: List[str]):
        return [
            annotation for annotation in self.annotated_samples if annotation.id in ids
        ]

    @property
    def num_annotations(self):
        return len(self.annotated_samples)

    def save(self, filename: str):
        with open(filename, "w") as f:
            json.dump(self.to_dict(), f, indent=4, sort_keys=True)

    def statistics(self):
        return calculate_pai_stats(self.annotated_samples)

    def print(self):
        print(json.dumps(self.to_dict(), indent=4, sort_keys=True))

    def print_semantic(self, annotation_index: int = None):
        semantic_annotations = []
        selected_annotations = self.annotated_samples
        if annotation_index is not None:
            if annotation_index >= len(selected_annotations):
                raise IndexError(
                    f"annotation_index exceed the total number of annotations (max index {len(selected_annotations)})"
                )
            selected_annotations = [selected_annotations[annotation_index]]

        for annotation in selected_annotations:
            semantic_annotations.append(
                {
                    "id": annotation.id,
                    "media": annotation.media,
                    "dataset": annotation.dataset.value,
                    "categorization": {
                        "coarse_grained_pai": self.correspondences.get(
                            "categorization", {}
                        )
                        .get("coarse_grained_pai")
                        .get(annotation.categorization.get("coarse_grained_pai")),
                        "fine_grained_pai": self.correspondences.get(
                            "categorization", {}
                        )
                        .get("fine_grained_pai")
                        .get(annotation.categorization.get("fine_grained_pai")),
                        "pas_type": annotation.categorization.get("pas_type"),
                    },
                    "attributes": {
                        "person": {
                            "sex": self.correspondences.get("attributes", {})
                            .get("person")
                            .get("sex")
                            .get(annotation.attributes.person.sex),
                            "skin_tone": self.correspondences.get("attributes", {})
                            .get("person")
                            .get("skin_tone")
                            .get(annotation.attributes.person.skin_tone),
                            "age": self.correspondences.get("attributes", {})
                            .get("person")
                            .get("age")
                            .get(annotation.attributes.person.age),
                        },
                        "conditions": {
                            "lighting": self.correspondences.get("attributes", {})
                            .get("conditions")
                            .get("lighting")
                            .get(annotation.attributes.conditions.lighting),
                            "capture_device": self.correspondences.get("attributes", {})
                            .get("conditions")
                            .get("capture_device")
                            .get(annotation.attributes.conditions.capture_device),
                        },
                    },
                }
            )
        print(
            json.dumps({"annotations": semantic_annotations}, indent=4, sort_keys=True)
        )


annotations = Annotations.load(f"{GRADGPAD_PATH}/data/gradgpad_annotations.json")
