### This is for the 1st challenge activity (Binomial Distrobution)
# Import packages and functions
from scipy.stats import binom

# Set values for n and pi
n = int(input())
pi = float(input())

# Calculate probabilities
# Your code goes here
pEqual = binom.pmf(3, n, pi)
pLess = binom.cdf(3, n, pi)
pGreater = 1 - pLess

# Print probabilities
print('P(X = 3) =', pEqual)
print('P(X <= 3) =', pLess)
print('P(X > 3) =', pGreater)

### This is for the 2nd challenge activity (Normal Distrobution)
# Import packages and functions
from scipy.stats import norm

# Set values for mu and sigma
mu = int(input())
sigma = float(input())

# Calculate probabilities
# Your code goes here
pLess = norm.cdf(-3, mu, sigma) 
pGreater = 1 - pLess

# Print probabilities
print('P(X <= -3) =', pLess)
print('P(X > -3) =', pGreater)

### This is for the 3rd challenge activity (T Distrobution)
# Import packages and functions
from scipy.stats import t

# Set value for df
df = int(input())

# Calculate probabilities
# Your code goes here
pLess = t.cdf(-1.74, df)
pGreater = 1 - pLess

# Print probabilities
print('P(X <= -1.74) =', pLess)
print('P(X > -1.74) =', pGreater)