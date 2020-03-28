#!/usr/bin/env python3
from textblob import TextBlob;


Sentence = TextBlob("Python is a high-level, general-purpose programming language.")
print(Sentence.tags); 