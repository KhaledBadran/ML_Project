import matplotlib.pyplot as plt
import numpy as np


def plot_bar(data_dict):
    n_entities = data_dict.keys()
    scores = data_dict.values()
    colors = ["navy", "tan", "salmon"]

    r = np.arange(len(n_entities))
    width = 0.25

    precision = [score[0] for score in scores]
    bar1 = plt.bar(r, precision, width, color=colors[0])

    recall = [score[1] for score in scores]
    bar2 = plt.bar(r + width, recall, width, color=colors[1])

    f1 = [score[2] for score in scores]
    bar3 = plt.bar(r + width * 2, f1, width, color=colors[2])

    plt.xlabel("Entity Type")
    plt.title("Results")

    plt.xticks(r + width, n_entities)
    plt.legend((bar1, bar2, bar3), ("Precision", "Recall", "F1"))
    plt.show()
