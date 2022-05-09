from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier

from sklearn.model_selection import StratifiedKFold
from sklearn.preprocessing import LabelBinarizer, StandardScaler
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

import pandas as pd

import matplotlib.pyplot as plt

import numpy as np

def run_classifier(name, X, Y, classifier):
    skf = StratifiedKFold(n_splits=5, random_state=42, shuffle=True)
    skf.get_n_splits(X, Y)

    index = 1

    plt.figure(figsize=(12, 8))

    for train_index, test_index in skf.split(X, Y):
        X_train, X_test = X[train_index], X[test_index]
        Y_train, Y_test = Y[train_index], Y[test_index]

        classifier.fit(X_train, Y_train)
        predicted = classifier.predict(X_test)

        cm = confusion_matrix(Y_test, predicted)

        plt.cla()

        cmd = ConfusionMatrixDisplay(cm, display_labels=['Benign','Malicious'])
        cmd.plot(cmap='magma')
        cmd.ax_.set_title("Confusion Matrix - " + name + " k-fold #" + str(index))
        plt.savefig("cm_figures/" + name + "-{}".format(index) + ".png")
        plt.close()

        index = index + 1


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
