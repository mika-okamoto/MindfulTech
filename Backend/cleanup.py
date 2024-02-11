import pandas as pd
import numpy as np


def cleanup(df):
    df = df[df["Are you self-employed?"] != 1]
    df = df[(df['What is your age?'] > 18) & (df['What is your age?'] < 100)]
    df = df[(df["Are you self-employed?"] != 1) & (
        df["Is your primary role within your company related to tech/IT?"].isin(['', 1, np.nan]))]
    replace_dict = {"nonbinary": 1, 'female': 2, 'Female': 2, 'F': 2, 'f': 0, 'M': 0, 'm': 0, 'Male': 0, 'male': 0,
                    "woman": 2, "cis male": 0, "Cis male": 0, "dude": 0}
    df["What is your gender?"] = df["What is your gender?"].replace(replace_dict, regex=True)
    df["What is your gender?"] = df["What is your gender?"].replace(to_replace=r'[^0-2]', value=1, regex=True)
    df.replace('Not eligible for coverage / N/A', np.nan, inplace=True)
    df.replace('Not applicable to me', np.nan, inplace=True)
    df.replace('1-5', 0, inplace=True)
    df.replace('6-25', 1, inplace=True)
    df.replace('26-100', 2, inplace=True)
    df.replace('100-500', 3, inplace=True)
    df.replace('500-1000', 4, inplace=True)
    df.replace('More than 1000', 5, inplace=True)
    df['Do you work remotely?'].replace("Always", 1, inplace=True)
    df['Do you work remotely?'].replace("Sometimes", 0.5, inplace=True)
    df['Do you work remotely?'].replace("Never", 0, inplace=True)

    df.replace("Yes", 1, inplace=True)
    df.replace('No', 0, inplace= True)
    df.replace('Maybe', 0.5, inplace = True)
    df.replace("I don't know", 0.5, inplace = True)
    df.replace("I am not sure", 0.5, inplace = True)

    df.replace("Some did", 0.5, inplace=True)
    df.replace("Some of them", 0.5, inplace=True)
    df.replace("No, none did", 0, inplace=True)
    df.replace("None of them", 0, inplace=True)
    df.replace("None did", 0, inplace=True)
    df.replace("Yes, they all did", 1, inplace=True)
    df.replace("N/A (not currently aware)", np.nan, inplace=True)
    df.replace("I was aware of some", 0.5, inplace=True)
    df.replace("No, I only became aware later", 0, inplace=True)
    df.replace("Yes, I was aware of all of them", 1, inplace=True)
    df.replace("Yes, all of them", 1, inplace=True)
    df.replace("Yes, at all of my previous employers", 1, inplace=True)
    df.replace("No, at none of my previous employers", 0, inplace=True)
    df.replace("Some of my previous employers", 0.5, inplace=True)

    df['Do you feel that being identified as a person with a mental health issue would hurt your career?'].replace(0.5, 3,inplace=True)
    df['Do you feel that being identified as a person with a mental health issue would hurt your career?'].replace(
        "Yes, I think it would", 4, inplace=True)
    df['Do you feel that being identified as a person with a mental health issue would hurt your career?'].replace(
        "Yes, it has", 5, inplace=True)
    df['Do you feel that being identified as a person with a mental health issue would hurt your career?'].replace(
        "No, I don't think it would", 2, inplace=True)
    df['Do you feel that being identified as a person with a mental health issue would hurt your career?'].replace(
        "No, it has not", 1, inplace=True)
    df[
        'Do you think that team members/co-workers would view you more negatively if they knew you suffered from a mental health issue?'].replace(
        0.5, 3, inplace=True)
    df[
        'Do you think that team members/co-workers would view you more negatively if they knew you suffered from a mental health issue?'].replace(
        "Yes, I think they would", 4, inplace=True)
    df[
        'Do you think that team members/co-workers would view you more negatively if they knew you suffered from a mental health issue?'].replace(
        "Yes, they do", 5, inplace=True)
    df[
        'Do you think that team members/co-workers would view you more negatively if they knew you suffered from a mental health issue?'].replace(
        "No, I don't think they would", 2, inplace=True)
    df[
        'Do you think that team members/co-workers would view you more negatively if they knew you suffered from a mental health issue?'].replace(
        "No, they do not", 1, inplace=True)

    df.replace('Rarely', 1, inplace = True)
    df.replace('Never', 0, inplace = True)
    df.replace('Sometimes', 2, inplace = True)
    df.replace('Often', 3, inplace = True)

    df[['Does your employer provide mental health benefits as part of healthcare coverage?',
        'Do you know the options for mental health care available under your employer-provided coverage?',
        'Has your employer ever formally discussed mental health (for example, as part of a wellness campaign or other official communication)?',
        'Does your employer offer resources to learn more about mental health concerns and options for seeking help?',
        'Have your previous employers provided mental health benefits?',
        'Were you aware of the options for mental health care provided by your previous employers?',
        'Did your previous employers ever formally discuss mental health (as part of a wellness campaign or other official communication)?',
        'Did your previous employers provide resources to learn more about mental health issues and how to seek help?']] = df[['Does your employer provide mental health benefits as part of healthcare coverage?',
        'Do you know the options for mental health care available under your employer-provided coverage?',
        'Has your employer ever formally discussed mental health (for example, as part of a wellness campaign or other official communication)?',
        'Does your employer offer resources to learn more about mental health concerns and options for seeking help?',
        'Have your previous employers provided mental health benefits?',
        'Were you aware of the options for mental health care provided by your previous employers?',
        'Did your previous employers ever formally discuss mental health (as part of a wellness campaign or other official communication)?',
        'Did your previous employers provide resources to learn more about mental health issues and how to seek help?']].replace(np.nan, -1)

    df['Employer_Resource_Avail'] = (df[['Does your employer provide mental health benefits as part of healthcare coverage?',
                                        'Do you know the options for mental health care available under your employer-provided coverage?',
                                        'Has your employer ever formally discussed mental health (for example, as part of a wellness campaign or other official communication)?',
                                        'Does your employer offer resources to learn more about mental health concerns and options for seeking help?']].max(axis = 1) + df[['Have your previous employers provided mental health benefits?',
                                        'Were you aware of the options for mental health care provided by your previous employers?',
                                        'Did your previous employers ever formally discuss mental health (as part of a wellness campaign or other official communication)?',
                                        'Did your previous employers provide resources to learn more about mental health issues and how to seek help?']].max(axis = 1)) / 2

    df['Negative_Conseq'] = df[['Do you think that discussing a mental health disorder with your employer would have negative consequences?', 
                                'Do you think that discussing a mental health disorder with previous employers would have negative consequences?']].max(axis = 1)

    df['Comfortable_Discussing'] = df[['Would you feel comfortable discussing a mental health disorder with your coworkers?',
                                        'Would you have been willing to discuss a mental health issue with your previous co-workers?',
                                        'Would you feel comfortable discussing a mental health disorder with your direct supervisor(s)?',
                                        'Would you have been willing to discuss a mental health issue with your direct supervisor(s)?']].mean(axis = 1)

    df['Hurt_Career'] = df[['Do you feel that being identified as a person with a mental health issue would hurt your career?',
                            'Do you think that team members/co-workers would view you more negatively if they knew you suffered from a mental health issue?']].max(axis = 1)

    df[['If you have a mental health issue, do you feel that it interferes with your work when being treated effectively?',
                            'If you have a mental health issue, do you feel that it interferes with your work when NOT being treated effectively?']] = df[['If you have a mental health issue, do you feel that it interferes with your work when being treated effectively?',
                            'If you have a mental health issue, do you feel that it interferes with your work when NOT being treated effectively?']].replace(np.nan, -1)

    df['Productivity'] = df[['If you have a mental health issue, do you feel that it interferes with your work when being treated effectively?',
                            'If you have a mental health issue, do you feel that it interferes with your work when NOT being treated effectively?']].max(axis = 1)

    df['How willing would you be to share with friends and family that you have a mental illness?'].replace(
            "Somewhat open", 4, inplace=True)
    df['How willing would you be to share with friends and family that you have a mental illness?'].replace("Very open",
                                                                                                            5,
                                                                                                            inplace=True)
    df['How willing would you be to share with friends and family that you have a mental illness?'].replace(
        "Somewhat not open", 2, inplace=True)
    df['How willing would you be to share with friends and family that you have a mental illness?'].replace(
        "Not open at all", 1, inplace=True)
    df['How willing would you be to share with friends and family that you have a mental illness?'].replace("Neutral",
                                                                                                            3,
                                                                                                            inplace=True)
    df['How willing would you be to share with friends and family that you have a mental illness?'].replace(
        "Not applicable to me (I do not have a mental illness)", 0, inplace=True)

    df[['If so, what condition(s) were you diagnosed with?', 'If yes, what condition(s) have you been diagnosed with?',
        'If maybe, what condition(s) do you believe you have?']] = df[['If so, what condition(s) were you diagnosed with?', 'If yes, what condition(s) have you been diagnosed with?',
        'If maybe, what condition(s) do you believe you have?']].replace(np.nan, -1)

    df.replace('\.*mood.*', 2, regex=True, inplace=True)
    df.replace('\.*anxiety.*', 1, regex=True, inplace=True)
    df.replace('\.*Anxiety.*', 1, regex=True, inplace=True)
    df.replace('\.*Mood.*', 2, regex=True, inplace=True)

    df["What is your gender?"].replace(np.nan, 1, inplace=True)

    df[['If so, what condition(s) were you diagnosed with?', 'If yes, what condition(s) have you been diagnosed with?',
        'If maybe, what condition(s) do you believe you have?']] = df[['If so, what condition(s) were you diagnosed with?', 'If yes, what condition(s) have you been diagnosed with?',
        'If maybe, what condition(s) do you believe you have?']].replace('\.*', -1, regex=True)

    df[['If so, what condition(s) were you diagnosed with?', 'If yes, what condition(s) have you been diagnosed with?',
        'If maybe, what condition(s) do you believe you have?']] = df[['If so, what condition(s) were you diagnosed with?', 'If yes, what condition(s) have you been diagnosed with?',
        'If maybe, what condition(s) do you believe you have?']].replace("[^0-9]", -1, regex=True)

    df['Label'] = df[
        ['If so, what condition(s) were you diagnosed with?', 'If yes, what condition(s) have you been diagnosed with?',
            'If maybe, what condition(s) do you believe you have?']].max(axis=1)
    
    df = df[['What is your age?', 'What is your gender?', 'How many employees does your company or organization have?',
    'Do you work remotely?', 'Label', 'Do you have a family history of mental illness?',
    'Employer_Resource_Avail', 'Negative_Conseq', 'Comfortable_Discussing', 'Hurt_Career', 
    'How willing would you be to share with friends and family that you have a mental illness?', 'Productivity']]

    df.rename(columns = {'What is your age?': 'age', 'What is your gender?': 'gender', 'How many employees does your company or organization have?': "num_employees",
                     'Do you work remotely?': 'work_remote', 'Do you have a family history of mental illness?': 'family_history',
                     'How willing would you be to share with friends and family that you have a mental illness?': 'share_family'}, inplace = True)
    return df