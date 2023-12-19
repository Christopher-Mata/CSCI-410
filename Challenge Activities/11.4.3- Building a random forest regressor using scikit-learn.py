### This is for the 1st challenge activity (Regresison forest)
# Import packages and functions
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import export_text

# Seed random number generator
rng = np.random.RandomState(41)

# Load the dataset
hawk = pd.read_csv('hawk_Example.csv')

# Assign outcome to y and features to X 
y = hawk['Wing']
X = hawk.drop('Wing', axis=1)
X = pd.get_dummies(X, drop_first=True) # categorical maps to numerical

# Split dataset into training data and testing data
XTrain, XTest, yTrain, yTest = train_test_split(X, y, test_size=.3, random_state=rng)

# Initialize the model -- random forest regression trees
hawkRFR = RandomForestRegressor(n_estimators=87, max_features='sqrt', bootstrap=True, random_state=rng)

# Fit the model with training data
hawkRFR = hawkRFR.fit(XTrain, yTrain)

# Print a random tree generated in the forest
print('Random tree:')
print(export_text(hawkRFR[80], feature_names=X.columns.to_list()))

### This is for the 2nd challenge activity (Regression forest)
# Import packages and functions
# Import packages and functions
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import export_text  

# Seed random number generator
rng = np.random.RandomState(31)

# Load the dataset
hawk = pd.read_csv('hawk_Example.csv') 

# Assign outcome to y and features to X 
y = hawk['Hallux']
X = hawk.drop('Hallux', axis=1)
X = pd.get_dummies(X, drop_first=True) # categorical maps to numerical 

# Split dataset into training data and testing data
XTrain, XTest, yTrain, yTest = train_test_split(X, y, test_size=.3, random_state=rng)

# Initialize the model -- random forest regression trees
hawkRFR = RandomForestRegressor(n_estimators=35, max_features='sqrt', bootstrap=True, max_depth = 4, random_state=rng)

# Fit the model with training data

# Your code goes here
hawkRFR.fit(XTrain, yTrain)
# Print a random tree generated in the forest
print('Random tree:')
print(export_text(hawkRFR[11], feature_names=X.columns.to_list()))

### This is for the 3rd challenge activity (Regression forest)