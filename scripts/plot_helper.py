import matplotlib.pyplot as plt
import numpy as np

def plot_bar(data_dict):
    n_entities = data_dict.keys()
    scores = data_dict.values()
    colors = ['lightsteelblue', 'steelblue', 'yellowgreen']
    
    plt.figure(figsize=(11,7))
    
    r = np.arange(len(n_entities))
    width = 0.25
    
    precision = [score[0] for score in scores]
    bar1 = plt.bar(r, precision, width, color=colors[0], edgecolor='black')
    x_bar1 = r-0.1
    for index, value in enumerate(precision):
        plt.text(x_bar1[index], value+0.01, "{0:.3f}".format(value))
    
    recall = [score[1] for score in scores]
    bar2 = plt.bar(r+width, recall, width, color=colors[1], edgecolor='black')
    x_bar2 = r+width-0.1
    for index, value in enumerate(recall):
        plt.text(x_bar2[index], value+0.01, "{0:.3f}".format(value))
    
    f1 = [score[2] for score in scores]
    bar3 = plt.bar(r+width*2, f1, width, color=colors[2], edgecolor='black')
    x_bar3 = r+width*2-0.1
    for index, value in enumerate(f1):
        plt.text(x_bar3[index], value+0.01, "{0:.3f}".format(value))
    
    plt.title("Results")
    plt.xlabel("Entity Type")
    plt.ylim(0.0,1.0)
    plt.xticks(r+width, n_entities)
    plt.legend((bar1, bar2, bar3), ('Precision', 'Recall', 'F1 Score'))
    plt.show()
