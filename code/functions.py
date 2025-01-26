# <TODO>: Add Docs

import io
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def standardize_datetime(df: pd.DataFrame, col_name: str, format: str):
    return pd.to_datetime(df[col_name], format=format, errors="coerce")


def get_null_counts(df: pd.DataFrame):
    return pd.DataFrame(
        {
            "column": df.columns,
            "null_count": df.isnull().sum(),
            "non_null_count": df.notnull().sum(),
        }
    ).reset_index(drop=True)


def plot_null_percentages(df: pd.DataFrame):
    # Calculate percentages
    df_sorted = df.sort_values("null_count", ascending=False)
    total = df_sorted["null_count"] + df_sorted["non_null_count"]
    df_sorted["null_pct"] = (df_sorted["null_count"] / total * 100).round(1)
    df_sorted["non_null_pct"] = (df_sorted["non_null_count"] / total * 100).round(1)

    plt.figure(figsize=(12, 6))

    sns.barplot(x="column", y="null_pct", data=df_sorted, color="red", label="Null %")
    sns.barplot(
        x="column",
        y="non_null_pct",
        data=df_sorted,
        color="green",
        label="Non-Null %",
        bottom=df_sorted["null_pct"],
    )

    # Add percentage labels
    for i, pct in enumerate(df_sorted["null_pct"]):
        plt.text(i, 50, f"{pct}%", ha="center", va="center")

    plt.xticks(rotation=45, ha="right")
    plt.xlabel("Column Names")
    plt.ylabel("Percentage (%)")
    plt.ylim(0, 100)
    plt.legend()
    plt.tight_layout()
    return plt
