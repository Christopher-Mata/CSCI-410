### This is for the 1st challenge activity (2-d array)
# Load the necessary package
import numpy as np

# Create an array
myArray = np.array([[2, 17], [16, 5], [6, 14], [13, 10], [4, 8], [11, 7], [9, 3]])

# Print the array
print(myArray)

# Load necessary package
import numpy as np

### This is for the 2nd challenge activity (2-d array insert column)
# Create array
exArray = [['t', 'h', 'w', 'b', 'r'], ['c', 'p', 'q', 'v', 'n']]

# Insert character into the last column of array
exArray = np.insert(exArray, 5, 'g', axis=1)

# Print the array
print(exArray)

### This is for the 3rd challenge activity (2-d array delete row)
# Load necessary package
import numpy as np

# Create array
myArr = [[6, 1], [5, 2], [7, 9], [8, 4]]

# Delete column 0 of array
myArr = np.delete(myArr, 0, axis=1)

# Print the array
print(myArr)

### This is for the 4th challenge activity (2-d array flatten row-major order)
# Load necessary package
import numpy as np

# Create array
myArr = [[8, 7, 3, 0], [9, 1, 6, 4]]

# Flatten array
myArr = np.ravel(myArr, 'C')

# Print the array
print(myArr)


### This is for the 5th challenge activity (2-d array find sine of array)
# Load necessary package
import numpy as np

# Create array
myArray = [[10, 37, 19, 22, 15, 26, 28], [23, 3, 9, 36, 4, 43, 24]]

# Find sine of array elements
myArray = np.sin(myArray)

# Print the array
print(myArray)