### Imports of the program
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

### Global variables
global fileName
fileName = 'data/data.csv'
global tag
tag = ' $ - '

def main():
    """
    Main function of the program
    TODO: Depending on the data, we might need to do a barchart, logchart, histogram, train and perdict to analze the data
    NOTE: This is just a template for the main function, it uses dummy values and wont compile untill the dataSet has been determined
    :return: None
    """

    ## Reads the data and makes sure it is actually loaded
    data = pd.read_csv(fileName)
    print(data.head())
    
    ## Cleans the data, drops the other value in race
    data = data[data["Race"] != "other"]

    ## describes the data
    ## Gets age and victem information
    dataInfo(data)
    
    ## Make box and whisker plot for outlers
    checkOutliers(data)
    
    ## Calls a function to start graphing/plotting the data
    graphData(data)
    
    ## Calls a function to start modeling the data
    modelData(data)
    
    
def checkOutliers(data):
    """
    Graphs the data to check for outliers
    :param data: the data that is being graphed
    :return: None
    """
    sns.boxplot(x=data["Age"])
    sns.boxplot(x=data["Victim Count"])
    
def dataInfo(data):
    print(data.describe())

def graphData(data):
    """
    Graphs the data
    :param data: the data that is being graphed
    :return: None
    """
    
    ## Plots the data for the first Question
    sns.countplot(x='Sex', data=data)

    ## Plots the data for the second Question
    sns.histplot(x='Race', data=data)
    
    ## Plots the data for the fourth Question
    sns.histplot(x='Method', data=data)
    
    ## Additional graphing just to explore the data
    X = data['Age']
    y = data['Victim Count']
    plt.scatter(X, y)
    plt.show()
    
def modelData(data):
    """
    Graphs the data to make the model
    :param data: the data that is being graphed
    :return: None
    """

### Runs the main function
if __name__ == '__main__':
    main()