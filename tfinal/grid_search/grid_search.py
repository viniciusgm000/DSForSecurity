from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier

from sklearn.preprocessing import LabelBinarizer, StandardScaler
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import make_scorer, recall_score, accuracy_score, precision_score, confusion_matrix

import pandas as pd

def search(name, data, target, classifier, parameters, scorers, score_to_refit):
    print('=====================> ' + name)
    print('----- Parameters: ' + str(parameters))
    out_classifier = GridSearchCV(estimator=classifier, param_grid=parameters, scoring=scorers, refit=score_to_refit, cv=None, return_train_score=True, n_jobs=-1)
    
    scaler = StandardScaler()
    data_scaled = scaler.fit(data).transform(data)
    out_classifier.fit(data_scaled, target)

    predicted = out_classifier.predict(data_scaled)

    # print('----- Best: ', out_classifier.best_estimator_)
    print('----- Best parameters: ', out_classifier.best_params_)
    print('----- Best score: ', out_classifier.best_score_)
    print('----- Confusion Matrix: (pos -> Malicious, neg -> Benign)')

    print(pd.DataFrame(confusion_matrix(target, predicted), columns=['pred_neg', 'pred_pos'], index=['neg', 'pos']))

    print('\n')

def main():
    df = pd.read_csv("80.csv")

    lb = LabelBinarizer()
    df['Class'] = lb.fit_transform(df['Class'].values)
    # Malicious -> 1 - Benign -> 0
    labels = df['Class'].values
    df.drop(columns=['index'], inplace=True)
    df_droped = df.drop(columns=['Class']).values

    param_knn = {
        'n_neighbors': [1, 3, 5],
        'algorithm': ['brute']
    }

    param_rf = {
        'n_estimators': [50, 100],
        'random_state': [42]
    }

    param_svc = {
        'max_iter': [1000, 5000],
        'random_state': [42],
        'tol': [0.01]
    }

    param_mlp = {
        'max_iter': [1000, 5000],
        'random_state': [42],
        'learning_rate': ['adaptive'],
        'tol': [0.01]
    }

    scorers = {
        'precision_score': make_scorer(precision_score),
        'recall_score': make_scorer(recall_score),
        'accuracy_score': make_scorer(accuracy_score)
    }

    score_to_refit = 'precision_score'

    print('\n')

    search('KNeighborsClassifier', df_droped, labels, KNeighborsClassifier(), param_knn, scorers, score_to_refit)
    search('RandomForestClassifier', df_droped, labels, RandomForestClassifier(), param_rf, scorers, score_to_refit)
    search('SVC', df_droped, labels, SVC(), param_svc, scorers, score_to_refit)
    search('MLPClassifier', df_droped, labels, MLPClassifier(), param_mlp, scorers, score_to_refit)

if __name__ == "__main__":
    main()
