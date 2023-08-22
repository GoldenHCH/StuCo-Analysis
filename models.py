import pandas as pd
from nltk.corpus import wordnet
import os
import openai
from AI import *
import gspread
from oauth2client import service_account as sv_acc

openai.api_key = "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"

#input a paragraph, extract keywords, output a string of keywords
def ai(paragraph):
  response = openai.Completion.create(
    model="text-davinci-003",
    prompt= f"extract the keywords from {paragraph}, make sure the words are separated by commas",
    temperature=0.9,
    max_tokens=1000,
    top_p=1.0,
    frequency_penalty=0.8,
    presence_penalty=0.0
  )
  return str(response['choices'][0]['text'])

#input, loop through dataframe, convert each paragraphs in cells in the dataframe into keywords using the "ai" function
#this function edits the dataframe
def convert_to_keywords(df):
    for i in range(len(df)):
        word = ai(df.loc[i, "Response"])
        df.loc[i, "Response"] = word

#finds all the synonyms of the input
#input a string (word/phrase) and output a set of all the synonyms
def synonym_extractor(phrase):
    synonyms = [] #create a list for synonyms
    antonyms = [] #create a list for antonyms

    for syn in wordnet.synsets(phrase):
        for l in syn.lemmas():
            synonyms.append(l.name())
            if l.antonyms():
                antonyms.append(l.antonyms()[0].name())

    return set(synonyms) #use set to eliminate repeated words


def syn_convert(list):
    #loop through the words
    for w in list:
        syn_set = synonym_extractor(w)
        # new_list = [x for x in cleaned_word_list if x != w]
        for i in range(len(list)):
            if list[i] in syn_set:
                list[i] = w
    return list

def good_attr(df):
    words, lists, lol, final, cleaned_list = [], [], [], [], []
    good_words = df.loc[df["Rating"] == "Good", "word"]
    for list in good_words:
        lol.append(list)

    for i in lol:
        lists.append(i)

    for i in lists:
        words.append(i)
        for i in words:
            final = i.split(",")

        for i in final:
            i = i.replace("Keywords: ", "")
            i = i.replace("[", "")
            i = i.replace("]", "")
            i = i.replace("'", "")
            i = i.replace(" ", "")
            i = i.lower()
            cleaned_list.append(i)

    return cleaned_list

def bad_attr(df):
    words = []
    lists = []
    lol = []
    final = []
    cleaned_list = []
    bad_words = df.loc[df["Rating"] == "Poor", "word"]
    for list in bad_words:
        lol.append(list)

    for i in lol:
        lists.append(i)

    for i in lists:
        words.append(i)
        for i in words:
            final = i.split(",")

        for i in final:
            i = i.lower()
            i = i.replace("[", "")
            i = i.replace("]", "")
            i = i.replace("'", "")
            i = i.strip()
            i = i.replace(" ", "_")
            i = i.lower()
            cleaned_list.append(i)
    return cleaned_list

def analyze(list):
    lists = {}
    for val in list:
        if val in lists.keys():
            count = lists[val]
            count += 1
            lists[val] = count
        else:
            lists[val] = 1
    sorted_dict = sorted(lists.items(), key=lambda item: item[1])
    return sorted_dict


def compare(good_dict, bad_dict):
    pass

def creat_df(good, bad, out_in_string):
    df_good = pd.DataFrame(good, columns=['Word', 'Occurance'])
    df_bad = pd.DataFrame(bad, columns=['Word', 'Occurance'])
    if out_in_string == "good":
        return df_good
    elif out_in_string == "bad":
        return df_bad


def api():
    scopes = {
        'https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive'
    }

    creds = sv_acc.ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scopes=scopes)

    # read data from sheet into a pandas dataframe
    file = gspread.authorize(creds)
    worksheet = file.open('Analysis of things that make an event successful  (Responses)').sheet1
    data = worksheet.get_all_values()
    headers = data.pop(0)
    df = pd.DataFrame(data, columns=headers)
    # df.drop(columns=['Time'])

    new_df = pd.DataFrame(df, columns=['Event', 'Response', "Rating"])

    return df
