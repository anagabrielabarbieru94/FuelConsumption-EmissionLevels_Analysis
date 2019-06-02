import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_samples, silhouette_score

import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

file_name = "../../dissertation_datasets/merged_dataset.csv"
data_frame = pd.read_csv(file_name, encoding = "ISO-8859-1", error_bad_lines=False)
k_range = range(2, 10)


def cluster_by_euro_metric_urban():
    silhouettes = []
    for k in k_range:
        f1 = data_frame['Euro standard']
        encoder = LabelEncoder()
        f1 = encoder.fit_transform(f1.astype('str'))
        f2 = data_frame['Metric Urban (Cold)']
        X = np.array(list(zip(f1, f2)))

        C_x = np.random.choice(f1, size=k)
        C_y = np.random.choice(f2, size=k)
        C = np.array(list(zip(C_x, C_y)))
        kmeans = KMeans(n_clusters=k)
        kmeans = kmeans.fit(X)
        print(kmeans)
        labels = kmeans.predict(X)
        silhouette_avg = silhouette_score(X, labels)
        silhouettes.append(silhouette_avg)
        print("For n_clusters =", k,
              "The average silhouette_score is :", silhouette_avg)
        centroids = kmeans.cluster_centers_
        fig = plt.figure()
        kx = fig.add_subplot(111)
        for i in range(k):
            points = np.array([X[j] for j in range(len(X)) if labels[j] == i])
            kx.scatter(points[:, 0], points[:, 1], s = 20, cmap='rainbow')
        kx.scatter(centroids[:, 0], centroids[:, 1], marker='.', s = 200, c='#050505')
        plt.grid(True)
        plt.xlabel("Euro standard")
        plt.ylabel("Metric Urban (Cold)")
        plt.title("Number of clusters={}".format(k))
        plt.show()
        plt.draw()
        fig.savefig('cluster_plots/euro_metric_urban_k-means_k'+str(k)+'.png')

    fig = plt.figure()
    silhouette = fig.add_subplot(111)
    silhouette.plot(k_range, silhouettes, 'b*-')
    plt.xlabel("Number of clusters")
    plt.ylabel("silhouette score")
    plt.title("Selecting the k with the Elbow Method")
    plt.show()
    plt.draw()
    fig.savefig('cluster_plots/euro_metric_urban_k-means_silhouette.png')


cluster_by_euro_metric_urban()
