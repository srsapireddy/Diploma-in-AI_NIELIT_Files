from textblob import TextBlob;
from textblob import Word;

para = "Rains give us water and cool climate. Children are playing in the rain. Jack and John are splashing  water. The children are enjoying the rain.";

tPara = TextBlob(para);
tagList = tPara.tags;

text_blob_object = TextBlob(para)

freqTable = dict();

for word , pos in tagList: 
	if (pos.startswith('NN')):
		word = word.lower();
		if (freqTable.has_key(word)):
			freqTable[word] = freqTable[word]+ 1;
		else :
			freqTable[word] = 1;


print(freqTable);
print("Number of Words: ")
print( len(freqTable))

document_sentence = text_blob_object.sentences

print(document_sentence)
print("Number of Sentences: ")
print(len(document_sentence))
 