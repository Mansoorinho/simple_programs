"""
A simple English dictionary created by Mansoor Nabawi on Jun 5
"""
import json
#from difflib import SequenceMatcher as SQ
from difflib import get_close_matches as gcm
#loading the dictionary as data
data = json.load(open("data.json","r"))

def translate(word: str)-> str:
    """
    This function get a word as an input and search for its meaning\
    if the word entered didn't exactly match to the dictionary\
    it looks for the closest match and asks user's opinion.
    """
    word = word.lower()
    if word in data:
        return data[word]
    elif gcm(word, data.keys(),cutoff=0.8):
        Possib =  gcm(word, data.keys())[0]
        UserAnswer = input (f"Did you mean '{Possib}' ? 'Y' for yes 'N' for no: ")
        if UserAnswer == "Y":
            return translate(Possib)
        elif UserAnswer == "N":
            return f"The word '{word} does not exist, please double check"
        else:
            return "We didn't uderstand your query!"
    else:
        return f"the word '{word}' does not exist, please double check it"

word = input("Enter a word: ")
print(translate(word))