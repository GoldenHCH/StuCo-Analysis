import pandas as pd
from nltk.corpus import wordnet

df = pd.read_csv('rand copy.csv')
check_list = ["simple", "easy", "traditional", "communicating", "communication", "nostalgia", "food", "music", "pictures", "seniors", "fun"]

def synonym_antonym_extractor(phrase):
    synonyms = []
    antonyms = []

    for syn in wordnet.synsets(phrase):
        for l in syn.lemmas():
            synonyms.append(l.name())
            if l.antonyms():
                antonyms.append(l.antonyms()[0].name())

    return set(synonyms)

def syn_convert(cleaned_word_list):
    for w in cleaned_word_list:
        syn_set = synonym_antonym_extractor(w)
        # new_list = [x for x in cleaned_word_list if x != w]
        for i in range(len(cleaned_word_list)):
            if cleaned_word_list[i] in syn_set:
                cleaned_word_list[i] = w
    return cleaned_word_list

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
