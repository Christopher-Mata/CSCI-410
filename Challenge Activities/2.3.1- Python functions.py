### This is for the 1st challenge activity (Function calling)
# Defines the function findResult
def findResult(x, y):
    result = x - y
    return result

# Prints the output of the function findResult() for x=1 and y=7
print(findResult(1,7))

### This is for the 2st challenge activity (Function calling)
def showTime(year, month, day, hour, minutes):
    print(str(month) + '/' + str(day) + '/' + str(year) + ' ' + str(hour) + ':' + str(minutes))

showTime(year=2021,month=1,day=18,hour=11,minutes=56)

### This is for the 3rd challenge activity (Function define)
# Defines the function show()
def show(u,v = 4, w = 18):
    print(str(w) + '/' + str(u) + '/' + str(v))
    
show(8, 5, 6)
show(v=13, u=2)
show(w=9, u=12)

### This is for the 4th challenge activity (Function Parameters)
# Defines the function subtract
def subtract(x, y):
    result = x - y
    return result

# Defines the function calculation
def calculation(operation, x, y, z):
     return operation(x, y) + z

# Creates an object called diffFirst with value 1
diffFirst = 1

# Creates an object called diffSecond with value 28
diffSecond = 28

# Prints the output of the function calculation() using subtract, diffFirst, diffSecond, and 9 as arguments
print(calculation(subtract, diffFirst, diffSecond, 9))