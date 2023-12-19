### This is for the 1st challenge activity (fitting a DBSCAN model)
import pandas as pd
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler

wine = pd.read_csv('wine1.csv')

# Create an input matrix with selected features
X = wine[['density', 'fixed_acidity']]

scaler = StandardScaler()
X = pd.DataFrame(scaler.fit_transform(X))

# Cluster using DBSCAN with default options
dbscanModel = DBSCAN()

# Your code goes here
dbscanModel.fit(X)

print(dbscanModel.labels_)

### This is for the 2nd challenge activity (fitting and making a DBSCAN model)
import pandas as pd
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler

wine = pd.read_csv('wine1.csv')

# Create an input matrix with selected features
X = wine[['chlorides', 'fixed_acidity']]

scaler = StandardScaler()
X = pd.DataFrame(scaler.fit_transform(X))

# Your code goes here
dbModel = DBSCAN()
dbModel.fit(X)

print(dbModel.labels_)

### This is for the 3rd challenge activity (fitting and making a DBSCAN model)
import pandas as pd
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler

wine = pd.read_csv('wine1.csv')

# Create an input matrix with selected features
X = wine[['pH', 'sulphates']]

scaler = StandardScaler()
X = pd.DataFrame(scaler.fit_transform(X))

# Your code goes here
dbModel = DBSCAN(eps=0.81, min_samples=5)
dbModel.fit(X)

print(dbModel.labels_)