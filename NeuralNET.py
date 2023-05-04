# import necessary libraries
import numpy as np
import nltk
from nltk.stem.porter import PorterStemmer

# create an instance of PorterStemmer
Stemmer = PorterStemmer()

# function to tokenize sentence
def Tokenized(sentence):
    return nltk.word_tokenize(sentence)

# function to perform stemming
def Stems(word):
    return Stemmer.stem(word.lower())

# function to create bag of words
def bag_of_words(tokenized_sentence, words):
    # perform stemming on each word of the tokenized sentence
    sentence_word = [Stems(word) for word in tokenized_sentence]
    # initialize the bag with zeros
    bag = np.zeros(len(words), dtype=np.float32)

    # loop through each word in words and set bag value to 1 if word is present in sentence_word
    for idx, w in enumerate(words):
        if w in sentence_word:
            bag[idx] = 1

    return bag
