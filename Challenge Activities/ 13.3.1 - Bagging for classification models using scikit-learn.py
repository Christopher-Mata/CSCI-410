# This is for the 1st challenge activity
# Import packages and functions
import numpy as np
import pandas as pd
from sklearn.ensemble import BaggingClassifier

# Load the dataset
data = pd.read_csv('avila.csv').dropna()

# Create input features X and output feature y
X = data[['ic_distance', 'upper', 'lower', 'exploitation', 'rows',
         'modular', 'line_spacing', 'weight', 'peak_num', 
         'modular_line']]
y = data[['class']]

# Initialize the model

# Your code goes here
baggingModel = BaggingClassifier(random_state=10)

# Fit the model
baggingModel = baggingModel.fit(X, np.ravel(y))
baggingModel.score(X, y)

print('Classification accuracy:', baggingModel.score(X, y))

# This is for the 2nd challenge activity
# Import packages and functions
import numpy as np
import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import BaggingClassifier

# Load the dataset
data = pd.read_csv('avila.csv').dropna()

# Create input features X and output feature y
X = data[['ic_distance', 'upper', 'lower', 'exploitation', 'rows',
         'modular', 'line_spacing', 'weight', 'peak_num', 
         'modular_line']]
y = data[['class']]

# Initialize the model
baggingModel = BaggingClassifier(random_state=6, n_estimators=30, base_estimator=GaussianNB())

# Fit the model
baggingModel = baggingModel.fit(X, np.ravel(y))
baggingModel.score(X, y)

print('Classification accuracy:', baggingModel.score(X, y))

# This is for the 3rd challenge activity
# Import packages and functions
import numpy as np
import pandas as pd
from sklearn.ensemble import BaggingClassifier

# Load the dataset
data = pd.read_csv('avila.csv').dropna()

# Create input features X and output feature y
X = data[['ic_distance', 'upper', 'lower', 'exploitation', 'rows',
         'modular', 'line_spacing', 'weight', 'peak_num', 
         'modular_line']]
y = data[['class']]

# Initialize the model
baggingModel = BaggingClassifier(random_state=10)

# Fit the model and calculate predicted probabilities
baggingModel.fit(X, np.ravel(y))
probs = baggingModel.predict_proba(X)


print('Predicted probabilities:', probs)