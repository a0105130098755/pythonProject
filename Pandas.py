import numpy as np
import pandas as pd

s1 = pd.Series([10, 20, 30, 40, 50])
print(s1)

s2 = pd.Series(['a', 'b', 'c', 1, 2, 3])
print(s2)

s3 = pd.Series([np.nan, np.nan, np.nan], index=[10, 20, 30])
print(s3)

index_date = ['2024-07-26', '2024-07-27', '2024-07-28', '2024-07-29']
s4 = pd.Series([200, 300, np.nan, 500], index=index_date)
print(s4)

s5 = pd.Series({'국어': 100, '영어': 95, '수학': 50})
print(s5)

df = pd.DataFrame({
    'name': ['민지', '하니', '혜린', '다니엘', '혜인'],
    'kor': [50, 88, 98, 99, 45],
    'eng': [88, 99, 88, 99, 77]
})
print(df['eng'])

print(sum(df['eng']) / df['eng'].size)

df = pd.DataFrame({
    'product': ['apple', 'strawberry', 'watermelon'],
    'price': [1800, 1500, 3000],
    'sales': [24, 38, 13]
})

print(df)

print(f"Average price: {sum(df['price']) / df['price'].size}")
print(f"Average sales: {sum(df['sales']) / df['sales'].size}")
