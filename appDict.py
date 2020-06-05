"""
A simple English dictionary created by Mansoor Nabawi on Jun 5
"""
import json
from difflib import SequenceMatcher as SQ
from difflib import get_close_matches as gcm

data = json.load(open("data.json","r"))
print(type(data))

def translate(word: str)-> str:
    word = word.lower()
    if word in data:
        return data[word]
    elif gcm(word, data.keys(),cutoff=0.8):
        Possib =  gcm(word, data.keys())[0]
        posibWord = input (f"Did you mean '{Possib}'' ? ")
        if posibWord == "Y":
            return translate(Possib)
        else:
            return "Good bye"
    else:
        return f"the word '{word}' does not exist, please double check it"

word = input("Enter a word: ")
print(translate(word))