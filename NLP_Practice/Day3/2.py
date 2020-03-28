#!/usr/bin/env python
from textblob.classifiers import NaiveBayesClassifier;


file = open('/home/ai37/Desktop/sac.txt','r');
record = file.readline().strip();

trainData = [];
while record:
#	print(record);
	data = record.split(',');
#	print(data[0]);
#	print(data[1]);
	record = file.readline().strip();
	category = data[0];
	content = data[1];
	tuple = content , category;
	trainData.append(tuple);
print("Training ..");
classifier = NaiveBayesClassifier(trainData);
print(classifier.classify('Measles antibody: reevaluation of protective titers.'));
	
