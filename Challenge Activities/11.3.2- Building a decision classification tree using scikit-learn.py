### This is for the 1st challenge activity (Decision Trees classification)
# Import packages and functions
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_text  

# Seed random number generator
rng = np.random.RandomState(34)

# Load the dataset
birdOfPrey = pd.read_csv('birdOfPrey_Example.csv') 

# Assign outcome to y and features to X 
y = birdOfPrey['Species']
X = birdOfPrey.drop('Species', axis=1)

# Initialize the model -- decision tree classifier

# Your code goes here
birdOfPreyCT = DecisionTreeClassifier(min_samples_leaf=5, random_state=rng)

# Fit the model
birdOfPreyCT.fit(X,y)

# Print classification tree
print(export_text(birdOfPreyCT, feature_names=X.columns.to_list()))

### This is for the 2nd challenge activity (Decision Trees classification)
# Import packages and functions 
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_text  

# Seed random number generator
rng = np.random.RandomState(48)

# Load the dataset
hawk = pd.read_csv('hawk_Example.csv') 

# Assign outcome to y and features to X 
y = hawk['Species']
X = hawk.drop('Species', axis=1)

# Initialize the model -- decision tree classifier
hawkCT = DecisionTreeClassifier(max_depth=3, min_samples_split=5, min_samples_leaf=1, random_state=rng)

# Fit the model
hawkCT.fit(X,y)
# Your code goes here

# Print classification tree
print(export_text(hawkCT, feature_names=X.columns.to_list()))

### This is for the 3rd challenge activity (Decision Trees classification)
# Import packages and functions
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_text  

# Seed random number generator
rng = np.random.RandomState(25)

# Load the dataset
hawk = pd.read_csv('hawk_Example.csv') 

# Assign outcome to y and features to X 
y = hawk['Species']
X = hawk.drop('Species', axis=1)

# Initialize the model -- decision tree classifier

# Your code goes here
hawkCT =  DecisionTreeClassifier(max_depth=4, min_samples_split=5, min_samples_leaf=7, random_state=rng)

# Fit the model
hawkCT.fit(X,y)

# Print classification tree
print(export_text(hawkCT, feature_names=X.columns.to_list()))