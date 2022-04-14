#!/usr/bin/python
# -*- encoding: iso-8859-1 -*-

# KNN classifier

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.preprocessing import normalize

import pandas as pd
import numpy
import sys

numpy.set_printoptions(threshold=sys.maxsize)

# carrega dado
df = pd.read_csv("data_final.csv")
df_droped = df.drop(columns=['Class'])
values = df_droped.values

# salva os labels originais e converte utilizando uma enumeracao
labels = df['Class'].values
d = dict([(y,x) for x,y in enumerate(sorted(set(labels)))])
# benign 0 - malicious 1
Y = [d[x] for x in labels]

# realiza uma normalizacao quadratica: https://stats.stackexchange.com/questions/225564/scikit-learn-normalization-mode-l1-vs-l2-max
normalized_data = normalize(values, norm='l2')
X = pd.DataFrame(normalized_data)

# divide em treino e teste com uma seed fixa e 20% para teste
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42, stratify=Y)

# cria o classificador
knn = RandomForestClassifier(n_jobs = -1)
knn.fit(X_train, Y_train)

# classifica
Y_pred = knn.predict(X_test)

# acurácia
print("\nBenign 0 - Malicious 1")
print('Acuracia: ', knn.score(X_test, Y_test))
print(confusion_matrix(Y_test, Y_pred))
print(classification_report(Y_test, Y_pred, labels=[0, 1]))
# print(Y_test[20:50])
# print(Y_pred[20:50])