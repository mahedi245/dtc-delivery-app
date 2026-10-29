import pandas as pd
import sys

file_path = r'D:\Zahir\ওয়াডার_ভিজিট_ডেলিভারি_তালিকা-1.xlsx'
try:
    df = pd.read_excel(file_path)
    print('Columns/Headers:')
    print(list(df.columns))
    print('\nFirst 3 rows of data:')
    print(df.head(3).to_string())
except Exception as e:
    print('Error decoding file:', e)
