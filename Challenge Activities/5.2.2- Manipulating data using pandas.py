### This is the 1st challenge problem (requency table)
# Import packages and functions
import pandas as pd

# Load the dataset
df = pd.read_csv('credit_card.csv')

# Create a frequency table for Total_calls_made
freqTable = df.groupby('Total_calls_made').size()

# Display frequency table
print(freqTable)

### This is the 2nd challenge problem (contingency table)
# Import packages and functions
import pandas as pd
import numpy as np

# Load the dataset
df = pd.read_csv('credit_card.csv')

# Create a contingency table for Total_Credit_Cards and Total_visits_online
contingencyTable = df.pivot_table(index='Total_Credit_Cards', columns='Total_visits_online', aggfunc='size')

# Display contingency table
print(contingencyTable)