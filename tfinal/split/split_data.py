from sklearn.model_selection import train_test_split

import pandas as pd

def main():
    df = pd.read_csv("data_final.csv")
    df.index.name = 'index'

    train, test = train_test_split(df, test_size=0.2, random_state=42)

    train.to_csv('80.csv')
    test.to_csv('20.csv')

    df_droped = test.drop(columns=['Class'])
    df_droped.to_csv('20_without_label.csv')


if __name__ == "__main__":
    main()