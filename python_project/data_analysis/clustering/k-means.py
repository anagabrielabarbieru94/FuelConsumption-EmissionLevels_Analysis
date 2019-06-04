import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_samples, silhouette_score
from scipy import stats
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

file_name = "../../dissertation_datasets/merged_dataset.csv"
data_frame = pd.read_csv(file_name, encoding = "ISO-8859-1", error_bad_lines=False)
k_range = range(2, 10)


def cluster_by_euro_metric(column_name):
    silhouettes = []
    global data_frame

    for k in k_range:
        euro_types = set(data_frame['Euro standard'])
        data_frame['Euro standard'] = data_frame['Euro standard'].astype("category", categories=euro_types).cat.codes

        f1 = data_frame['Euro standard']
        f2 = data_frame[column_name]
        X = np.array(list(zip(f1, f2)))

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
        fig.savefig('cluster_plots/Euro_'+column_name+'_k-means_k'+str(k)+'.png')

    fig = plt.figure()
    silhouette = fig.add_subplot(111)
    silhouette.plot(k_range, silhouettes, 'b*-')
    plt.xlabel("Number of clusters")
    plt.ylabel("silhouette score")
    plt.title("Selecting the k with the Elbow Method")
    plt.show()
    plt.draw()
    fig.savefig('cluster_plots/Euro_'+column_name+'_k-means_silhouette.png')

def cluster_data(column_name):
    columns = ['Transmission',
               'Engine Capacity', 'Fuel Type', 'Euro standard', column_name]
    df_tr = data_frame[columns]
    silhouettes = []

    #transform categorical data
    #manufacturer_types = set(df_tr['Manufacturer'])
    #model_types = set(df_tr['Model'])
    transmission_types = set(df_tr['Transmission'])
    euro_types = set(df_tr['Euro standard'])
    fuel_types = set(df_tr['Fuel Type'])

    #df_tr['Manufacturer'] = df_tr['Manufacturer'].astype("category", categories=manufacturer_types).cat.codes
    #df_tr['Model'] = df_tr['Model'].astype("category", categories=model_types).cat.codes
    df_tr['Transmission'] = df_tr['Transmission'].astype("category", categories=transmission_types).cat.codes
    df_tr['Euro standard'] = df_tr['Euro standard'].astype("category", categories=euro_types).cat.codes
    df_tr['Fuel Type'] = df_tr['Fuel Type'].astype("category", categories=fuel_types).cat.codes

    # Cluster the data
    for k in k_range:
        df_tr_copy = df_tr
        # Standardize data
        df_tr_std = stats.zscore(df_tr_copy)
        kmeans = KMeans(n_clusters=k, random_state=0).fit(df_tr_std)
        labels = kmeans.labels_

        #Add clusters to the original data
        df_tr_copy['clusters'] = labels

        # Add the column into our list
        columns.extend(['clusters'])

        # Lets analyze the clusters
        clusters = df_tr_copy.groupby(['clusters']).mean()
        print(clusters)

        labels = kmeans.labels_
        print(labels)

        silhouette = silhouette_score(df_tr_std, labels)
        silhouettes.append(silhouette)

        fig = plt.figure()
        sns.lmplot('Euro standard', column_name,
                   data=df_tr_copy,
                   fit_reg=False,
                   hue="clusters",
                   scatter_kws={"marker": "D",
                                "s": 100})
        plt.title('Euro standard vs '+column_name)
        plt.xlabel('Manufacturer')
        plt.ylabel(column_name)

        plt.show()
        plt.draw()
        fig.savefig('cluster_plots/Euro_' + column_name + '_k-means_k' + str(k) + '.png')

    fig = plt.figure()
    silhouette = fig.add_subplot(111)
    silhouette.plot(k_range, silhouettes, 'b*-')
    plt.xlabel("Number of clusters")
    plt.ylabel("silhouette score")
    plt.title("Selecting the k with the Elbow Method")
    plt.show()
    plt.draw()
    fig.savefig('cluster_plots/Euro_' + column_name + '_k-means_silhouette.png')


if __name__ == "__main__":
    cluster_by_euro_metric('Metric Urban (Cold)')
    #cluster_data('Metric Urban (Cold)')
