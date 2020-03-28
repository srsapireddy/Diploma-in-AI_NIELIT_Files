#!/usr/bin/env python
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

texts = [
    'Timmy bought bright blue fishes.',
    'Timmy bought bright blue and orange bowl.',
    'The dog ate a fish at the store.',
    'Timmy went to the store. Timmy ate a bug. Timmy saw a fish.',
    'It meowed once at the bug, it is still barking at the bug and the fish',
    'The dog is at the fish store. The dog is orange. The dog is barking at the fish.',
    'Timmy is a fish.',
    'Timmy Timmy she loves fishes Timmy Timmy is no dog .',
    'The store is closed now.',
    'How old is that tree?',
    'I do not eat fish I do not eat dogs I only eat bugs.'
]
                                             
tfidf=TfidfVectorizer(stop_words='english')
vectoriser=TfidfVectorizer()
vectoriser.fit(texts)
vocab=vectoriser.vocabulary_
matrix=tfidf.fit_transform(texts);
kmeans=KMeans(n_clusters=2);
kmeans.fit(matrix)
labels=kmeans.labels_;
for i in range(len(labels)):
 print(str(texts[i])+"belongs to clusters"+str(labels[i]))
DF={}
for i in range(len(texts)):
    tokens = texts[i]
    for w in tokens:
        try:
            DF[w].add(i)
        except:
            DF[w] = {i} 
for i in DF:
 DF[i] =len(DF[i])
 DF
plt.scatter(texts,labels,c=labels)
plt.show()

