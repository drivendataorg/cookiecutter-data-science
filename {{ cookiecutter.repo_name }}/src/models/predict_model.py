import os
import pickle
from train_model import ROOT, fetch_processed


def main():
    _, X_test, *_ = fetch_processed('data/processed/titanic.csv')
    pickled_model = os.path.join(ROOT, 'models/titanic.model')
    with open(pickled_model, 'rb') as fin:
        deserialized_model = pickle.load(fin)
    y_pred = deserialized_model.predict(X_test)
    print(f'The model returned these predictions:\n{y_pred}')


if __name__ == '__main__':
    main()