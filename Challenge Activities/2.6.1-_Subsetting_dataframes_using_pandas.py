### This is for the 1st challenge activity (creating dataframe of distnaces)
# Loads necessary packages
import pandas as pd

# Loads the taxi.csv dataset
taxisNY = pd.read_csv('taxi.csv')

# Subset a column of the taxisNY dataframe by specifying the column name
distance = taxisNY[['distance']]

# Prints the column
print(distance)

### This is for the 2nd challenge activity (using iloc method to subser 15 columns and 10 rows)

# Loads the taxi.csv dataset
taxicabsNY = pd.read_csv('taxi.csv')

# Subset taxicabsNY using the iloc method
df = taxicabsNY.iloc[0:10,0:15]

# Prints the column
print(df)

### This is for the 3rd challenge activity (using loc method to subset after 8 rows and only passangers)
# Loads the taxi.csv dataset
taxicabsNY = pd.read_csv('taxi.csv')

# Subset taxicabsNY by specifying columns and rows using the loc method
df = taxicabsNY.loc[8:, ["passengers"]]

# Prints the column
print(df)

### This is for the 4th challenge activity (create dataframe uisng comaroison operator)
# Loads the taxi.csv dataset
taxicabsNY = pd.read_csv('taxi.csv')

# Subset taxicabsNY using comparison operators
df = taxicabsNY[taxicabsNY['distance'] >= 2]

# Prints the column
print(df)

### This is for the 5th challenge activity (create dataframe uisng comaroison and logical operators)
# Loads the taxi.csv dataset
taxicabsNY = pd.read_csv('taxi.csv')

# Subset taxicabsNY using comparison and logical operators
df = taxicabsNY[(taxicabsNY['pickup_borough'] == 'Queens') & 
((taxicabsNY['dropoff_zone'] == 'Van Cortlandt Village') | 
(taxicabsNY['dropoff_zone'] == 'Lenox Hill East'))]

# Prints the column
print(df)