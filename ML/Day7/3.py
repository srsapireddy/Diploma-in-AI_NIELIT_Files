import pandas as pd
data=pd.read_csv("banking.csv",delimiter=",")
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()

secondCol=data['job']

le.fit(secondCol)
newCol=le.transform(secondCol)
print(newCol)
