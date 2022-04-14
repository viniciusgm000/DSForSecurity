#!/usr/bin/python
# -*- encoding: iso-8859-1 -*-

from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import normalize
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np 
import seaborn as sns

# le o dado original
df = pd.read_csv("data_final.csv")
df_droped = df.drop(columns=['Class'])
values = df_droped.values

# salva os labels originais e converte utilizando uma enumeracao
labels = df['Class'].values
d = dict([(y,x) for x,y in enumerate(sorted(set(labels)))])
# benign 0 - malicious 1
# print(d)
# print([d[x] for x in labels])
labels_enum = [d[x] for x in labels]

# realiza uma normalizacao quadratica: https://stats.stackexchange.com/questions/225564/scikit-learn-normalization-mode-l1-vs-l2-max
normalized_data = normalize(values, norm='l2')
normalized_df = pd.DataFrame(normalized_data)

# faz a clusterizacao e extrai os labels encontrados
kmeans = KMeans(n_clusters=2, n_init=5, init='k-means++', random_state=42).fit(normalized_df)
labels_scale = kmeans.labels_
# clusters_scale = pd.concat([normalized_df, pd.DataFrame({'cluster_scaled':labels_scale})], axis=1)

# realiza um pca dos clusters encontrados e plota com os labels encontrados
pca2 = PCA(n_components=3).fit(normalized_df)
pca2d = pca2.transform(normalized_df)
plt.figure(figsize = (10,10))
sns.scatterplot(pca2d[:,0], pca2d[:,1], 
                hue=labels_scale, 
                palette='Set1',
                s=100, alpha=0.2).set_title('KMeans Clusters (2) Derived from Original Dataset - Found Label', fontsize=15)
plt.legend()
plt.ylabel('PC2')
plt.xlabel('PC1')
plt.savefig("clustering_pca_fl.png")

# realiza um pca dos clusters encontrados e plota com os labels originais
pca2 = PCA(n_components=3).fit(normalized_df)
pca2d = pca2.transform(normalized_df)
plt.figure(figsize = (10,10))
sns.scatterplot(pca2d[:,0], pca2d[:,1], 
                hue=labels, 
                palette='Set1',
                s=100, alpha=0.2).set_title('KMeans Clusters (2) Derived from Original Dataset - Original Label', fontsize=15)
plt.legend()
plt.ylabel('PC2')
plt.xlabel('PC1')
plt.savefig("clustering_pca_ol.png")
