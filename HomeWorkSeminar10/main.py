'''В ячейке ниже представлен код генерирующий DataFrame, которая состоит
всего из 1 столбца. Ваша задача перевести его в one hot вид. 
Сможете ли вы это сделать без get_dummies?
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()
'''

import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

one_hot_data = pd.DataFrame()
unique_values = data['whoAmI'].unique()
for value in unique_values:
    one_hot_data[f'is_{value}'] = (data['whoAmI'] == value).astype(int)
print (one_hot_data.head())