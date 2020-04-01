# Load libraries
from pandas import read_csv
from pandas.plotting import scatter_matrix
from matplotlib import pyplot


#Loading data
url = "/home/ak/ML projects/flower classification/iris.csv"
names = ['sepal-length','sepal-width','petal=length','petal-width','class']
dataset = read_csv(url,names=names)

#Statistical summary
#print(dataset.describe())
#print(dataset.groupby('class').size())

#Data Visualization
#dataset.plot(kind='box', subplots = True, layout = (2,2), sharex = False, sharey = False)
#dataset.hist()
#scatter_matrix(dataset)
#pyplot.show()

