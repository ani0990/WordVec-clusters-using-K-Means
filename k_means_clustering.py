# -*- coding: utf-8 -*-

from sklearn.cluster import KMeans
import time
from numpy import *

def load_wv(vocabfile, wvfile):
    wv = loadtxt(wvfile, dtype=float,delimiter=',')
    with open(vocabfile) as fd:
        words = [line.strip() for line in fd]
    num_to_word = dict(enumerate(words))
    word_to_num = {v:k for k,v in num_to_word.items()}
    return wv, word_to_num, num_to_word

wv, word_to_num, num_to_word = load_wv('./vocabulary.txt', './embeddings.txt')

start = time.time() # Start time

# Set "k" (num_clusters) to be 1/5th of the vocabulary size, or an
# average of 5 words per cluster
word_vectors = wv
num_clusters = int(word_vectors.shape[0] / 10)

# Initalize a k-means object and use it to extract centroids
kmeans_clustering = KMeans( n_clusters = num_clusters )
idx = kmeans_clustering.fit_predict( word_vectors )

# Get the end time and print how long the process took
end = time.time()
elapsed = end - start
print("Time taken for K Means clustering: ", elapsed, "seconds.")

index2word =[]
for i in range(0,len(num_to_word)):
    index2word.append(num_to_word[i])
                                                                                           
word_centroid_map = dict(zip(index2word, idx ))

# For the first 10 clusters
for cluster in range(0,10):
    
    # Print the cluster number  
    print("\nCluster %d" % cluster)
    
    # Find all of the words for that cluster number, and print them out
    words = []
    for i in range(0,len(word_centroid_map)):
        if( word_centroid_map[list(word_centroid_map)[i]] == cluster ):
            words.append(list(word_centroid_map)[i])
    print(words)
