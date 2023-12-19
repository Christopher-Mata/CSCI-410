### This is for the 1st Challenge Activity (Merging)
# Import packages
import pandas as pd

# Load the first dataset
mdataLeft = pd.read_csv('mammals_append_left.csv')

# Load the second dataset
mdataRight = pd.read_csv('mammals_append_right.csv')

# Join the first and second datasets using the parameters how='right' and sort=True
enriched = mdataLeft.merge(mdataRight, how='right', sort=True)

# Print enriched dataframe
print(enriched)

### This is for the 2nd Challenge Activity (Concattenating)
# Import packages
import pandas as pd

# Load the first dataset
animalsLeft = pd.read_csv('mammals_append_left.csv')

# Load the second dataset
animalsRight = pd.read_csv('mammals_append_right.csv')

# Join the first and second datasets using the parameter join='outer'
enriched = pd.concat([animalsLeft, animalsRight], join='outer')

# Print enriched dataframe
print(enriched)