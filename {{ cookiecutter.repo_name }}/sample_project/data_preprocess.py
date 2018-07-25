import pandas as pd
from sklearn.preprocessing import StandardScaler

# Read in data (from http://biostat.mc.vanderbilt.edu/wiki/Main/DataSets)
urllink = 'http://biostat.mc.vanderbilt.edu/wiki/pub/Main/DataSets/titanic3.csv'
data = pd.read_csv(urllink)

# which columns have NaN
print(pd.isnull(data).sum() > 0)

# Feature engineering ---
title = ['Mlle', 'Mrs', 'Mr', 'Miss', 'Master', 'Don', 'Rev', 'Dr', 'Mme', 'Ms', 'Major', 'Col', 'Capt', 'Countess']

def ExtractTitle(name):
    tit = 'missing'
    for item in title:
        if item in name:
            tit = item
    if tit == 'missing':
        tit = 'Mr'
    return tit


data["title"] = data.apply(lambda row: ExtractTitle(row["name"]), axis=1)

# Impute missing value ---

# Age: replace NaN with median
data["age"].fillna(data.age.median(), inplace=True)

# Embarked: replace NaN with the mode value
data["embarked"].fillna(data.embarked.mode()[0], inplace=True)

# Fare: replace NaN with median
data["fare"].fillna(data.fare.median(), inplace=True)

# Encode Categorical features ---

data["cabin"] = data.apply(lambda obs: "No" if pd.isnull(obs['cabin']) else "Yes", axis=1)  # binarize “cabin” feature

data = pd.get_dummies(data, columns=['sex', 'title', 'cabin', 'embarked'])

# Scaling numerical features ---
scale = StandardScaler().fit(data[['age', 'fare']])
data[['age', 'fare']] = scale.transform(data[['age', 'fare']])

# Save dataset ---
data.to_csv('titanic_clean.csv', index=False)
