import pandas as pd
import matplotlib.pyplot as plt

internet_users = pd.read_csv('Data/number-of-internet-users.csv', dtype=str)
internet_users.dropna(inplace=True) 
internet_users.plot(
               kind='scatter',
               x='Year',
               y='Number of Internet users',
               color='blue',
               alpha=0.3,
               title='test'

                   )
plt.show()