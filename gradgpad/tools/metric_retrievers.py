from enum import Enum


class Metric(Enum):
    BPCER = 1
    APCER_AGGREGATE = 2
    APCER_SPECIFIC = 3

    @staticmethod
    def available():
        return ["BPCER", "APCER_AGGREGATE", "APCER_SPECIFIC"]


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


metric_providers = {
    "BPCER": bpcer_metric_retriever,
    "APCER_AGGREGATE": apcer_aggregate_metric_retriever,
    "APCER_SPECIFIC": apcer_specific_metric_retriever,
}


def metric_retriever_providers(metric: Metric):
    providers = {
        Metric.BPCER: bpcer_metric_retriever,
        Metric.APCER_AGGREGATE: apcer_aggregate_metric_retriever,
        Metric.APCER_SPECIFIC: apcer_specific_metric_retriever,
    }

    metric_retriever = providers.get(metric)

    if not metric_retriever:
        raise TypeError(
            f"Metric selected is not supported. Please, try with {Metric.available()}"
        )

    return metric_retriever
