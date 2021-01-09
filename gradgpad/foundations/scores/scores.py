import random
import numpy as np

from typing import List, Dict, Callable

from sklearn.preprocessing import LabelEncoder

from gradgpad.foundations.annotations.annotation import Annotation
from gradgpad.foundations.annotations.dataset import Dataset
from gradgpad.foundations.annotations.filter import Filter
from gradgpad.foundations.annotations.person_attributes import Sex, Age, SkinTone
from gradgpad.foundations.annotations.scenario import Scenario
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
            annotations_from_ids, Filter(scenario=Scenario.GENUINE)
        )
        scores = [score for id, score in self.scores.items() if id in filtered_ids]
        return scores

    def get_attacks(self):
        ids = self.scores.keys()
        annotations_from_ids = annotations.get_annotations_from_ids(ids)
        filtered_ids = self._get_filtered_ids(
            annotations_from_ids, Filter(scenario=Scenario.GENUINE)
        )
        scores = [score for id, score in self.scores.items() if id not in filtered_ids]
        return scores

    def get_attacks_with_ids(self):
        ids = self.scores.keys()
        annotations_from_ids = annotations.get_annotations_from_ids(ids)
        filtered_ids = self._get_filtered_ids(
            annotations_from_ids, Filter(scenario=Scenario.GENUINE)
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
            annotations_from_ids, Filter(scenario=Scenario.GENUINE)
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
            if annotation.categorization.get("fine_grained_pai") == 0:
                scores.append(self.scores[id])
                labels.append(0)
            elif annotation.categorization.get("fine_grained_pai") in pai_labels:
                scores.append(self.scores[id])
                labels.append(1)

        return (
            np.asarray(list(scores), dtype=np.float32),
            np.asarray(labels, dtype=np.int),
        )

    def _get_numpy_labels_filter_by_filter(
        self,
        options: List,
        filter_provider: Callable,
        unknown_label_value: int = None,
        encode_label: bool = False,
    ):
        ids = self.scores.keys()
        annotations_from_ids = annotations.get_annotations_from_ids(ids)

        filtered_ids_by_subdivision = {}
        filtered_ids_order = {}

        for order, option in enumerate(options):
            filtered_ids_by_subdivision[option] = self._get_filtered_ids(
                annotations_from_ids, filter_provider(option)
            )
            filtered_ids_order[option] = order

        labels = []

        for id in ids:
            value = None
            for subdivision, filtered_ids in filtered_ids_by_subdivision.items():
                if id in filtered_ids:
                    value = subdivision.value
                    break
            if value is None and unknown_label_value is not None:
                value = unknown_label_value

            labels.append(value)

        if encode_label:
            le = LabelEncoder()
            labels = le.fit_transform(labels)
            le_name_mapping = dict(zip(le.classes_, le.transform(le.classes_)))
            if le_name_mapping.get(str(unknown_label_value)) is not None:
                labels = [label - 1 for label in labels]

        return np.asarray(labels, dtype=np.int)

    def get_numpy_labels_by_scenario(self):
        return self._get_numpy_labels_filter_by_filter(
            Scenario.options(), lambda option: Filter(scenario=option)
        )

    def get_numpy_labels_by_sex(self):
        return self._get_numpy_labels_filter_by_filter(
            Sex.options(), lambda option: Filter(sex=option), unknown_label_value=-1
        )

    def get_numpy_labels_by_age(self):
        return self._get_numpy_labels_filter_by_filter(
            Age.options(), lambda option: Filter(age=option), unknown_label_value=-1
        )

    def get_numpy_labels_by_skin_tone(self):
        return self._get_numpy_labels_filter_by_filter(
            SkinTone.options(),
            lambda option: Filter(skin_tone=option),
            unknown_label_value=-1,
        )

    def get_numpy_labels_by_dataset(self):
        return self._get_numpy_labels_filter_by_filter(
            Dataset.options(),
            lambda option: Filter(dataset=option),
            unknown_label_value=-1,
            encode_label=True,
        )

    def get_numpy_labels_by_dataset_and_scenario(self, scenario: Scenario):
        return self._get_numpy_labels_filter_by_filter(
            Dataset.options(),
            lambda option: Filter(scenario=scenario, dataset=option),
            unknown_label_value=-1,
            encode_label=True,
        )

    def get_numpy_fine_grained_pai_labels(self):
        ids = self.scores.keys()
        annotations_from_ids = annotations.get_annotations_from_ids(ids)
        fine_grained_pai_labels = [
            annotation.categorization.get("fine_grained_pai")
            for annotation in annotations_from_ids
        ]
        return np.asarray(fine_grained_pai_labels, dtype=np.int)

    def _get_smallest_length(self, x):
        return [
            k for k in x.keys() if len(x.get(k)) == min([len(n) for n in x.values()])
        ]

    def get_fair_sex_subset(self) -> Dict[str, Dict]:
        def sex_filter_provider(sex, dataset, pseudo_random_values=None):
            return Filter(
                scenario=Scenario.GENUINE,
                sex=sex,
                dataset=dataset,
                pseudo_random_values=pseudo_random_values,
            )

        return self.get_fair_subset(Sex.options(), sex_filter_provider)

    def get_fair_age_subset(self) -> Dict[str, Dict]:
        def age_filter_provider(age, dataset, pseudo_random_values=None):
            return Filter(
                scenario=Scenario.GENUINE,
                age=age,
                dataset=dataset,
                pseudo_random_values=pseudo_random_values,
            )

        return self.get_fair_subset(Age.options(), age_filter_provider)

    def get_fair_skin_tone_subset(self) -> Dict[str, Dict]:
        def skin_tone_filter_provider(skin_tone, dataset, pseudo_random_values=None):
            return Filter(
                scenario=Scenario.GENUINE,
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
            if (
                filter.scenario
                and annotation.categorization.get("pas_type") != filter.scenario.value
            ):
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
