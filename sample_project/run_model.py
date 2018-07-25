# imports
import pandas as pd
from collections import OrderedDict

# Sampling
from sklearn.model_selection import train_test_split

# Classifiier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

# Metrics
from sklearn.metrics import accuracy_score

# Visualisation
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(color_codes=True)
pal = sns.color_palette("Set2", 10)
sns.set_palette(pal)

# Read in clean data
data = pd.read_csv('titanic_clean.csv')

data_y = data.survived
data_x = data.drop(['survived', 'name', 'ticket', 'boat', 'body', 'home.dest'], axis=1)

# Create training and test sets
X_train, X_test, y_train, y_test = train_test_split(data_x, data_y, test_size=0.2, random_state=0)


# Random Forest Classifier ---
model = RandomForestClassifier(n_estimators = 100)

# Fit to the training data
model.fit(X_train, y_train)

# Predict on the test data: y_pred
y_pred = model.predict(X_test)

# Score / Metrics
accuracy = model.score(X_test, y_test) # = accuracy
print('Random Forest',accuracy)


# Features importance
def FeaturesImportance(data, model):
    features = data.columns.tolist()
    fi = model.feature_importances_

    sorted_features = {}
    for feature, imp in zip(features, fi):
        sorted_features[feature] = round(imp, 3)

    # sort the dictionnary by value
    sorted_features = OrderedDict(sorted(sorted_features.items(), reverse=True, key=lambda t: t[1]))

    for feature, imp in sorted_features.items():
        print(feature+" : ",imp)

    dfvi = pd.DataFrame(list(sorted_features.items()), columns=['Features', 'Importance'])
    # dfvi.head()
    plt.figure(figsize=(15, 5))
    sns.barplot(x='Features', y='Importance', data=dfvi);
    plt.xticks(rotation=90)
    plt.show()


# Features importance
FeaturesImportance(data, model)