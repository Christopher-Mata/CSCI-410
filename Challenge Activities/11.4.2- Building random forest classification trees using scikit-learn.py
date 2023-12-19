### This is for the 1st challenge activity (forest building)
# Import packages and functions
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import export_text  

# Seed random number generator
rng = np.random.RandomState(12)

# Load the dataset
hawk = pd.read_csv('hawk_Example.csv') 

# Assign outcome to y and features to X 
y = hawk['Age']
X = hawk.drop('Age', axis=1)

# Split dataset into training data and testing data
XTrain, XTest, yTrain, yTest = train_test_split(X, y, test_size=.3, random_state=rng)

# Initialize the model -- random forest classification trees
hawkRFC = raptorRFC = RandomForestClassifier(n_estimators=85, max_features='sqrt', criterion='gini', bootstrap=True, random_state=rng)

# Fit the model with training data
hawkRFC = hawkRFC.fit(XTrain, yTrain)

# Print first and last random trees generated in the forest
print('First tree:')
print(export_text(hawkRFC[0], feature_names=X.columns.to_list()))
print('Last tree:')
print(export_text(hawkRFC[85-1], feature_names=X.columns.to_list()))

### This is for the 2nd challenge activity (forest building)
# Import packages and functions
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import export_text  

# Seed random number generator
rng = np.random.RandomState(28)

# Load the dataset
raptor = pd.read_csv('raptor_Example.csv') 

# Assign outcome to y and features to X 
y = raptor['Age']
X = raptor.drop('Age', axis=1)

# Split dataset into training data and testing data
XTrain, XTest, yTrain, yTest = train_test_split(X, y, test_size=.3, random_state=rng)

# Initialize the model -- random forest classifier
raptorRFC = RandomForestClassifier(n_estimators=35, max_features='sqrt', criterion='gini', bootstrap=True, random_state=rng)

# Fit the model with training data

# Your code goes here
raptorRFC.fit(XTrain, yTrain)

# Print first and last random trees generated in the forest
print('First tree:')
print(export_text(raptorRFC[0], feature_names=X.columns.to_list()))
print('Last tree:')
print(export_text(raptorRFC[35-1], feature_names=X.columns.to_list()))

### This is for the 3rd challenge activity (forest building)
# Import packages and functions
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import export_text  

# Seed random number generator
rng = np.random.RandomState(22)

# Load the dataset
birdOfPrey = pd.read_csv('birdOfPrey_Example.csv') 

# Assign outcome to y and features to X 
y = birdOfPrey['Species']
X = birdOfPrey.drop('Species', axis=1)

# Split dataset into training data and testing data
XTrain, XTest, yTrain, yTest = train_test_split(X, y, test_size=0.2, random_state=rng)

# Your code goes here
# Initialize the model -- random forest classifier
birdOfPreyRFC = RandomForestClassifier(n_estimators=11, bootstrap=True, random_state=rng)

# Fit the model with training data
birdOfPreyRFC.fit(XTrain, yTrain)

# Print first and last random trees generated in the forest
print('First tree:')
print(export_text(birdOfPreyRFC[0], feature_names=X.columns.to_list()))
print('Last tree:')
print(export_text(birdOfPreyRFC[11-1], feature_names=X.columns.to_list()))