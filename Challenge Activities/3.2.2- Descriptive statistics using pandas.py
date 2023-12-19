### This is for the 1st challenge activity (MEDIAN)
# Import packages and functions
import pandas as pd

housing = pd.read_csv('txhousing.csv')

medianHomes = housing['volume'].median()

print('Median:', medianHomes)

### This is for the 2nd challenge activity (STANDARD DEVIATION)
# Import packages and functions
import pandas as pd

housing = pd.read_csv('txhousing.csv')

stdHomes = housing["sales_price"].std()

print('Standard deviation:', stdHomes)

### This is for the 3rd challenge activity (TABLE OF DISCRIPTIVE MEASURES)
# Import packages and functions
import pandas as pd

housing = pd.read_csv('txhousing.csv')

table = housing['sales'].describe()

print(table)