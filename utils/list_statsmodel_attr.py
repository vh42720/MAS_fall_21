import pandas as pd
import numpy as np
import statsmodels.api as sm

# A dataframe with two variables
np.random.seed(123)
rows = 12
rng = pd.date_range('1/1/2017', periods=rows, freq='D')
df = pd.DataFrame(np.random.randint(100,150,size=(rows, 2)), columns=['y', 'x'])
df = df.set_index(rng)

x = sm.add_constant(df['x'])
model = sm.OLS(df['y'], x).fit()

for attr in dir(model):
    if not attr.startswith('_'):
        print(attr)