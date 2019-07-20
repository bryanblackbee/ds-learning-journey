import pandas as pd
import re

def read_lazada_csv():
    return pd.read_csv('data_train.csv', 
                 names="country,sku_id,title,category_lvl_1,category_lvl_2,category_lvl_3,desc,price,xb".split(','))