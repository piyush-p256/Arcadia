from sklearn.cluster import KMeans
import numpy as np

def analyze(data):
    X = np.array([list(stat.values()) for stat in data.recent_matches])
    kmeans = KMeans(n_clusters=3).fit(X)
    cluster = kmeans.predict([list(data.stats.values())])[0]
    return {"player_id": data.player_id, "playstyle_cluster": int(cluster)}
