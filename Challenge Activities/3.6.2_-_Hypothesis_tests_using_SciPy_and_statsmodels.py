### This is for the 1st challenge activity (p and test statistic)
# Import packages and functions
import pandas as pd
from statsmodels.stats.proportion import proportions_ztest

# Load the dataset
trails = pd.read_csv('trails.csv')

x = trails['lowvolume'].value_counts()
n = trails.shape[0]

# Find the test statistic and p-value
test = proportions_ztest(x, n, value=0.30, prop_var=0.3, alternative='smaller')

print('Test statistic:', test[0])
print('p-value:', test[1])

### This is for the 2nd challenge activity (T Distrobution)
# Import packages and functions
import pandas as pd
from scipy.stats import ttest_1samp

# Load the dataset
trails = pd.read_csv('trails.csv')

# Find the test statistic and p-value
test = ttest_1samp(a=trails['volume'], popmean=325, alternative='greater')

print('Test statistic:', test[0])
print('p-value:', test[1])

### This is for the 3rd challenge activity (Two independent samples)
# Import packages and functions
import pandas as pd
from scipy.stats import ttest_ind

# Load the dataset and define groups
trails = pd.read_csv('trails.csv')
group1 = trails[trails['season']=='spring']['volume']
group2 = trails[trails['season']!='spring']['volume']

# Find the test statistic and p-value
test = ttest_ind(a=group1, b=group2, equal_var=False, alternative='two-sided')

print('Test statistic:', test[0])
print('p-value:', test[1])