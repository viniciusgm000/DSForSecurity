from sklearn.metrics import confusion_matrix, classification_report

from sklearn.preprocessing import LabelBinarizer, StandardScaler

from joblib import load
import sys

import pandas as pd

def main(data_file, data_file_with_labels, classifier_file):
    scaler = StandardScaler()

    df = pd.read_csv(data_file)
    df.drop(columns=['index'], inplace=True)
    df_scaled = scaler.fit(df).transform(df)

    df_target = pd.read_csv(data_file_with_labels)
    df_target.drop(columns=['index'], inplace=True)

    classifier = load(classifier_file)
    predicted = classifier.predict(df_scaled)

    lb = LabelBinarizer()
    df_target['Class'] = lb.fit_transform(df_target['Class'].values)
    # Malicious -> 1 - Benign -> 0
    target = df_target['Class'].values

    print(pd.DataFrame(confusion_matrix(target, predicted), columns=['pred_neg', 'pred_pos'], index=['neg', 'pos']))
    print(classification_report(target, predicted, labels=[0, 1]))

if __name__ == "__main__":
    if (len(sys.argv) != 4):
        print("Error - Correct usage:")
        print(str(sys.argv[0]), " <FILE_TO_PREDICT> <FILE_TO_PREDICT_WITH_LABELS> <MODEL>")
        sys.exit()
    main(str(sys.argv[1]), str(sys.argv[2]), str(sys.argv[3]))