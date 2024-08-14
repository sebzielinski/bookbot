from operator import itemgetter
from collections import OrderedDict

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        return file_contents


def numOfWords(text):
    words = text.split()
    return len(words)


def numOfChars(text):
    charDict = {}
    text = text.lower()
    
    for char in text:
        if char in charDict.keys():
            charDict[char] = charDict[char] + 1
        else:
            charDict[char] = 1
    return charDict


def sortOn(dict):
    
    return dict["num"]

def printReport(text):
    num_words = numOfWords(text)
    char_dict = numOfChars(text)

    sorted_chars = OrderedDict(sorted(char_dict.items(), key=itemgetter(1), reverse=True))
    # print(sorted_chars)

    # --- print stuff ---
    
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document\n")
    for char in sorted_chars:
        if char.isalpha():
            print(f"The '{char}' character was found {sorted_chars[char]} times")
    print("--- End report ---")



if __name__ == "__main__":
    text = main()
    printReport(text)

