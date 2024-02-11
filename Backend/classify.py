import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import classification_report, f1_score
from cleanup import cleanup


def train():
    df = pd.read_csv('../mental-heath-in-tech-2016_20161114.csv')
    df = cleanup(df)

    y = df['Label']
    X = df.drop(['Label'], axis=1)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=22)
    clf = RandomForestClassifier()
    print(cross_val_score(clf, X, y, cv=3))

    clf = RandomForestClassifier()
    clf.fit(X_train, y_train)
    print(classification_report(y_test, clf.predict(X_test)))

    clf_full = RandomForestClassifier()
    clf_full.fit(X, y)
    return clf_full


def predict(x_input, model):
    mappings = {
        -1: "None",
        1: "Anxiety",
        2: "Mood"
    }
    return mappings[model.predict(x_input)]
