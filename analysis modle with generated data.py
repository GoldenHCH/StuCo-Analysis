import pandas as pd

df = pd.read_csv('rand copy.csv')

def good_attr():
    words = []
    lists = []
    lol = []
    final = []
    cleaned_list = []
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

def bad_attr():
    words = []
    lists = []
    lol = []
    final = []
    cleaned_list = []
    good_words = df.loc[df["Rating"] == "Poor", "word"]
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

def creat_df(good, bad, out):
    df_good = pd.DataFrame(good, columns=['Word', 'Occurance'])
    df_bad = pd.DataFrame(bad, columns=['Word', 'Occurance'])
    if out == good:
        return df_good
    elif out == bad:
        return df_bad

def plot(df):
    pass

def main():
    good = good_attr()
    bad = bad_attr()
    print(analyze(good))
    print(analyze(bad))
    # print(f"Words in bad events {analyze(bad)}")


main()