import random
import numpy as np

from typing import List, Dict, Callable

from gradgpad.annotations.annotation import Annotation
from gradgpad.annotations.dataset import Dataset
from gradgpad.annotations.filter import Filter
from gradgpad.annotations.person_attributes import Sex, Age, SkinTone
from gradgpad.annotations.spai import Spai
from gradgpad.tools.open_result_json import open_result_json
from gradgpad import annotations


class Scores:
    @staticmethod
    def from_filename(filename: str):
        return Scores(open_result_json(filename))

    def __init__(self, scores: Dict = None):
        self.scores = scores

    def get_genuine(self):
        ids = self.scores.keys()
        annotations_from_ids = annotations.get_annotations_from_ids(ids)
        filtered_ids = self._get_filtered_ids(
            annotations_from_ids, Filter(spai=Spai.GENUINE)
        )
        scores = [score for id, score in self.scores.items() if id in filtered_ids]
        return scores

    def get_attacks(self):
        ids = self.scores.keys()
        annotations_from_ids = annotations.get_annotations_from_ids(ids)
        filtered_ids = self._get_filtered_ids(
            annotations_from_ids, Filter(spai=Spai.GENUINE)
        )
        scores = [score for id, score in self.scores.items() if id not in filtered_ids]
        return scores

    def get_attacks_with_ids(self):
        ids = self.scores.keys()
        annotations_from_ids = annotations.get_annotations_from_ids(ids)
        filtered_ids = self._get_filtered_ids(
            annotations_from_ids, Filter(spai=Spai.GENUINE)
        )
        scores = {
            id: score for id, score in self.scores.items() if id not in filtered_ids
        }
        return scores

    def get_numpy_scores(self):
        return np.asarray(list(self.scores.values()), dtype=np.float32)

    def get_numpy_labels(self):
        ids = self.scores.keys()
        annotations_from_ids = annotations.get_annotations_from_ids(ids)
        filtered_ids = self._get_filtered_ids(
            annotations_from_ids, Filter(spai=Spai.GENUINE)
        )
        labels = [0 if id in filtered_ids else 1 for id in ids]
        return np.asarray(labels, dtype=np.int)

    def get_numpy_scores_and_labels_filtered_by_labels(self, pai_labels=None):
        if not pai_labels:
            return self.get_numpy_scores(), self.get_numpy_labels()

        ids = self.scores.keys()
        annotations_from_ids = annotations.get_annotations_from_ids(ids)
        # filtered_ids = self._get_filtered_ids(
        #     annotations_from_ids, Filter(spai=Spai.GENUINE)
        # )
        scores = []
        labels = []
        for id in ids:
            annotation = [
                annotation for annotation in annotations_from_ids if annotation.id == id
            ][0]
            if annotation.spai.get("specific") == 0:
                scores.append(self.scores[id])
                labels.append(0)
            elif annotation.spai.get("specific") in pai_labels:
                scores.append(self.scores[id])
                labels.append(1)

        return (
            np.asarray(list(scores), dtype=np.float32),
            np.asarray(labels, dtype=np.int),
        )

    def get_numpy_labels_by_type_pai(self):
        ids = self.scores.keys()
        annotations_from_ids = annotations.get_annotations_from_ids(ids)
        genuine_filtered_ids = self._get_filtered_ids(
            annotations_from_ids, Filter(spai=Spai.GENUINE)
        )
        type_I_filtered_ids = self._get_filtered_ids(
            annotations_from_ids, Filter(spai=Spai.PAI_TYPE_I)
        )
        type_II_filtered_ids = self._get_filtered_ids(
            annotations_from_ids, Filter(spai=Spai.PAI_TYPE_II)
        )
        type_III_filtered_ids = self._get_filtered_ids(
            annotations_from_ids, Filter(spai=Spai.PAI_TYPE_III)
        )

        labels = []
        for id in ids:
            if id in genuine_filtered_ids:
                label = 0
            elif id in type_I_filtered_ids:
                label = 1
            elif id in type_II_filtered_ids:
                label = 2
            elif id in type_III_filtered_ids:
                label = 3
            else:
                continue
            labels.append(label)

        return np.asarray(labels, dtype=np.int)

    def get_numpy_specific_pai_labels(self):
        ids = self.scores.keys()
        annotations_from_ids = annotations.get_annotations_from_ids(ids)
        specific_pais_labels = [
            annotation.spai.get("specific") for annotation in annotations_from_ids
        ]
        return np.asarray(specific_pais_labels, dtype=np.int)

    def _get_smallest_length(self, x):
        return [
            k for k in x.keys() if len(x.get(k)) == min([len(n) for n in x.values()])
        ]

    def get_fair_sex_subset(self) -> Dict[str, Dict]:
        def sex_filter_provider(sex, dataset, pseudo_random_values=None):
            return Filter(
                spai=Spai.GENUINE,
                sex=sex,
                dataset=dataset,
                pseudo_random_values=pseudo_random_values,
            )

        return self.get_fair_subset(Sex.options(), sex_filter_provider)

    def get_fair_age_subset(self) -> Dict[str, Dict]:
        def age_filter_provider(age, dataset, pseudo_random_values=None):
            return Filter(
                spai=Spai.GENUINE,
                age=age,
                dataset=dataset,
                pseudo_random_values=pseudo_random_values,
            )

        return self.get_fair_subset(Age.options(), age_filter_provider)

    def get_fair_skin_tone_subset(self) -> Dict[str, Dict]:
        def skin_tone_filter_provider(skin_tone, dataset, pseudo_random_values=None):
            return Filter(
                spai=Spai.GENUINE,
                skin_tone=skin_tone,
                dataset=dataset,
                pseudo_random_values=pseudo_random_values,
            )

        return self.get_fair_subset(SkinTone.options(), skin_tone_filter_provider)

    def get_fair_grouped_skin_tone_subset(self) -> Dict[str, Dict]:
        fair_skin_tone_subset = self.get_fair_skin_tone_subset()

        yellow = {}
        if "LIGHT_YELLOW" in fair_skin_tone_subset.keys():
            yellow = {**yellow, **fair_skin_tone_subset["LIGHT_YELLOW"]}
        if "MEDIUM_YELLOW_BROWN" in fair_skin_tone_subset.keys():
            yellow = {**yellow, **fair_skin_tone_subset["MEDIUM_YELLOW_BROWN"]}

        pink = {}
        if "LIGHT_PINK" in fair_skin_tone_subset.keys():
            pink = {**pink, **fair_skin_tone_subset["LIGHT_PINK"]}
        if "MEDIUM_PINK_BROWN" in fair_skin_tone_subset.keys():
            pink = {**pink, **fair_skin_tone_subset["MEDIUM_PINK_BROWN"]}

        dark = {}
        if "MEDIUM_DARK_BROWN" in fair_skin_tone_subset.keys():
            dark = {**dark, **fair_skin_tone_subset["MEDIUM_DARK_BROWN"]}
        if "DARK_BROWN" in fair_skin_tone_subset.keys():
            dark = {**dark, **fair_skin_tone_subset["DARK_BROWN"]}

        grouped_fair_skin_tone_subset = {"YELLOW": yellow, "PINK": pink, "BROWN": dark}
        return grouped_fair_skin_tone_subset

    def get_fair_subset(
        self, demographic_options: List, filter_provider: Callable
    ) -> Dict[str, Dict]:

        required_num_scores = {}
        for dataset in Dataset.options():
            filters = {
                demographic.name: filter_provider(demographic, dataset)
                for demographic in demographic_options
            }

            filtered_scores = {}
            for key, filter in filters.items():
                filtered_scores[key] = self.filtered_by(filter)

            smallest_key = self._get_smallest_length(filtered_scores)[0]
            required_num_scores[dataset] = len(filtered_scores[smallest_key])

        fair_demographic_scores = {}

        for dataset, required_num_score in required_num_scores.items():
            if required_num_score == 0:
                continue

            for demographic in demographic_options:
                filtered_scores = self.filtered_by(
                    filter_provider(demographic, dataset, required_num_score)
                )
                # print(f"{demographic.value} | {dataset.value} -> {len(filtered_scores)}")

                if demographic.name not in fair_demographic_scores:
                    fair_demographic_scores[demographic.name] = filtered_scores
                else:
                    fair_demographic_scores[demographic.name].update(filtered_scores)
        return fair_demographic_scores

    def filtered_by(self, filter: Filter):
        ids = self.scores.keys()
        annotations_from_ids = annotations.get_annotations_from_ids(ids)

        filtered_ids = self._get_filtered_ids(annotations_from_ids, filter)

        return {key: value for key, value in self.scores.items() if key in filtered_ids}

    def _get_filtered_ids(self, annotations_from_ids: List[Annotation], filter: Filter):
        ids = []
        for annotation in annotations_from_ids:
            if filter.spai and annotation.spai.get("type") != filter.spai.value:
                continue
            if filter.sex and annotation.attributes.person.sex != filter.sex.value:
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

    def length(self):
        return len(self.scores)
