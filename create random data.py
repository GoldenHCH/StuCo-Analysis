import random
import pandas as pd
import re

listA = []
listB = []
listC = []
listD = []
listE = []
listF = []

for i in range(1, 10):
    listA.append(random.randint(1, 9))
    listB.append(random.randint(1, 9))
    listC.append(random.randint(1, 9))
    listD.append(random.randint(1, 9))
    listE.append(random.randint(1, 9))
    listF.append(random.randint(1, 9))

event_list = ['a', 'b', 'c', 'd', 'e', 'f']

num_to_word = {
    1: "apple",
    2: "banana",
    3: "capital",
    4: "delta",
    5: "elephant",
    6: "fine",
    7: "gold",
    8: "high",
    9: "jump"
}

def word(number):
    return num_to_word[number]

new_listA = []
new_listB = []
new_listC = []
new_listD = []
new_listE = []
new_listF = []

def to_word(list,new_list):
    for items in list:
        new_list.append(word(items))

to_word(listA,new_listA)
to_word(listB,new_listB)
to_word(listC,new_listC)
to_word(listD,new_listD)
to_word(listE,new_listE)
to_word(listF,new_listF)

lol = [new_listA, new_listB, new_listC, new_listD, new_listE, new_listF]
df = pd.DataFrame({"event": event_list, "word": lol})

df.to_csv("rand.csv")