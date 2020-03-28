#!/usr/bin/env python
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score

documents = [
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

vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(documents)

true_k = 2
model = KMeans(n_clusters=true_k, init='k-means++', max_iter=100, n_init=1)
model.fit(X)

print("Top terms per cluster:")
order_centroids = model.cluster_centers_.argsort()[:, ::-1]
terms = vectorizer.get_feature_names()
for i in range(true_k):
    print "Cluster %d:" % i,
    for ind in order_centroids[i, :10]:
        print ' %s' % terms[ind],
    print

