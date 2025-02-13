import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randint(1, 101, size=(5,2)), columns=['X', 'Y'])

print('Original DataFrame:')
print(df)

print("Sum of X coloumn: ", df['X'].sum())