from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

vectorizer = TfidfVectorizer(stop_words='english')

def cluster_documents(docs, n_clusters=5):
    X = vectorizer.fit_transform(docs)
    km = KMeans(n_clusters=n_clusters, random_state=42).fit(X)
    return km.labels_.tolist()
