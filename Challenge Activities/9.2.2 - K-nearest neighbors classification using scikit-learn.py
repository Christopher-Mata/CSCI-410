### This is for the 1st challenge activity (KNN)
# Import packages and functions
import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

# Import dataset
sleep = pd.read_csv('sleep.csv')

# Create input matrix X and output matrix y
X = sleep[['brainwt', 'bodywt']]
y = sleep[['vore']]

# Your code goes here
knnModel = KNeighborsClassifier(n_neighbors=5)
knnModel = knnModel.fit(X, np.ravel(y))

# Print predictions
print(knnModel.predict(X))

### This is for the 2nd challenge activity (KNN fitting)
# Import packages and functions
import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

# Import dataset
sleep = pd.read_csv('sleep.csv')

# Create input matrix X and output matrix y
X = sleep[['awake', 'bodywt']]
y = sleep[['vore']]

knnModel = KNeighborsClassifier(n_neighbors=5)
knnModel.fit(X,np.ravel(y))
# Your code goes here

# Print predictions
print(knnModel.predict(X))

### This is for the 3rd challenge activity (KNN prediction)
# Import packages and functions
import numpy as np
import pandas as pd

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

# Import dataset
sleep = pd.read_csv('sleep.csv')

# Create input matrix X and output matrix y
X = sleep[['bodywt', 'awake']]
y = sleep[['vore']]

knnModel = KNeighborsClassifier(n_neighbors=3)
knnModel = knnModel.fit(X.values, np.ravel(y.values))

# Your code goes here
neighbors = knnModel.kneighbors([[1, 0.5]], return_distance=False)
# Print neighbors
print(neighbors)