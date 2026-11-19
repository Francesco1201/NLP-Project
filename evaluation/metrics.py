# Summary tables of the scores. ScoreData loads the scores exported from the evaluation workbooks. 
# fullTable builds the table of all criteria, grouped by model or by game category. fullLatex and ReportWriter save it as CSV and LaTeX.

import copy
import os
import pandas as pd

modelOrder = ["Qwen", "Llama-1B", "Mistral-7B", "Qwen-7B"]
modelLabels = {"Qwen": "Qwen2.5-0.5B", "Llama-1B": "Llama-3.2-1B", "Mistral-7B": "Mistral-7B", "Qwen-7B": "Qwen2.5-7B"}
shortLabels = {"Qwen": "Qwen 0.5B", "Llama-1B": "Llama 1B", "Mistral-7B": "Mistral 7B", "Qwen-7B": "Qwen 7B"}
categoryOrder = ["Abstract deterministic", "Low-interaction procedural", "Exception-heavy rule systems",
                 "Thematic with randomness", "Social/party"]
categoryLabels = {"Abstract deterministic": "Abstract", "Low-interaction procedural": "Procedural",
                  "Exception-heavy rule systems": "Exception-heavy", "Thematic with randomness": "Thematic",
                  "Social/party": "Social/party"}
groupings = {"model": (modelOrder, shortLabels), "category": (categoryOrder, categoryLabels)}


# Scores of all tasks, one DataFrame per CSV file in the scores folder.
class ScoreData:

    def __init__(self, scoresDir):
        self.explain = pd.read_csv(os.path.join(scoresDir, "explain.csv"))
        self.flawOutputs = pd.read_csv(os.path.join(scoresDir, "flaw_outputs.csv"))
        self.flawItems = pd.read_csv(os.path.join(scoresDir, "flaw_items.csv"))
        self.simulation = pd.read_csv(os.path.join(scoresDir, "simulation.csv"))
        self.generation = pd.read_csv(os.path.join(scoresDir, "generation.csv"))
        self.variant = pd.read_csv(os.path.join(scoresDir, "variant.csv"))

    # Copy of the data restricted to one model.
    def forModel(self, model):
        subset = copy.copy(self)
        for name in ["explain", "flawOutputs", "flawItems", "simulation", "generation", "variant"]:
            frame = getattr(self, name)
            setattr(subset, name, frame[frame["model"] == model])
        return subset
        
    # Number of scored answers or flaws per model, to check that the data are complete.    
    def counts(self):
        frames = {"explain": self.explain, "flawOutputs": self.flawOutputs, "flawItems": self.flawItems,
                  "simulation": self.simulation, "generation": self.generation, "variant": self.variant}
        return pd.DataFrame({name: frame.groupby("model").size() for name, frame in frames.items()}).reindex(modelOrder)

# Mean of a criterion per group, for 1-5 criteria and counts.
def meanRow(frame, column, key, order):
    return frame.groupby(key)[column].mean().reindex(order).map(lambda v: "--" if pd.isna(v) else f"{v:.2f}")

# Share of true values per group, as a percentage (recall, fixes).
def shareRow(values, groups, order):
    return values.groupby(groups).mean().reindex(order).map(lambda v: "--" if pd.isna(v) else f"{v:.0%}")

# Percentage of answers with score 2 / 1 / 0 per group, for 0-2 criteria.
def splitRow(frame, column, key, order):
    shares = frame.groupby(key)[column].value_counts(normalize=True).unstack(fill_value=0)
    shares = shares.reindex(index=order, columns=[2, 1, 0], fill_value=0)
    return shares.apply(lambda row: " / ".join(f"{v * 100:.0f}" for v in row), axis=1)

