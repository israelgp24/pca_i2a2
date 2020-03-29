import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler


data = pd.read_excel('PCA_exercise.xlsx', index_col=0)
data_trans = data.T
sc = StandardScaler()
data_trans_std = sc.fit_transform(data_trans.values)
pca = PCA(n_components=4)
data_trans_pca=pca.fit_transform(data_trans_std)

# PCA scree plot
plt.figure(figsize=(10,5))
plt.bar(
        ['PCA {}'.format(str(i+1)) for i in range(pca.n_components_)], 
        pca.explained_variance_ratio_,
        align='center', 
        label='individual variance'
)
plt.ylabel('variance ratio')
plt.legend()
plt.show()
print('Variance Ratio: ', np.round(pca.explained_variance_ratio_,3))

# Correlation Matrix
plt.figure()
correlation_Matrix = np.corrcoef(data_trans)
objects = ['Object {}'.format(str(i+1)) for i in range(pca.n_components_)]
sns.heatmap(
        correlation_Matrix, 
        vmax=1, 
        square=True,
        annot=True, 
        annot_kws={"fontsize":8}, 
        xticklabels=objects, 
        yticklabels=objects
)  
plt.show()

# Objects in a plane with coordinates PCA 1 and PCA 2 
element_x = []
element_y = []
for i in range(pca.n_components_):
    element_x.append(data_stars_pca[i][0])
    element_y.append(data_stars_pca[i][1])
    
    
plt.scatter(
element_x,
element_y
)
