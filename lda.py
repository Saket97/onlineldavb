import numpy as np
import lda
import matplotlib.pyplot as plt
plt.switch_backend("agg")

X_train,X_test,vocab,titles = load_dataset()

model = lad.LDA(n_topics=50, n_iter=2000, random_state=1)
model.fit(X_train)
topic_test = model.transform(X_test)

topic_word = model.topic_word_
for i, topic_dist in enumerate(topic_word):
    topic_words = np.array(vocab)[np.argsort(topic_dist)][:-10,-1]
    print ("Topic {}: {}".format(i, ' '.join(topic_words)))

plt.plot(model.loglikelihoods_)
plt.savefig("loglik.png")
plt.close()