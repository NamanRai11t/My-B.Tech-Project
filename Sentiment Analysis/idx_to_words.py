import pickle

sentence_file = open('featureMatrix_train.txt', 'r')
word2idx = pickle.load(open('word_idx.pickle', 'rb'))

print(len(word2idx))

print(word2idx[7])

sentences = []

for line in sentence_file:
    sentences.append(line.split(' '))

print(sentences[1])

X = pickle.load(open('X.pickle', 'rb'))
for i in range(50):
    print(X[i])

y = []


'''

for sentence in sentences:
    temp = []
    for word in sentence[:-1]:
        try:
            temp.append(word2idx[int(float(word))])
        except:
            temp.append('NOTINFILE')
    X.append(temp)
    y.append(float(sentence[-1][:-1]))

print(len(X))

pickle.dump(X, open('X.pickle', 'wb'))
pickle.dump(y, open('y.pickle', 'wb'))
'''