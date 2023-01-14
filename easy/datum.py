import pandas as pd

day,month = map(int,input().split())
d = pd.Timestamp(f'2009-{month}-{day}')

print(d.day_name())