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
    title='Internet Users (%) in Australia',
    yticks=(0,5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100),
    xticks =(1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025)
    )
    plt.show()

def mental_disorders_graph(kind):

    mental_disorders = pd.read_csv('Data/percent-of-mental-disorders.csv')
    mental_disorders['Percentage of people with mental disorders in Australia'] = mental_disorders['Percentage of people with mental disorders in Australia'] * 100
    mental_disorders.plot(
    kind=kind,
    x='Year',
    y='Percentage of people with mental disorders in Australia',
    color='blue',
    alpha=0.3,
    title='Mental Disorders (%) in Australia',
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
    mental_disorders['Percentage of people with mental disorders in Australia'] = mental_disorders['Percentage of people with mental disorders in Australia'] * 100
    if year == "":
        print(mental_disorders)
        return
    
    try:
        year = int(year)
    except ValueError:
        print('Incorrect input, select a year from 1990-2020')
        return

    filtered = mental_disorders.loc[mental_disorders['Year'] == year]

    if not filtered.empty:
        print(f"\nMental disorder data for the year {year}:")
        print(filtered) 

    else:
        print(f"\nNo data found for the year {year}.")

def combined_graphs():
    internet_users = pd.read_csv('Data/percent-of-internet-users.csv')
    mental_disorders = pd.read_csv('Data/percent-of-mental-disorders.csv')
    mental_disorders['Percentage of people with mental disorders in Australia'] = mental_disorders['Percentage of people with mental disorders in Australia'] * 100
    combined = pd.merge(
        mental_disorders[['Year', 'Percentage of people with mental disorders in Australia']],
        internet_users[['Year', 'Percentage of people using the internet in Australia']],
        on='Year'
                        )

    plt.plot(combined['Year'], combined['Percentage of people with mental disorders in Australia'],
                 label='Mental Disorders (%)', color='red', marker='o')
    
    plt.plot(combined['Year'], combined['Percentage of people using the internet in Australia'],
                 label='Internet Users (%)', color='blue', marker='s')
    
    plt.title('Correlation of Mental Disorders and Technology Use')
    plt.xlabel('Year')
    plt.ylabel('Percentage')
    plt.xticks([1990, 1995, 2000, 2005, 2010, 2015, 2020])
    plt.legend()
    plt.grid(True)
    plt.show()


