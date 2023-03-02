# 1
import random, numpy as np, pandas as pd

# 2
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst}) 

# 3
data.head()

# 4
# exaple pd.get_dummies(data)
pd.get_dummies(data)

# 5
# not pd.get_dummies(data)
data['whoAmI_human'] = list(map(int, data['whoAmI'] == 'human'))
data['whoAmI_robot'] = list(map(int, data['whoAmI'] == 'robot'))

# 6
data