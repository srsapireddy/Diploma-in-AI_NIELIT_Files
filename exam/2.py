#!/bin/env python3
from textblob import TextBlob

# file1 = open("/home/ai37/Desktop/exam/file.txt",mode="r")
# file = TextBlob(str(file1))

t = TextBlob("Beautiful is better than ugly. "
				   "Explicit is better than implicit. "
				   "Simple is better than complex.")
print(t.sentences)
print(t.words)

x = input("Enter an integer: ")
print(t.words[x])
print(t.sentences[x])

a = t.sentences
c = len(a)
print(t.words[c])




