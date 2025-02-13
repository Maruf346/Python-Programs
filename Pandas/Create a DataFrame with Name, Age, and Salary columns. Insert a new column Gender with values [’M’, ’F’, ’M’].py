import pandas as pd

Data = ({'name': ['alice', 'bob', 'charlie'], 
         'age': [23, 30, 28], 
         'salary': [30000, 45000, 60000]})

df = pd.DataFrame(Data)
df['Gender'] = ['M', 'F', 'M']

print(df)