from textblob import TextBlob
sentence="Forests have many treees, birrds and animals. Forest are souce for water."
tbsentence=TextBlob(sentence)
print(tbsentence.correct())