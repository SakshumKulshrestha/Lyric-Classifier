from preprocess import preprocess
from sklearn.naive_bayes import GaussianNB as classifier

f_train, f_test, l_train, l_test = preprocess()
classifier.fit(f_train, l_train)

print("accuracy: " + str(classifier.score(f_test, l_test)))