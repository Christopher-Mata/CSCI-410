### This is for the 1st Challenge Activity (Removing Duplicates)
# Import packages and functions
import pandas as pd

# Load the dataset
healthy = pd.read_csv('healthy_example.csv')

# Remove instances with duplicate values of life_expectancy 
healthyClean = healthy.drop_duplicates(subset='life_expectancy')

healthyClean.info()

### This is for the 2nd Challenge Activity (Removing Missing Values)
# Import packages and functions
import pandas as pd

# Load the dataset
lifestyle = pd.read_csv('lifestyle_example.csv')

# Remove instances with missing values of annual_hours_worked
lifestyleClean = lifestyle.dropna(subset=['annual_hours_worked'])

lifestyleClean.info()

### This is for the 3rd Challenge Activity (Replacing Missing Values with Mean)
# Import packages and functions
import pandas as pd

# Load the dataset
lifestyle = pd.read_csv('lifestyle_example.csv')

# Calculate the mean values of the features
lifestyleMean = lifestyle.mean(numeric_only=True)
print('Mean:', lifestyleMean['outdoor_activities'], '\n')

# Replace missing values of outdoor_activities in place with the mean of outdoor_activities
lifestyle['outdoor_activities'].fillna(lifestyleMean['outdoor_activities'], inplace=True)

print(lifestyle['outdoor_activities'])