### This is for the 1st challenge activity (Decision Trees)
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeRegressor
from sklearn.tree import export_text

# Seed the random number generator
rng = np.random.RandomState(22)

# Read in the data
hawkExample = pd.read_csv('hawkExample.csv')

# Encode sex as a dummy variable
hawkExampleWithDummy = pd.get_dummies(hawkExample, drop_first=True)

# Assign outcome to y and features to X 
y = hawkExampleWithDummy['Weight']
X = hawkExampleWithDummy.drop('Weight', axis=1)

# Define model
hawkRT = DecisionTreeRegressor(max_depth=2, min_samples_leaf=3, random_state=rng)

# Fit the model
hawkRT.fit(X,y)

# Print regression tree
print(export_text(hawkRT, feature_names=X.columns.to_list()))

### This is for the 2nd challenge activity (Decision Trees fit and creation)
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeRegressor
from sklearn.tree import export_text

# Seed the random number generator
rng = np.random.RandomState(16)

# Read in the data
birdOfPreyExample = pd.read_csv('birdOfPreyExample.csv')

# Encode sex as a dummy variable
birdOfPreyExampleWithDummy = pd.get_dummies(birdOfPreyExample, drop_first=True)

# Assign outcome to y and features to X 
y = birdOfPreyExampleWithDummy['Weight']
X = birdOfPreyExampleWithDummy.drop('Weight', axis=1)

# Initialize the model
birdOfPreyRT = DecisionTreeRegressor(max_depth=3, random_state=rng)

# Fit the model
birdOfPreyRT.fit(X,y)

# Print regression tree info
print('max_depth = ' + str(birdOfPreyRT.max_depth) + ', ' + str(birdOfPreyRT.random_state))

# Print regression tree
print(export_text(birdOfPreyRT, feature_names=X.columns.to_list()))

### This is for the 3rd challenge activity (Decision Trees fit and creation)
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeRegressor
from sklearn.tree import export_text

rng = np.random.RandomState(17)

penguins = pd.read_csv('raptorExample.csv')
penguinsWithDummies = pd.get_dummies(penguins, drop_first=True)

# Assign outcome to y and features to X 

# Your code goes here
y = penguinsWithDummies['Weight']
X = penguinsWithDummies.drop('Weight', axis=1)

# Initialize the model
raptorRT = DecisionTreeRegressor(max_depth=3, min_samples_leaf=2, random_state=rng)

# Fit the model
raptorRT.fit(X, y)

# Print regression tree info
print('max_depth = ' + str(raptorRT.max_depth) + ', ' + str(raptorRT.random_state))

# Print regression tree
print(export_text(raptorRT, feature_names=X.columns.to_list()))