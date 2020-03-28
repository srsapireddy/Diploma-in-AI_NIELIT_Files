import pandas 
import scipy 
import numpy 
from sklearn.preprocessing import MinMaxScaler,StandardScaler 
#url = "https://archive.ics.uci.edu/ml/machine-learning-databases/pima-indians-diabetes/pima-indians-diabetes.data"
#names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class'] 
dataframe = pandas.read_csv("pimaindians.csv") 
array = dataframe.as_matrix()
  
# separate array into input and output components 
X = array[:,0:8] 
Y = array[:,8] 
scaler = StandardScaler() 
rescaledX = scaler.fit_transform(X) 
  
# summarize transformed data 
numpy.set_printoptions(precision=3) 
print(rescaledX[0:5,:]) 
