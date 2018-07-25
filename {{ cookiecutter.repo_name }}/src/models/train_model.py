import os
import pandas as pd
from pathlib import Path
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

ROOT = Path(__file__).resolve().parents[2]


def fetch_processed(data_path):
    data = pd.read_csv(os.path.join(ROOT, data_path))
    data_y = data.survived
    data_x = data.drop(['survived', 'name', 'ticket', 'boat', 'body', 'home.dest'], axis=1)
    return data_y, data_x


def fit_and_pickle(ys, xs):
    # Create training and test sets
    X_train, X_test, y_train, y_test = train_test_split(xs, ys, test_size=0.2, random_state=0)
    model = RandomForestClassifier(n_estimators=100)

    # Fit to the training data
    model.fit(X_train, y_train)

    # Please pickle the model


def main():
    ys, xs = fetch_processed('data/processed/titanic.csv')
    fit_and_pickle(ys, xs)


if __name__ == '__main__':
    main()