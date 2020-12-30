import pandas as pd


def create_dataframe(metric_retriever, results):

    data = {"Metric": [], "Error Rate (%)": [], "Protocol": []}

    for protocol_name, performance_info in sorted(results.items()):
        metric, value = metric_retriever(performance_info)
        data["Metric"].append(metric)
        data["Error Rate (%)"].append(value)
        data["Protocol"].append(protocol_name)
    df = pd.DataFrame(data, columns=list(data.keys()))
    return df