# Table of all criteria of all tasks; columns are models (key="model") or categories (key="category").
def fullTable(data, key="model"):
    order, labels = groupings[key]
    detected = data.flawItems[data.flawItems["detected"] == 1]

    def mean(frame, column):
        return meanRow(frame, column, key, order)

    def share(frame, values):
        return shareRow(values, frame[key], order)

    def split(frame, column):
        return splitRow(frame, column, key, order)

    rows = {
        ("Explain", "Task understanding (1-5)"): mean(data.explain, "taskUnderstanding"),
        ("Explain", "Coverage (1-5)"): mean(data.explain, "coverage"),
        ("Explain", "Consistency (1-5)"): mean(data.explain, "consistency"),
        ("Explain", "Hallucination (1-5)"): mean(data.explain, "hallucination"),
        ("Flaw Detection", "Task understanding (1-5)"): mean(data.flawOutputs, "taskUnderstanding"),
        ("Flaw Detection", "Recall"): share(data.flawItems, data.flawItems["detected"]),
        **{("Flaw Detection", f"Recall: {flawType}"): share(items, items["detected"])
           for flawType, items in [(t, data.flawItems[data.flawItems["flawType"] == t])
                                   for t in ["missing", "ambiguous", "inconsistent"]]},
        ("Flaw Detection", "Type correct (of detected)"): share(detected, detected["typeCorrect"]),
        ("Flaw Detection", "Exact fix (of detected)"): share(detected, detected["fixQuality"] == 2),
        ("Flaw Detection", "Partial or exact fix (of detected)"): share(detected, detected["fixQuality"] >= 1),
        ("Flaw Detection", "Invented problems per answer"): mean(data.flawOutputs, "inventedProblems"),
        ("Simulation", "Task understanding (1-5)"): mean(data.simulation, "taskUnderstanding"),
        ("Simulation", "Move correctness: 2 / 1 / 0 (%)"): split(data.simulation, "moveCorrectness"),
        ("Simulation", "Consistency (1-5)"): mean(data.simulation, "consistency"),
        ("Simulation", "Hallucination (1-5)"): mean(data.simulation, "hallucination"),
        ("Generation of a New Game", "Task understanding (1-5)"): mean(data.generation, "taskUnderstanding"),
        ("Generation of a New Game", "Constraint adherence (1-5)"): mean(data.generation, "constraintAdherence"),
        ("Generation of a New Game", "Completeness (1-5)"): mean(data.generation, "completeness"),
        ("Generation of a New Game", "Playability (1-5)"): mean(data.generation, "playability"),
        ("Generation of a New Game", "Balance: 2 / 1 / 0 (%)"): split(data.generation, "balance"),
        ("Generation of a New Game", "Fun: 2 / 1 / 0 (%)"): split(data.generation, "fun"),
        ("Variant", "Task understanding (1-5)"): mean(data.variant, "taskUnderstanding"),
        ("Variant", "Meaningful variant: 2 / 1 / 0 (%)"): split(data.variant, "meaningfulVariant"),
        ("Variant", "Consistency (1-5)"): mean(data.variant, "consistency"),
        ("Variant", "Hallucination (1-5)"): mean(data.variant, "hallucination"),
        ("Variant", "Balance: 2 / 1 / 0 (%)"): split(data.variant, "balance"),
        ("Variant", "Fun: 2 / 1 / 0 (%)"): split(data.variant, "fun"),
    }
    table = pd.DataFrame(rows).T
    table.index.names = ["task", "criterion"]
    return table.rename(columns=labels)

# Name of a criterion in the LaTeX table (recall by type indented under Recall).
def latexLabel(criterion):
    if criterion.startswith("Recall: "):
        return r"\quad " + criterion[len("Recall: "):].capitalize()
    criterion = criterion.replace(": 2 / 1 / 0 (%)", r" (2/1/0, \%)").replace("(1-5)", "(1--5)")
    return criterion.replace(" (of detected)", "").replace(" per answer", "")

# LaTeX code of a summary table, with one block of rows per task.
def fullLatex(table, caption, label):
    headers = [r"\shortstack[r]{" + column.replace("-", r"-\\").replace("/", r"/\\") + "}" for column in table.columns]
    header = " & ".join([r"\textbf{Criterion}"] + [rf"\textbf{{{column}}}" for column in headers])
    columns = len(table.columns)
    lines = [r"\begin{table}[htbp]", rf"\caption{{{caption}}}\label{{{label}}}%",
             r"\small\setlength{\tabcolsep}{4pt}" if columns <= 4 else r"\footnotesize\setlength{\tabcolsep}{2pt}",
             rf"\begin{{tabular}}{{@{{}}l{'r' * columns}@{{}}}}", r"\toprule", header + r" \\"]
    for task in table.index.get_level_values("task").unique():
        lines += [r"\midrule", rf"\multicolumn{{{columns + 1}}}{{@{{}}l}}{{\textbf{{{task}}}}} \\"]
        for criterion, values in table.loc[task].iterrows():
            cells = [v.replace(" / ", "/").replace("%", r"\%") for v in values]
            lines.append(" & ".join([latexLabel(criterion)] + cells) + r" \\")
    lines += [r"\botrule", r"\end{tabular}", r"\end{table}"]
    return "\n".join(lines) + "\n"

# Saves the tables in the tables folder.
class ReportWriter:

    def __init__(self, tablesDir):
        self.tablesDir = tablesDir
        os.makedirs(tablesDir, exist_ok=True)

    def table(self, table, name):
        table.to_csv(os.path.join(self.tablesDir, f"{name}.csv"))
        return table

    def latex(self, text, name):
        with open(os.path.join(self.tablesDir, f"{name}.tex"), "w") as file:
            file.write(text)
        return text
