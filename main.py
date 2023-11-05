### Imports of the program
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

### Global variables
global fileName
fileName = 'data.csv'
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
    data = pd.read_csv('data.csv')
    print(data.head())

    ## describes the data
    print(tag, data.describe())

    ## plots the data
    sns.pairplot(data, hue='species')
    plt.show()

    ## prepares the data for training and analysis
    X = data.drop(['species'], axis=1)
    y = data['species']

### Runs the main function
if __name__ == '__main__':
    main()