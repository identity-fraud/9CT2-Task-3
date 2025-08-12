import pandas as pd
import matplotlib.pyplot as plt

def internet_users_graph(kind):
    internet_users = pd.read_csv('Data/percent-of-internet-users.csv') 
    internet_users.plot(
                kind=kind,
                x='Year',
                y='Individuals using the Internet in Australia (%)',
                color='blue',
                alpha=0.3,
                title='Number of Internet users in Australia every year',
                yticks=(0,5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100),
                xticks =(1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025)
                    )

    plt.show()


mental_disorders = pd.read_csv('Data/percent-of-mental-disorders.csv')
