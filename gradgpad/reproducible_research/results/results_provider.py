from gradgpad.annotations.coarse_grain_pai import CoarseGrainPai
from gradgpad.annotations.dataset import Dataset
from gradgpad.annotations.device import Device
from gradgpad.evaluation.metrics.metrics import Metrics
from gradgpad.reproducible_research import Dict, Scores
from gradgpad.reproducible_research.scores.approach import Approach
from gradgpad.reproducible_research.scores.protocol import Protocol
from gradgpad.reproducible_research.scores.scores_provider import ScoresProvider
from gradgpad.reproducible_research.scores.subset import Subset


def get_analysis_from_metrics(metrics: Metrics) -> Dict:
    bpcer_fixing_working_points = [
        0.01,
        0.05,
        0.1,
        0.15,
        0.20,
        0.25,
        0.30,
        0.35,
        0.40,
        0.45,
        0.5,
    ]  # [0.05, 0.1, 0.15, 0.20, 0.30, 0.40]
    apcer_fixing_working_points = [
        0.05,
        0.1,
        0.15,
        0.20,
        0.25,
        0.30,
    ]  # [0.05, 0.1, 0.15, 0.20, 0.30, 0.40]

    analysis = metrics.get_indeepth_analysis(
        bpcer_fixing_working_points, apcer_fixing_working_points
    )

    return analysis


class ResultsProvider:
    @staticmethod
    def grandtest(approach: Approach) -> Dict[str, Dict]:
        protocol = Protocol.GRANDTEST
        return {
            f"{protocol.value}": ResultsProvider.get(
                approach=approach, protocol=protocol
            )
        }

    @staticmethod
    def cross_dataset(approach: Approach) -> Dict[str, Dict]:
        results = {}
        protocol = Protocol.CROSS_DATASET

        for dataset in Dataset.options():
            key = f"{protocol.value}_{dataset.value}"

            results[key] = ResultsProvider.get(
                approach=approach, protocol=protocol, dataset=dataset
            )
        return results

    @staticmethod
    def lodo(approach: Approach) -> Dict[str, Dict]:
        results = {}
        protocol = Protocol.LODO

        for dataset in Dataset.options():
            key = f"{protocol.value}_{dataset.value}"

            results[key] = ResultsProvider.get(
                approach=approach, protocol=protocol, dataset=dataset
            )
        return results

    @staticmethod
    def intradataset(approach: Approach) -> Dict[str, Dict]:
        results = {}
        protocol = Protocol.INTRADATASET

        for dataset in Dataset.options():
            key = f"{protocol.value}_{dataset.value}"

            results[key] = ResultsProvider.get(
                approach=approach, protocol=protocol, dataset=dataset
            )
        return results

    @staticmethod
    def cross_device(approach: Approach) -> Dict[str, Dict]:
        results = {}
        protocol = Protocol.CROSS_DEVICE

        for device in Device.options():
            key = f"{protocol.value}_{device.value}"

            results[key] = ResultsProvider.get(
                approach=approach, protocol=protocol, device=device
            )
        return results

    @staticmethod
    def unseen_attack(approach: Approach) -> Dict[str, Dict]:
        results = {}
        protocol = Protocol.UNSEEN_ATTACK

        for pai in CoarseGrainPai.options():
            key = f"{protocol.value}_{pai.value}"

            results[key] = ResultsProvider.get(
                approach=approach, protocol=protocol, pai=pai
            )
        return results

    @staticmethod
    def all(approach: Approach) -> Dict[str, Dict]:
        results = {}
        results.update(ResultsProvider.grandtest(approach))
        results.update(ResultsProvider.cross_dataset(approach))
        results.update(ResultsProvider.lodo(approach))
        results.update(ResultsProvider.cross_device(approach))
        results.update(ResultsProvider.unseen_attack(approach))
        # results.update(ResultsProvider.intradataset(approach))
        return results

    @staticmethod
    def get(
        approach: Approach,
        protocol: Protocol,
        dataset: Dataset = None,
        device: Device = None,
        pai: CoarseGrainPai = None,
    ) -> Dict:
        scores_subsets = {
            subset.value: ScoresProvider.get(
                approach=approach,
                protocol=protocol,
                subset=subset,
                dataset=dataset,
                device=device,
                pai=pai,
            )
            for subset in Subset.options()
        }
        metrics = Metrics(
            devel_scores=scores_subsets.get(Subset.DEVEL.value),
            test_scores=scores_subsets.get(Subset.TEST.value),
        )
        return get_analysis_from_metrics(metrics)

    @staticmethod
    def get_grandtest_sex(approach: Approach) -> Dict:
        scores_subsets = {}
        for subset in Subset.options():
            grandtest_sex_scores = ScoresProvider.get(
                approach=approach, protocol=Protocol.GRANDTEST, subset=subset
            ).get_fair_sex_subset()
            scores_subsets[subset.value] = Scores(scores=grandtest_sex_scores)

        metrics = Metrics(
            devel_scores=scores_subsets.get(Subset.DEVEL.value),
            test_scores=scores_subsets.get(Subset.TEST.value),
        )
        return get_analysis_from_metrics(metrics)

    @staticmethod
    def get_grandtest_age(approach: Approach) -> Dict:
        scores_subsets = {}
        for subset in Subset.options():
            grandtest_age_scores = ScoresProvider.get(
                approach=approach, protocol=Protocol.GRANDTEST, subset=subset
            ).get_fair_age_subset()
            scores_subsets[subset.value] = Scores(scores=grandtest_age_scores)

        metrics = Metrics(
            devel_scores=scores_subsets.get(Subset.DEVEL.value),
            test_scores=scores_subsets.get(Subset.TEST.value),
        )

        return get_analysis_from_metrics(metrics)

    @staticmethod
    def get_grandtest_skin_tone(approach: Approach) -> Dict:
        scores_subsets = {}
        for subset in Subset.options():
            grandtest_skin_tone_scores = ScoresProvider.get(
                approach=approach, protocol=Protocol.GRANDTEST, subset=subset
            ).get_fair_skin_tone_subset()
            scores_subsets[subset.value] = Scores(scores=grandtest_skin_tone_scores)

        metrics = Metrics(
            devel_scores=scores_subsets.get(Subset.DEVEL.value),
            test_scores=scores_subsets.get(Subset.TEST.value),
        )

        return get_analysis_from_metrics(metrics)
