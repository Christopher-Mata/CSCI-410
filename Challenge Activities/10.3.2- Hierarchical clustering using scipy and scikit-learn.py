### This is for the 1st challenge activity (make a cluster model)
import pandas as pd

from scipy.cluster.hierarchy import linkage
from scipy.spatial.distance import pdist
from sklearn.preprocessing import StandardScaler

wine = pd.read_csv('wine1.csv')

# Calculate a distance matrix with selected variables
X = wine[['pH', 'alcohol']]

scaler = StandardScaler()
X = pd.DataFrame(scaler.fit_transform(X))

# pdist() calculates pairs of distances between each instance in the dataset
dist = pdist(X)

# Your code goes here
clusterModel = linkage(dist, method='centroid', metric='euclidean')

print(clusterModel)

### This is for the 2nd challenge activity (make a cluster model and make a distance matrix)
import pandas as pd

from scipy.cluster.hierarchy import linkage
from scipy.spatial.distance import pdist
from sklearn.preprocessing import StandardScaler

wine = pd.read_csv('wine1.csv')

# Calculate a distance matrix with selected variables
X = wine[['citric_acid', 'density']]

scaler = StandardScaler()
X = pd.DataFrame(scaler.fit_transform(X))

# Your code goes here
clusterModel = linkage(X, method='complete', metric='euclidean')
pdist(X)

print(clusterModel)