from enum import Enum


class Metric(Enum):
    BPCER = 1
    APCER_AGGREGATE = 2
    APCER_SPECIFIC = 3
    BPCER_AT_APCER_10_SPECIFIC = 4
    BPCER_AT_APCER_15_SPECIFIC = 5
    BPCER_AT_APCER_40_SPECIFIC = 6

    @staticmethod
    def available():
        return [
            "BPCER",
            "APCER_AGGREGATE",
            "APCER_SPECIFIC",
            "BPCER_AT_APCER_10_SPECIFIC",
            "BPCER_AT_APCER_15_SPECIFIC",
            "BPCER_AT_APCER_40_SPECIFIC",
        ]


def bpcer_metric_retriever(performance_info):
    value = performance_info.get("acer_info", {}).get("aggregate", {}).get("bpcer")
    return "BPCER", value


def apcer_aggregate_metric_retriever(performance_info):
    max_apcer_pai = (
        performance_info.get("acer_info", {}).get("aggregate", {}).get("max_apcer_pai")
    )
    num_pais = len(
        performance_info.get("acer_info", {})
        .get("aggregate", {})
        .get("apcer_per_pai", {})
    )
    value = (
        performance_info.get("acer_info", {})
        .get("aggregate", {})
        .get("apcer_per_pai", {})
        .get(max_apcer_pai)
    )
    return f"$APCER_{{{num_pais}-PAI}}$", value


def apcer_specific_metric_retriever(performance_info):
    max_apcer_pai = (
        performance_info.get("acer_info", {}).get("specific", {}).get("max_apcer_pai")
    )
    num_pais = len(
        performance_info.get("acer_info", {})
        .get("specific", {})
        .get("apcer_per_pai", {})
    )
    value = (
        performance_info.get("acer_info", {})
        .get("specific", {})
        .get("apcer_per_pai", {})
        .get(max_apcer_pai)
    )
    return f"$APCER_{{{num_pais}-PAI}}$", value


def bpcer_at_apcer_10_specific_metric_retriever(performance_info):
    bpcer_at_apcer_10 = (
        performance_info.get("acer_info", {})
        .get("specific", {})
        .get("relative_working_points", {})
        .get("bpcer", {})
        .get("apcer_10")
    )
    return "$BPCER @ APCER=10%$", bpcer_at_apcer_10


def bpcer_at_apcer_15_specific_metric_retriever(performance_info):
    bpcer_at_apcer_15 = (
        performance_info.get("acer_info", {})
        .get("specific", {})
        .get("relative_working_points", {})
        .get("bpcer", {})
        .get("apcer_15")
    )
    return "$BPCER @ APCER=15%$", bpcer_at_apcer_15


def bpcer_at_apcer_40_specific_metric_retriever(performance_info):
    bpcer_at_apcer_40 = (
        performance_info.get("acer_info", {})
        .get("specific", {})
        .get("relative_working_points", {})
        .get("bpcer", {})
        .get("apcer_40")
    )
    return "$BPCER @ APCER=40%$", bpcer_at_apcer_40


def metric_retriever_providers(metric: Metric):
    providers = {
        Metric.BPCER: bpcer_metric_retriever,
        Metric.APCER_AGGREGATE: apcer_aggregate_metric_retriever,
        Metric.APCER_SPECIFIC: apcer_specific_metric_retriever,
        Metric.BPCER_AT_APCER_10_SPECIFIC: bpcer_at_apcer_10_specific_metric_retriever,
        Metric.BPCER_AT_APCER_15_SPECIFIC: bpcer_at_apcer_15_specific_metric_retriever,
        Metric.BPCER_AT_APCER_40_SPECIFIC: bpcer_at_apcer_40_specific_metric_retriever,
    }

    metric_retriever = providers.get(metric)

    if not metric_retriever:
        raise TypeError(
            f"Metric selected is not supported. Please, try with {Metric.available()}"
        )

    return metric_retriever
