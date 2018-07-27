import os
import pickle
import pandas as pd
from pathlib import Path
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

ROOT = Path(__file__).resolve().parents[2]

if '{{ cookiecutter.python_interpreter }}' == 'python3':
    PROTOCOL = pickle.DEFAULT_PROTOCOL
else:
    PROTOCOL = 2


def fetch_processed(data_path):
    data = pd.read_csv(os.path.join(ROOT, data_path))
    data_y = data.survived
    data_x = data.drop(['survived', 'name', 'ticket', 'boat', 
        'body', 'home.dest'], axis=1)
    # Create training and test sets
    X_train, X_test, y_train, y_test = train_test_split(data_x, data_y, 
        test_size=0.2, random_state=0)
    return X_train, X_test, y_train, y_test


def fit_model(X_train, y_train):
    model = RandomForestClassifier(n_estimators=100)
    # Fit to the training data
    model.fit(X_train, y_train)
    return model


def main():
    x_train, x_test, y_train, y_test = fetch_processed('data/processed/titanic.csv')
    # Train the model 
    model = fit_model(x_train, y_train)

    # Paths for storage
    model_out_dir = os.path.join(ROOT, 'models/titanic.model')
    x_test_path = os.path.join(ROOT, 'data/processed/titanic_x_test.csv')
    y_test_path = os.path.join(ROOT, 'data/processed/titanic_y_test.csv')
    
    # Store model and test set for prediction
    with open(model_out_dir, 'wb') as fout:
        pickle.dump(model, fout, PROTOCOL)
    x_test.to_csv(x_test_path, index=False)
    y_test.to_csv(y_test_path, index=False)


if __name__ == '__main__':
    main()
