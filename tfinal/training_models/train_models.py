from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelBinarizer, StandardScaler
# from sklearn.metrics import make_scorer, recall_score, accuracy_score, precision_score, confusion_matrix

from joblib import dump

import time

import pandas as pd

def run_classifier(name, X_train, X_test, Y_train, Y_test, classifier):
    start = time.time()
    classifier.fit(X_train, Y_train)
    end = time.time()

    dump(classifier, 'models/' + name + '.joblib')

    print('=====================> ' + name)
    print('Training time: ' + str(end - start) + 's')

    

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

    print('\n')

    X_train, X_test, Y_train, Y_test = train_test_split(df_scaled, labels, test_size=0.5, random_state=42)

    run_classifier("KNeighborsClassifier_50-50", X_train, X_test, Y_train, Y_test, KNeighborsClassifier(algorithm='brute', n_neighbors=5))
    run_classifier("RandomForestClassifier_50-50", X_train, X_test, Y_train, Y_test, RandomForestClassifier(n_estimators=100, random_state=42))
    run_classifier("SVC_50-50", X_train, X_test, Y_train, Y_test, SVC(max_iter=1000, random_state=42, tol=0.01))
    run_classifier("MLPClassifier_50-50", X_train, X_test, Y_train, Y_test, MLPClassifier(learning_rate='adaptive', max_iter=1000, random_state=42, tol=0.01))

    X_train, X_test, Y_train, Y_test = train_test_split(df_scaled, labels, test_size=0.2, random_state=42)

    run_classifier("KNeighborsClassifier_80-20", X_train, X_test, Y_train, Y_test, KNeighborsClassifier(algorithm='brute', n_neighbors=5))
    run_classifier("RandomForestClassifier_80-20", X_train, X_test, Y_train, Y_test, RandomForestClassifier(n_estimators=100, random_state=42))
    run_classifier("SVC_80-20", X_train, X_test, Y_train, Y_test, SVC(max_iter=1000, random_state=42, tol=0.01))
    run_classifier("MLPClassifier_80-20", X_train, X_test, Y_train, Y_test, MLPClassifier(learning_rate='adaptive', max_iter=1000, random_state=42, tol=0.01))

    print('\n')

if __name__ == "__main__":
    main()
