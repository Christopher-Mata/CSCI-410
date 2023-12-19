### This is for the 1st challenge activity (make a dataframe and print correlation matrix)
import pandas as pd

wine_table = pd.read_csv('wine_table.csv')

# Your code goes here
X = wine_table[['chlorides', 'free_sulfur_dioxide', 'volatile_acidity', 'density', 'alcohol']]

print(X.corr())

### This is for the 2nd challenge activity (Fitting a PCA model)
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

wines = pd.read_csv('wines.csv')

X = wines[['fixed_acidity', 'residual_sugar', 'free_sulfur_dioxide', 'total_sulfur_dioxide']]

scaler = StandardScaler()
X = pd.DataFrame(scaler.fit_transform(X))

model = PCA(n_components=2)

# Your code goes here
model.fit(X)

print(model.explained_variance_ratio_)

### This is for the 3rd challenge activity (PCA components and calculate loading matrix)
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

wines = pd.read_csv('wines.csv')

X = wines[['citric_acid', 'density', 'fixed_acidity', 'total_sulfur_dioxide']]

scaler = StandardScaler()
X = pd.DataFrame(scaler.fit_transform(X))

model = PCA(n_components=2)

# Your code goes here
model.fit(X)

print(model.components_.T * np.sqrt(model.explained_variance_))
