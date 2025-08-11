import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def internet_users_line():
    internet_users = pd.read_csv('Data/number-of-internet-users.csv') 
    internet_users.plot(
                kind='line',
                x='Year',
                y='Individuals using the Internet in Australia (%)',
                color='blue',
                alpha=0.3,
                title='Number of Internet users in Australia every year'
                   )

    plt.show()
