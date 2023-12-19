### This is for the 1st challenge activity (LISTS)
exampleList2 = ['cat', 107]

# Create a list with elements 2, 'c', 18
exampleList1 = [2, 'c', 18]
print(exampleList1)

# Replace the first element with 'p'
exampleList1[0] = 'p'
print(exampleList1)

# Append 25 to the list
exampleList1.append(25)
print(exampleList1)

# Remove the third element from the list
exampleList1.pop(2)
print(exampleList1)

# Combine exampleList1 and exampleList2
combinedList = exampleList1 + exampleList2
print(combinedList)

### This is for the 2nd challenge activity (NAMEDTUPLE)
# Import the namedtuple class
from collections import namedtuple

# Create named tuple type Species with field names 'name', 'order', 'length', and 'legs'
# Your code goes here
Species = namedtuple('Species', ['name', 'order', 'length', 'legs'])

# Create an object of type Species with name = 'robin', order = 'passeriformes', length = 0.25, and legs = 2
# Your code goes here
robin = Species('robin', 'passeriformes', 0.25, 2)

# Print the order element of the robin object
# Your code goes here
print(robin.order)
print(robin)

### This is for the 3rd Challenge (SETS)
# Create a list
exampleList = [33, 1, 109]

# Create the set givenSet
givenSet = {33, 21}

# Convert exampleList to a set
practiceSet = set(exampleList)
print(sorted(practiceSet))

# Remove 1 from the set 
practiceSet.remove(1)
print(sorted(practiceSet))

# Find the union of practiceSet and givenSet
practiceSetUnion = practiceSet.union(givenSet)
print(sorted(practiceSetUnion))

### This is for the 4th challenge (DICTIONARY)
# Create a dictionary with indexes 'robin', 'tuna', and 'iguana', and values 0.25, 1, and 1.5
exampleDict = {'robin': 0.25, 'tuna': 1, 'iguana': 1.5}
print(exampleDict)

# Add an element with key 'muskox' and value 1.1
exampleDict['muskox'] = 1.1
print(exampleDict)

# Remove element with key 'tuna'
del exampleDict['tuna']
print(exampleDict)