### This is for the 1st challenge Activity (fit K clusters to the data)
import warnings
warnings.filterwarnings("ignore")

import pandas as pd
import numpy as np
from sklearn.cluster import KMeans

# Read in the data
wines = pd.read_csv('whitewine.csv')

# Seed random number generator
rng = np.random.RandomState(28)

# Initialize k-means clustering model
kModel = KMeans(n_clusters=3, random_state=rng)

# Your code goes here
kModel.fit(wines[['density','sulphates']])

print(kModel.cluster_centers_)

### This is for the 2st challenge Activity (fit and create K clusters to the data)
import warnings
warnings.filterwarnings("ignore")

import pandas as pd
import numpy as np
from sklearn.cluster import KMeans

# Read in the data
wines = pd.read_csv('whitewine.csv')

# Seed random number generator
rng = np.random.RandomState(10)

# Your code goes here
kmeansModel = KMeans(n_clusters=4, random_state=rng)
kmeansModel.fit(wines[['chlorides','density']])

print(kmeansModel.labels_[0:5])

### This is for the 3st challenge Activity (fit and create and print K clusters to the data)
import warnings
warnings.filterwarnings("ignore")

import pandas as pd
import numpy as np
from sklearn.cluster import KMeans

# Read in the data
wines = pd.read_csv('whitewine.csv')

# Seed random number generator
rng = np.random.RandomState(11)

# Your code goes here
kmeansModel = KMeans(n_clusters=3, random_state=rng)
kmeansModel.fit(wines[['chlorides','fixed_acidity']])

print(kmeansModel.inertia_)
