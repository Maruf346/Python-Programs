import pandas as pd

Data = ({'name': ['alice', 'bob', 'charlie'], 
         'age': [23, 30, 28], 
         'city': ['New York', 'Los Angeles', 'Chicago']})

df = pd.DataFrame(Data)
print(df['name'])
print(df.age)
print(df)

print('\n Age over 25: ')
print(df.query('age > 25'))

print('\n Sort by age in descending order: ')
print(df.sort_values('age', ascending=False))
