import sklearn
import sklearn.datasets
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import numpy as np
from sklearn.linear_model import SGDClassifier
from sklearn import metrics
from sklearn.model_selection import GridSearchCV

DETAIL = True

categories = ["pos", "neg"]

'''data load'''
data_train = sklearn.datasets.load_files("./train", description=None, categories=categories, load_content=True,
shuffle=True, encoding='latin-1', decode_error='strict', random_state=42)

data_test = sklearn.datasets.load_files("./test", description=None, categories=categories, load_content=True,
shuffle=True, encoding='latin-1', decode_error='strict', random_state=42)

'''Vectorization'''
count_vect= CountVectorizer()
X_train_counts = count_vect.fit_transform(data_train.data)

'''Indexation'''
tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)

'''Classification'''
clf = MultinomialNB().fit(X_train_tfidf, data_train.target)

'''Evaluation'''
docs_test = data_test.data
text_clf_NB = Pipeline([('vect', CountVectorizer()), ('tfidf', TfidfTransformer()), ('clf', MultinomialNB()),])
text_clf_SGDC = Pipeline([('vect', CountVectorizer()), ('tfidf', TfidfTransformer()), ('clf', SGDClassifier(loss='hinge', penalty='l2', alpha =1e-3, n_iter=5, random_state=42)),])

text_clf_NB = text_clf_NB.fit(data_train.data, data_train.target)
_ = text_clf_SGDC.fit(data_train.data, data_train.target)

predicted_NB = text_clf_NB.predict(docs_test)
predicted_SGDC = text_clf_SGDC.predict(docs_test)

print("\nPrediction :")
print("\tNaive Bays : {0}".format(np.mean(predicted_NB == data_test.target)))
print("\tSVM : {0}".format(np.mean(predicted_SGDC == data_test.target)))

'''Optimization WARNING ! Not working on Windows'''
parameters = {'vect__ngram_range':[(1,1),(1,2)],
            'tfidf__use_idf':(True, False),
            'clf__alpha':(1e-2, 1e-3),}
gs_clf = GridSearchCV(text_clf_SGDC, parameters, n_jobs=-1)#ici on lui donne beaucoup de ressources.
gs_clf = gs_clf.fit(data_train.data[:400], data_train.target[:400])
#print(twenty_train.target_names[gs_clf.predict(['God is love'])[0]])

#print(gs_clf.best_score_)

for param_name in sorted(parameters.keys()):
    print("%s: %r" % (param_name, gs_clf.best_params_[param_name]))


'''Outputs'''
if DETAIL:
    print("\nData loading :")
    print(data_train.target_names)
    print(len(data_train.data))
    print(len(data_train.filenames))
    print("\n".join(data_train.data[0].split("\n")[:3]))

    print("\n--------------------")
    print("\nVectorisation : ")
    print(X_train_counts.shape)
    print(count_vect.vocabulary_.get(u'algorithm'))

    print("\n--------------------")
    print("\nIndexation : ")
    print(X_train_tfidf.shape)

    print("\n--------------------")
    print("\nMetrics : ")
    print("\nClassification for Naive Bayes")
    print(metrics.classification_report(data_test.target, predicted_NB, target_names=data_test.target_names))
    print("\nMatrix for Naive Bayes")
    print(metrics.confusion_matrix(data_test.target, predicted_NB))

    print("\nClassification for SVM")
    print(metrics.classification_report(data_test.target, predicted_SGDC, target_names=data_test.target_names))
    print("\nMatrix for SVM")
    print(metrics.confusion_matrix(data_test.target, predicted_SGDC))
