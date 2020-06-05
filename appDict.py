"""
A simple English dictionary created by Mansoor Nabawi on Jun 5
"""
import json

data = json.load(open("data.json","r"))

def translate(word: str)-> str:
    word = word.lower()
    if word in data:
        return data[word]
    else:
        return f"the word '{word}' does not exist, please double check it"

word = input("Enter a word: ")
print(translate(word))