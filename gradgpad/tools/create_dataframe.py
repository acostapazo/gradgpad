import pandas as pd


def bpcer_metric_retriever(performance_info):
    value = performance_info.get("acer_info", {}).get("aggregate", {}).get("bpcer")
    return "BPCER", value


def create_dataframe(metric_retriever, results):

    data = {"Metric": [], "Error Rate (%)": [], "Protocol": []}

    for protocol_name, performance_info in results.items():
        metric, value = metric_retriever(performance_info)
        data["Metric"].append(metric)
        data["Error Rate (%)"].append(value)
        data["Protocol"].append(protocol_name)
    df_metrics = pd.DataFrame(data, columns=data.keys())
    return df_metrics


#
# def create_dataframe(
#     metrics: List[str],
#     selected_protocol,
#     filtered_protocols,
#     results,
#     results_correspondences,
# ):
#     protocols_key = f"{selected_protocol} Protocols"
#
#     data = {"Metric": [], "Error Rate (%)": [], protocols_key: []}
#
#     for protocol in filtered_protocols:
#         try:
#             subprotocol = (
#                 protocol.replace(f"{selected_protocol}", "")
#                 .replace("-", "")
#                 .replace(" ", "")
#             )
#             if subprotocol == "ALL":
#                 continue
#             performance_info = results[results_correspondences[protocol]]
#             acer_info = performance_info["acer_info"]
#             for metric in metrics:
#                 data["Metric"].append(metric)
#                 if metric == "BPCER":
#                     metric_value = (
#                         performance_info.get("acer_info", {})
#                         .get("aggregate", {})
#                         .get("bpcer")
#                     )
#                 elif metric == "APCER":
#                     max_apcer_pai = (
#                         performance_info.get("acer_info", {})
#                         .get("aggregate", {})
#                         .get("max_apcer_pai")
#                     )
#                     metric_value = (
#                         performance_info.get("acer_info", {})
#                         .get("aggregate", {})
#                         .get("apcer_per_pai", {})
#                         .get(max_apcer_pai)
#                     )
#                 elif metric == "SAPCER":
#                     max_apcer_pai = (
#                         performance_info.get("acer_info", {})
#                         .get("specific", {})
#                         .get("max_apcer_pai")
#                     )
#                     metric_value = (
#                         performance_info.get("acer_info", {})
#                         .get("specific", {})
#                         .get("apcer_per_pai", {})
#                         .get(max_apcer_pai)
#                     )
#                 else:
#                     metric_value = performance_info.get(metric.lower())
#                 data["Error Rate (%)"].append(metric_value)
#                 data[protocols_key].append(subprotocol)
#         except:
#             pass
#
#     df_metrics = pd.DataFrame(data, columns=data.keys())
#     return df_metrics
