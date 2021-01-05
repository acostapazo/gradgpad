import seaborn as sns
from pandas import DataFrame


def create_metric_bar_chart_comparison(
    df: DataFrame, output_filename: str, max_y_limit: int = None
):
    metric = df.columns[1]
    if max_y_limit:
        max_y_limit = df.max()[metric]
    sns.set(style="whitegrid")
    sns.set_context(
        "paper", rc={"font.size": 14, "axes.titlesize": 32, "axes.labelsize": 18}
    )
    g = sns.catplot(
        x="",
        y=metric,
        hue="Approach",
        data=df,
        kind="bar",
        height=5,
        aspect=1,
        palette=["skyblue", "sandybrown", "green"],
    )
    g.set(ylim=(0, max_y_limit))
    g.savefig(output_filename)
