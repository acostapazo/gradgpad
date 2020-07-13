import json
import os
import random
from typing import List

from gradgpad.annotations.annotation import Annotation
from gradgpad.annotations.correspondences import ANNOTATION_CORRESPONDENCES
from gradgpad.annotations.filter import Filter


class Annotations:
    def __init__(
        self, annotations: List = [], correspondences: dict = ANNOTATION_CORRESPONDENCES
    ):
        self.annotations = annotations
        self.correspondences = correspondences

    @staticmethod
    def from_items(items):
        annotations = Annotations()
        for item in items:
            annotations.add_item(item)
        return annotations

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

    def add_item(self, item):
        self.annotations.append(Annotation.from_item(item))

    def to_dict(self):
        return {
            "annotations": [annotation.to_dict() for annotation in self.annotations],
            "num_annotations": len(self.annotations),
            "correspondences": self.correspondences,
        }

    def get_ids(self, filter: Filter = Filter()):
        ids = []
        for annotation in self.annotations:
            if (
                filter.gender
                and annotation.attributes.person.gender != filter.gender.value
            ):
                continue
            if filter.age and annotation.attributes.person.age != filter.age.value:
                continue
            if (
                filter.skin_tone
                and annotation.attributes.person.skin_tone != filter.skin_tone.value
            ):
                continue

            if filter.dataset and annotation.dataset.value != filter.dataset.value:
                continue
            ids.append(annotation.id)

        if filter.random_values:
            if len(ids) < filter.random_values:
                raise ValueError(
                    "Error Filter: Required random_values is lower than filtered values"
                )
            else:
                ids = random.sample(ids, filter.random_values)

        if filter.pseudo_random_values:
            if len(ids) < filter.pseudo_random_values:
                raise ValueError(
                    "Error Filter: Required pseudo_random_values is lower than filtered values"
                )
            else:
                random.seed(len(ids))
                ids = random.sample(ids, filter.pseudo_random_values)

        return ids

    @property
    def num_annotations(self):
        return len(self.annotations)

    def save(self, filename: str):
        with open(filename, "w") as f:
            json.dump(self.to_dict(), f, indent=4, sort_keys=True)

    def print(self):
        print(json.dumps(self.to_dict(), indent=4, sort_keys=True))

    def print_semantic_annotations(self):
        semantic_annotations = []
        for annotation in self.annotations:
            semantic_annotations.append(
                {
                    "id": annotation.id,
                    "media": annotation.media,
                    "dataset": annotation.dataset.value,
                    "spai": {
                        "classical": self.correspondences.get("spai", {})
                        .get("classical")
                        .get(annotation.spai.get("classical")),
                        "specific": self.correspondences.get("spai", {})
                        .get("specific")
                        .get(annotation.spai.get("specific")),
                        "type": annotation.spai.get("type"),
                    },
                    "attributes": {
                        "person": {
                            "gender": self.correspondences.get("attributes", {})
                            .get("person")
                            .get("gender")
                            .get(annotation.attributes.person.gender),
                            "skin_tone": self.correspondences.get("attributes", {})
                            .get("person")
                            .get("skin_tone")
                            .get(annotation.attributes.person.skin_tone),
                            "age": self.correspondences.get("attributes", {})
                            .get("person")
                            .get("age")
                            .get(annotation.attributes.person.age),
                        },
                        "scenario": {
                            "lighting": self.correspondences.get("attributes", {})
                            .get("scenario")
                            .get("lighting")
                            .get(annotation.attributes.scenario.lighting),
                            "capture_device": self.correspondences.get("attributes", {})
                            .get("scenario")
                            .get("capture_device")
                            .get(annotation.attributes.scenario.capture_device),
                        },
                    },
                }
            )
        print(
            json.dumps({"annotations": semantic_annotations}, indent=4, sort_keys=True)
        )


ANNOTATIONS_DIR = os.path.abspath(os.path.dirname(__file__))
annotations = Annotations.load(f"{ANNOTATIONS_DIR}/gradgpad_annotations.json")
