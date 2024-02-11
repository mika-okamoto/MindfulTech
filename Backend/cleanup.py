import pandas as pd
import numpy as np


def cleanup(df):
    df = df[df["Are you self-employed?"] != 1]
    df = df[(df["Are you self-employed?"] != 1) & (
        df["Is your primary role within your company related to tech/IT?"].isin(['', 1, np.nan]))]
    replace_dict = {"nonbinary": 1, 'female': 2, 'Female': 2, 'F': 2, 'f': 0, 'M': 0, 'm': 0, 'Male': 0, 'male': 0,
                    "woman": 2, "cis male": 0, "Cis male": 0, "dude": 0}
    df["What is your gender?"] = df["What is your gender?"].replace(replace_dict, regex=True)
    df["What is your gender?"] = df["What is your gender?"].replace(to_replace=r'[^0-2]', value=1, regex=True)
    df.replace('Not eligible for coverage / N/A', np.nan, inplace=True)
    df.replace('Not applicable to me', np.nan, inplace=True)
    df.replace('I am not sure', 'Unsure', inplace=True)
    df.replace("I don't know", 'Unsure', inplace=True)
    df.replace('Very difficult', 5, inplace=True)
    df.replace('Somewhat difficult', 4, inplace=True)
    df.replace('Neither easy nor difficult', 3, inplace=True)
    df.replace('Somewhat easy', 2, inplace=True)
    df.replace('Very easy', 1, inplace=True)
    df.replace("Yes", 1, inplace=True)
    df.replace("Yes, always", 1, inplace=True)
    df.replace("Maybe", 0.5, inplace=True)
    df.replace("Sometimes", 0.5, inplace=True)
    df.replace("No", 0, inplace=True)
    df['Do you feel that your employer takes mental health as seriously as physical health?'].replace("Unsure", 0.5,
                                                                                                      inplace=True)
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
    df['Do you feel that being identified as a person with a mental health issue would hurt your career?'].replace(0.5,
                                                                                                                   3,
                                                                                                                   inplace=True)
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
        "Not applicable to me (I do not have a mental illness)", np.nan, inplace=True)
    df.replace("Maybe/Not sure", 0.5, inplace=True)
    df.replace("Yes, I observed", 1, inplace=True)
    df.replace("Yes, I experienced", 2, inplace=True)
    df[
        'If you have a mental health issue, do you feel that it interferes with your work when being treated effectively?'].replace(
        0.5, 2, inplace=True)
    df[
        'If you have a mental health issue, do you feel that it interferes with your work when being treated effectively?'].replace(
        "Rarely", 1, inplace=True)
    df[
        'If you have a mental health issue, do you feel that it interferes with your work when being treated effectively?'].replace(
        "Often", 3, inplace=True)
    df[
        'If you have a mental health issue, do you feel that it interferes with your work when being treated effectively?'].replace(
        "Never", 0, inplace=True)
    df[
        'If you have a mental health issue, do you feel that it interferes with your work when NOT being treated effectively?'].replace(
        0.5, 2, inplace=True)
    df[
        'If you have a mental health issue, do you feel that it interferes with your work when NOT being treated effectively?'].replace(
        "Rarely", 1, inplace=True)
    df[
        'If you have a mental health issue, do you feel that it interferes with your work when NOT being treated effectively?'].replace(
        "Often", 3, inplace=True)
    df[
        'If you have a mental health issue, do you feel that it interferes with your work when NOT being treated effectively?'].replace(
        "Never", 0, inplace=True)
    df['Do you work remotely?'].replace("Always", 1, inplace=True)
    df['Do you work remotely?'].replace("Never", 0, inplace=True)
    df['Do you work remotely?'].replace("Never", 0, inplace=True)
    df.replace('1-5', 0, inplace=True)
    df.replace('6-25', 1, inplace=True)
    df.replace('26-100', 2, inplace=True)
    df.replace('100-500', 3, inplace=True)
    df.replace('500-1000', 4, inplace=True)
    df.replace('More than 1000', 5, inplace=True)
    df['Does your employer provide mental health benefits as part of healthcare coverage?'].replace(np.NaN, 0,
                                                                                                    inplace=True)
    df['Do you know the options for mental health care available under your employer-provided coverage?'].replace(
        'Unsure', 0.5, inplace=True)
    df['Do you know the options for mental health care available under your employer-provided coverage?'].replace(
        np.NaN, 0.25, inplace=True)
    df[
        'Is your anonymity protected if you choose to take advantage of mental health or substance abuse treatment resources provided by your employer?'].replace(
        'Unsure', 0.5, inplace=True)
    df[
        'Is your anonymity protected if you choose to take advantage of mental health or substance abuse treatment resources provided by your employer?'].replace(
        np.NaN, 0.5, inplace=True)
    df.replace(np.NaN, -1.0, inplace=True)

    df.replace('\.*mood.*', 2, regex=True, inplace=True)
    df[['If so, what condition(s) were you diagnosed with?', 'If yes, what condition(s) have you been diagnosed with?',
        'If maybe, what condition(s) do you believe you have?']].replace('\.*anxiety.*', 1, regex=True, inplace=True)
    df.replace('\.*Anxiety.*', 1, regex=True, inplace=True)
    df.replace('\.*Mood.*', 2, regex=True, inplace=True)

    df[['If so, what condition(s) were you diagnosed with?', 'If yes, what condition(s) have you been diagnosed with?',
        'If maybe, what condition(s) do you believe you have?']].replace('\.*', 3, regex=True, inplace=True)

    df[['If so, what condition(s) were you diagnosed with?', 'If yes, what condition(s) have you been diagnosed with?',
        'If maybe, what condition(s) do you believe you have?']].replace("[^0-9]", 3, regex=True, inplace=True)

    df.replace("[^0-9]", -1.0, regex=True, inplace=True)

    df['Label'] = df[
        ['If so, what condition(s) were you diagnosed with?', 'If yes, what condition(s) have you been diagnosed with?',
         'If maybe, what condition(s) do you believe you have?']].max(axis=1)

    df.drop(
        ['If so, what condition(s) were you diagnosed with?', 'If yes, what condition(s) have you been diagnosed with?',
         'If maybe, what condition(s) do you believe you have?'], axis=1, inplace=True)
    df = df[(df['What is your age?'] > 18) & (df['What is your age?'] < 100)]

    # print(df.columns)
    df['Do you think that discussing mental health at work would have negative consequences?'] = df[
        ['Do you think that discussing a mental health disorder with your employer would have negative consequences?',
         'If a mental health issue prompted you to request a medical leave from work, asking for that leave would be:',
         'Do you think that discussing a physical health issue with your employer would have negative consequences?',
         'Have you heard of or observed negative consequences for co-workers who have been open about mental health issues in your workplace?',
         'If you have revealed a mental health issue to a coworker or employee, do you believe this has impacted you negatively?']].sum(
        axis=1)

    df['Comfort Discussing Mental Health problems'] = df[
        ['Would you feel comfortable discussing a mental health disorder with your coworkers?',
         'Would you feel comfortable discussing a mental health disorder with your direct supervisor(s)?',
         'Do you feel that your employer takes mental health as seriously as physical health?',
         'If you have revealed a mental health issue to a client or business contact, do you believe this has impacted you negatively?',
         'If you have been diagnosed or treated for a mental health disorder, do you ever reveal this to coworkers or employees?']].sum(
        axis=1)

    df.drop(['Are you self-employed?', 'Is your employer primarily a tech company/organization?',
             'Is your primary role within your company related to tech/IT?', 'Why or why not?', 'Why or why not?.1',
             'What country do you work in?', 'What country do you live in?',
             'What US state or territory do you live in?', 'What US state or territory do you work in?',
             'Has your employer ever formally discussed mental health (for example, as part of a wellness campaign or other official communication)?'],
            inplace=True, axis=1)

    df.drop(['Would you feel comfortable discussing a mental health disorder with your coworkers?',
             'Would you feel comfortable discussing a mental health disorder with your direct supervisor(s)?',
             'Do you feel that your employer takes mental health as seriously as physical health?',
             'If you have revealed a mental health issue to a client or business contact, do you believe this has impacted you negatively?',
             'If you have been diagnosed or treated for a mental health disorder, do you ever reveal this to coworkers or employees?'],
            inplace=True, axis=1)

    df.drop(
        ['Do you think that discussing a mental health disorder with your employer would have negative consequences?',
         'If a mental health issue prompted you to request a medical leave from work, asking for that leave would be:',
         'Do you think that discussing a physical health issue with your employer would have negative consequences?',
         'Have you heard of or observed negative consequences for co-workers who have been open about mental health issues in your workplace?',
         'If you have revealed a mental health issue to a coworker or employee, do you believe this has impacted you negatively?'],
        inplace=True, axis=1)
    return df
