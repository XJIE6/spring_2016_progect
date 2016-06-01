
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import nltk.stem
import scipy as sp
import pickle
def dist_norm(vl, v2):
    vl_normalized = vl/sp.linalg.norm(vl.toarray())
    v2_normalized = v2/sp.linalg.norm(v2.toarray())
    delta = vl_normalized - v2_normalized
    return sp.linalg.norm(delta.toarray())
arr = []
arr = pickle.load(open('./resources/data/data.txt', 'rb'))
print(len(arr))
print("evaled")

english_stemmer = nltk.stem.SnowballStemmer('english')

class StemmedTfidVectorizer (TfidfVectorizer):
    def build_analyzer (self ):
        analyzer = super(TfidfVectorizer, self).build_analyzer()
        return lambda doc: (english_stemmer.stem(w) for w in analyzer(doc))

vectorizer1 = StemmedTfidVectorizer(min_df = 10, max_df = 0.5, stop_words = 'english', decode_error = 'ignore')
vectorizer2 = StemmedTfidVectorizer(min_df = 10, max_df = 0.5, decode_error = 'ignore')
vectorizer3 = StemmedTfidVectorizer(min_df = 10, max_df = 0.5, decode_error = 'ignore')
print('before vectorizing')
vectorised1 = vectorizer1.fit_transform([c for (c, a, b) in arr])
res_a = []
for (c, a, b) in arr:
    cur = ""
    for ax in a:
        cur = cur + ax + "\n"
    res_a.append(cur)
vectorised2 = vectorizer2.fit_transform(res_a)
res_b = []
for (c, a, b) in arr:
    cur = ""
    for bx in b:
        cur = cur + bx + "\n"
    res_b.append(cur)
vectorised3 = vectorizer3.fit_transform(res_b)
print("before k-means")
num_clusters = 3
km1 = KMeans(n_clusters = num_clusters , init = 'random', n_init = 1 , verbose = 1)
km2 = KMeans(n_clusters = num_clusters , init = 'random', n_init = 1 , verbose = 1)
km3 = KMeans(n_clusters = num_clusters , init = 'random', n_init = 1 , verbose = 1)
print("k-means ready")
km1.fit(vectorised1)
km2.fit(vectorised2)
km3.fit(vectorised3)

