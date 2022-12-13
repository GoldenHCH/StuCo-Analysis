import pandas as pd
from nltk.corpus import wordnet
import models as md

df = pd.read_csv('dataFrame.csv')

def main():
    good = md.good_attr(df)
    bad = md.bad_attr(df)
    good = md.syn_convert(good)
    bad = md.syn_convert(bad)
    good = md.analyze(good)
    bad = md.analyze(bad)
    good_df = md.creat_df(good, bad, "good")
    bad_df = md.creat_df(good, bad, "bad")
    print(good_df)
    print(bad_df)

main()