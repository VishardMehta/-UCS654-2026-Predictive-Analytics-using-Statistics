import pandas as pd
import numpy as np

def validate(df, weights, impacts):
    if df.shape[1] < 3:
        raise ValueError("Input file must contain three or more columns")

    data = df.iloc[:, 1:]

    for col in data.columns:
        if not pd.api.types.is_numeric_dtype(data[col]):
            raise ValueError("From 2nd to last columns must contain numeric values only")

    if len(weights) != data.shape[1]:
        raise ValueError("Number of weights must match number of criteria")

    if len(impacts) != data.shape[1]:
        raise ValueError("Number of impacts must match number of criteria")

    for i in impacts:
        if i not in ["+", "-"]:
            raise ValueError("Impacts must be either + or -")

def topsis(input_file, weights, impacts, output_file):
    if input_file.endswith(".csv"):
        df = pd.read_csv(input_file)
    elif input_file.endswith(".xlsx") or input_file.endswith(".xls"):
        df = pd.read_excel(input_file)
    else:
        raise ValueError("Unsupported file format")

    weights = [float(w) for w in weights.split(",")]
    impacts = impacts.split(",")

    validate(df, weights, impacts)

    data = df.iloc[:, 1:].astype(float).values
    weights = np.array(weights)

    norm = data / np.sqrt((data ** 2).sum(axis=0))
    weighted = norm * weights

    ideal_best = np.array([
        weighted[:, i].max() if impacts[i] == "+" else weighted[:, i].min()
        for i in range(weighted.shape[1])
    ])

    ideal_worst = np.array([
        weighted[:, i].min() if impacts[i] == "+" else weighted[:, i].max()
        for i in range(weighted.shape[1])
    ])

    dist_best = np.sqrt(((weighted - ideal_best) ** 2).sum(axis=1))
    dist_worst = np.sqrt(((weighted - ideal_worst) ** 2).sum(axis=1))

    score = dist_worst / (dist_best + dist_worst)
    rank = score.argsort()[::-1].argsort() + 1

    result = df.copy()
    result["Topsis Score"] = score
    result["Rank"] = rank

    result.to_csv(output_file, index=False)
