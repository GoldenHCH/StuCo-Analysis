import pandas as pd
from nltk.corpus import wordnet
import os
import openai
from AI import *

openai.api_key = "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"
df = pd.read_csv('rand copy.csv')
# check_list = ["simple", "easy", "traditional", "communicating", "communication", "nostalgia", "food", "music", "pictures", "seniors", "fun"]

def ai(paragraph):
  response = openai.Completion.create(
    model="text-davinci-003",
    prompt= f"extract the keywords and classify the sentiment from {paragraph}",
    temperature=0.9,
    max_tokens=1000,
    top_p=1.0,
    frequency_penalty=0.8,
    presence_penalty=0.0
  )
  return response

def extract_keywords(df):
    for paragraphs in df["paragraph"]:
        word = ai(paragraphs)
        df['paragraph'].replace([paragraphs], word)

def synonym_extractor(phrase):
    synonyms = [] #create a list for synonyms
    antonyms = [] #create a list for antonyms

    for syn in wordnet.synsets(phrase):
        for l in syn.lemmas():
            synonyms.append(l.name())
            if l.antonyms():
                antonyms.append(l.antonyms()[0].name())

    return set(synonyms) #use set to eliminate repeated words

def syn_convert(df):
    #loop through the words
    for w in df.word:
        syn_set = synonym_extractor(w)
        # new_list = [x for x in cleaned_word_list if x != w]
        for i in range(len(df.word)):
            if df.word[i] in syn_set:
                df.word[i] = w
    return df.word

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

def plot(df):
    pass


def main():
    print(syn_convert(df))

main()