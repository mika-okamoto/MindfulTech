import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import classification_report, f1_score
from cleanup import cleanup
import numpy as np


def train():
    df = pd.read_csv('../mental-heath-in-tech-2016_20161114.csv')
    df = cleanup(df)

    y = df['Label']
    X = df.drop(['Label'], axis=1)
    # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=22)
    # clf = RandomForestClassifier(min_samples_leaf=4, n_estimators=800)
    # print(cross_val_score(clf, X, y, cv=3))

    # clf = RandomForestClassifier(min_samples_leaf=4, n_estimators=800)
    # clf.fit(X_train, y_train)
    # print(classification_report(y_test, clf.predict(X_test)))

    clf_full = RandomForestClassifier(min_samples_leaf=4, n_estimators=800)
    clf_full.fit(X, y)
    return clf_full


def predict(x_input, model):
    x_input.pop(4)
    x_input = np.array(x_input)
    x_input = x_input.reshape(1, -1)
    print(x_input)
    mappings = {
        0: "None",
        1: "Anxiety",
        2: "Mood"
    }
    return mappings[model.predict(x_input)[0]]
