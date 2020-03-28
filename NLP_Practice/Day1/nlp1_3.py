from textblob import TextBlob
sentence="Forests have many trees, birds and animals. Forest are souce for water."
tbsentence=TextBlob(sentence)
print(tbsentence.noun_phrases)