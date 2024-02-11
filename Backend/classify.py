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


def format(content):
    genders = {
        'male': 0,
        'female': 2,
        'other': 1
    }
    emp_count = {
        '1-5': 0,
        '6-25': 1,
        '26-100': 2,
        '100-500': 3,
        '501-1000': 4,
        '1000+': 5
    }

    remote_work = {
        'always': 1,
        'sometimes': 0.5,
        'never': 0
    }

    disorder = {
        'mood disorder': 2,
        'anxiety': 1,
        'no': -1,
        '': -1
    }

    family = {
        'yes': 1,
        'no': 0,
        "i don't know": 0.5,
        "maybe": 0.5,
        '': 0
    }

    num_10 = {
        'strong no': 1,
        'little no': 2,
        'maybe': 3,
        'little yes': 4,
        'strong yes': 5
    }

    sharing = {
        "n/a": 0,
        "not open at all": 1,
        "somewhat not open": 2,
        "neutral": 3,
        "somewhat open": 4,
        "very open": 5
    }

    productivity = {
        "n/a": -1,
        'never': 0,
        'rarely': 1,
        'sometimes': 2,
        'often': 3
    }

    formatted = [int(content.get('1')), genders[content.get('2')], emp_count[content.get('3')],
                 remote_work[content.get('4')],
                 disorder[content.get('5')], family[content.get('6')],
                 family[content.get('7')], family[content.get('8')], family[content.get('9')],
                 num_10[content.get('10')],
                 sharing[content.get('11')], productivity[content.get('12')]]

    survey = f"Age: {content.get('1')}\nGender: {content.get('2')}\nNumber of Employees at Company: {content.get('3')}\n" + \
             f"Does remote work: {content.get('4')}\nFamily history of mental disorders: {content.get('6')}\n" + \
             f"Does your employer offer resources to learn more about mental health concerns and options for seeking help?: {content.get('7')}\n" + \
             f"Do you think that discussing a mental health disorder with your employer would have negative consequences?: {content.get('8')}\n" + \
             f"Would you feel comfortable discussing a mental health disorder with your fellow employees?: {content.get('9')}\n" + \
             f"Do you feel that being identified as a person with a mental health issue would hurt your career?: {content.get('10')}\n" + \
             f"How willing would you be to share with friends and family that you have a mental illness?: {content.get('11')}\n" + \
             f"Do you believe your productivity/work is ever affected by a mental health issue?: {content.get('12')}"

    return survey, formatted
