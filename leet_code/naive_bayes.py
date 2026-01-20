# Implementing Naive Bayes - multinomial model for text classification


dataset = [
    ("Win money now", "spam"),
    ("Cheap loans available", "spam"),
    ("Limited time offer", "spam"),
    ("Congratulations you won a prize", "spam"),
    ("Free gift card offer", "spam"),

    ("Hi how are you", "ham"),
    ("Let's meet tomorrow", "ham"),
    ("Are you coming to the party", "ham"),
    ("Please call me", "ham"),
    ("See you soon", "ham")
]


def tokenize(text):
    return text.lower().split()#splitting the texts into words

import math
from collections import defaultdict,Counter

def train_naive_bayes(dataset):
    class_counts = Counter()
    word_counts = defaultdict(Counter)
    vocabulary = set()

    #Count words & classes

    for text,label in dataset:
        class_counts[label] += 1
        words = tokenize(text)
        for word in words:
            word_counts[label][word] += 1
            vocabulary.add(word)
    
    total_docs = sum(class_counts.values())
    priors = {}

    # Prior probability P(class)
    for cls in class_counts:
        priors[cls] = class_counts[cls]/total_docs

    return class_counts,word_counts,vocabulary,priors 


def predict(text,class_counts,word_counts,vocabulary,priors):
    words = tokenize(text)
    scores = {}

    vocab_size = len(vocabulary)

    for cls in class_counts:
        log_prob = math.log(priors[cls]) #logarithm of prior probability
        total_words_in_class = sum(word_counts[cls].values())

        for word in words:
            word_freq = word_counts[cls][word] + 1
            word_prob = word_freq / (total_words_in_class + vocab_size)
            log_prob += math.log(word_prob)#use logs to avoid tiny 
        
        scores[cls] = log_prob

    print(scores)
    return max(scores,key=scores.get)




class_counts,word_counts,vocabulary,priors = train_naive_bayes(dataset)

print(predict("free free lottery offer", class_counts, word_counts, vocabulary, priors))
print(predict("hi", class_counts, word_counts, vocabulary, priors))
