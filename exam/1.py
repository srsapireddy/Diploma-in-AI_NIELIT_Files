#!/bin/env python3

from textblob import TextBlob
from textblob import Word

list = ["cars", "buses", "trains"]


for word in list:
	tl = TextBlob(word).split()
	print(tl.singularize())
	x = raw_input("Enter plural of the word: ")
	if(tl == x):
       		print("Correct")
	else:
		print("Wrong")
	




