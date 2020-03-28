from textblob import TextBlob
sentence="Forests have many trees, birds and animals. Forest are souce for water."
tbsentence=TextBlob(sentence)
tbsentences=tbsentence.sentences;
print(tbsentences)