import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('world-happiness-report-2021.csv')

df_group = df.groupby(['Regional indicator'])

print('*')