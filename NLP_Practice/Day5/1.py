#!/usr/bin/env python
import os;
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer;
from sklearn.metrics.pairwise import cosine_similarity;

query='printer'
docList = [query];
namList=[query]
parentDir = "/home/ai37/newsgroups/";
files = os.listdir(parentDir);
for file in files:
	fullPath = parentDir+ file;
	filePtr = open(fullPath,'r');
        namList.append(filePtr.name)
	content  = filePtr.read();
	docList.append(content);

vectoriser = TfidfVectorizer(stop_words='english');
model = vectoriser.fit(docList);

matrix = vectoriser.fit_transform(docList);
print(model.vocabulary_);
print(matrix);

sim = cosine_similarity(matrix[0:1],matrix);
sim2=np.ravel(sim)
result =np.argwhere(sim2>0)
print(sim)
for j in range(result.size):
 i=np.asscalar(result[j])
 print(namList[i])
 print('-------------------------------------------------------------')

