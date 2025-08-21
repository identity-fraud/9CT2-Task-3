import pandas as pd
import matplotlib.pyplot as plt

def internet_users_graph(kind):
    internet_users = pd.read_csv('Data/percent-of-internet-users.csv') 
    internet_users.plot(
    kind=kind,
    x='Year',
    y='Percentage of people using the internet in Australia',
    color='blue',
    alpha=0.3,
    title='Number of Internet users in Australia every year',
    yticks=(0,5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100),
    xticks =(1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025)
    )
    plt.show()

def mental_disorders_graph(kind):

    mental_disorders = pd.read_csv('Data/percent-of-mental-disorders.csv')
    mental_disorders['val'] = mental_disorders['val'] * 100
    mental_disorders.plot(
    kind=kind,
    x='Year',
    y='Percentage of people with mental disorders in Australia',
    color='blue',
    alpha=0.3,
    title='Percent of mental disorders in Australia',
    xticks =(1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025)
    )
    plt.show()

def internet_users_dataset(year):
    internet_users = pd.read_csv('Data/percent-of-internet-users.csv')

    if year == "":
        print(internet_users)
        return
    
    try:
        year = int(year)
    except ValueError:
        print('Incorrect input, select a year from 1990-2020')
        return

    filtered = internet_users.loc[internet_users['Year'] == year]

    if not filtered.empty:
        print(f"\nInternet usage data for the year {year}:")
        print(filtered) 
    
    else:
        print(f"\nNo data found for the year {year}.")

    
def mental_disorders_dataset(year):
    mental_disorders = pd.read_csv('Data/percent-of-mental-disorders.csv')
    if year == "":
        print(mental_disorders)
    
    try:
        year = int(year)
    except ValueError:
        print('Incorrect input, select a year from 1990-2020')
        return

    filtered = mental_disorders.loc[mental_disorders['Year'] == year]

    if not filtered.empty:
        print(f"\nMental disorder data for the year {year}:")
        print(filtered) 
    
    if filtered.empty:
        print(mental_disorders)
    else:
        print(f"\nNo data found for the year {year}.")

