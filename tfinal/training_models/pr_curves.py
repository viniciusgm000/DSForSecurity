from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier

from sklearn.model_selection import StratifiedKFold
from sklearn.preprocessing import LabelBinarizer, StandardScaler
from sklearn.metrics import precision_recall_curve

import pandas as pd

import matplotlib.pyplot as plt

def run_classifier(name, X, Y, classifier):
    skf = StratifiedKFold(n_splits=5, random_state=42, shuffle=True)
    skf.get_n_splits(X, Y)

    plt.cla()

    plt.figure(figsize=(12, 8))
    plt.title("Precision X Recall por limiar para k-fold de 5")
    colors = ['b', 'g', 'r', 'c', 'y']

    index = 0

    for train_index, test_index in skf.split(X, Y):
        X_train, X_test = X[train_index], X[test_index]
        Y_train, Y_test = Y[train_index], Y[test_index]

        classifier.fit(X_train, Y_train)
        y_scores = classifier.predict_proba(X_test)[:, 1]
        p, r, t = precision_recall_curve(Y_test, y_scores)

        plt.plot(t, p[:-1], colors[index] + "--", label="{} - Precision".format(index + 1))
        plt.plot(t, r[:-1], colors[index] + "-", label="{} - Recall".format(index + 1))
        index = index + 1

    plt.ylabel("Pontuação")
    plt.xlabel("Limiar de decisão")
    plt.legend(loc='best')
    plt.savefig("pr_figures/" + name + ".png")

def main():
    df = pd.read_csv("80.csv")

    lb = LabelBinarizer()
    df['Class'] = lb.fit_transform(df['Class'].values)
    # Malicious -> 1 - Benign -> 0
    labels = df['Class'].values
    df.drop(columns=['index'], inplace=True)
    df_droped = df.drop(columns=['Class'])

    scaler = StandardScaler()
    df_scaled = scaler.fit(df_droped).transform(df_droped)

    run_classifier("KNeighborsClassifier", df_scaled, labels, KNeighborsClassifier(algorithm='brute', n_neighbors=5))
    run_classifier("RandomForestClassifier", df_scaled, labels, RandomForestClassifier(n_estimators=100, random_state=42))
    run_classifier("SVC", df_scaled, labels, SVC(max_iter=1000, random_state=42, tol=0.01, probability=True))
    run_classifier("MLPClassifier", df_scaled, labels, MLPClassifier(learning_rate='adaptive', max_iter=1000, random_state=42, tol=0.01))

if __name__ == "__main__":
    main()
