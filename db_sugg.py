#pip install scikit-learn==1.0.2
#pip install matplotlib

import pandas as pd
import numpy as np
from sklearn import tree, metrics
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
from scipy.io import arff


data,meta = arff.loadarff('./database_suggestions.arff')

attributes = meta.names()
data_value = np.asarray(data)

frequency = np.asarray(data['frequency']).reshape(-1,1)
volume = np.asarray(data['volume']).reshape(-1,1)
throughput = np.asarray(data['throughput']).reshape(-1,1)
price = np.asarray(data['price']).reshape(-1,1)

feat_labels = ['frequency', 'volume', 'throughput', 'price', 'suggestion']
class_labels = ['SQLite', 'Apache_Arrow', 'Amazon_Aurora', 'Redis', 'CockroachDB', 'Google_Cloud_Spanner', 'InfluxDB']

features = np.concatenate((frequency , volume, throughput, price),axis=1)


target = data['suggestion']

Arvore = DecisionTreeClassifier(criterion='entropy').fit(features, target)

plt.figure(figsize=(10, 6.5))
tree.plot_tree(Arvore,feature_names=feat_labels,class_names=class_labels,
                   filled=True, rounded=True)
plt.savefig('dbs_tree.png')


fig, ax = plt.subplots(figsize=(25, 10))
metrics.plot_confusion_matrix(Arvore,features,target,display_labels=class_labels, values_format='f', ax=ax)
plt.savefig('dbs_matrix.png')
