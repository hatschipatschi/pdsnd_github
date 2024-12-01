# -*- coding: utf-8 -*-
"""

Udacity - Python Project

"""

import time
import pandas as pd
import sys


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }



city_keys=", ".join(str(city.title()) for city in CITY_DATA)


months= {0: 'all',
         1: 'january',
         2: 'february',
         3: 'march',
         4: 'april',
         5: 'mai',
         6: 'june'}

month_dict=", ".join((f"{key}: {value.title()}" for key, value in months.items()))


days={0: 'all',
      1: 'monday',
      2: 'thuesday',
      3: 'wednesday',
      4: 'thursday',
      5: 'friday',
      6: 'saturday',
      7: 'sunday'}

days_dict=", ".join((f"{key}: {value.title()}" for key, value in days.items()))


#def get_filters(city, month, day):
def get_filters():
#def get_filters(city='', month='', day=''):
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    
    print('#'*40+'\n')
    print('Hello! Let\'s explore some US bikeshare data!\n')
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
    
            city=str(input('You have the data of the following cities available. '+ 
                           'Please choose one of those cities:\n{}\n'.format(city_keys.title())))
            if city.lower() in CITY_DATA.keys():
                print('\nYou have chosen {}\n'.format(city).title())
                
            else:
    
                print('\n--This dataset is not available, please try again.--\n')
                continue
            break
        
        except ValueError:
            print('\n--Please enter the name of the city.--\n')
            
        except KeyboardInterrupt:
            print('\n--Programm is closed. See you soon!--\n')
            sys.exit(0)


    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        try:
            print('Please choose a month by typing in the corresponding number.\n{}\n'.format(month_dict))
            month=int(input())
            if month in months.keys():
                print('\nYou have chosen {}.\n'.format(months.get(month).title()))
            else:
                print('\n--This data is not available, please try again.--\n')
                continue
            break
        
        except ValueError:
            print('\n--Please enter an integer.--\n')
        except KeyboardInterrupt:
            print('\n--Programm is closed. See you soon!--\n')
            sys.exit(0)
                          
            
    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)  
    while True:
        try:
            print('Please  choose a day of the week by typing in the corresponding number.\n{}\n'.format((days_dict)))
            day=int(input())
            if day in days.keys():
                print('\nYou have chosen {}.\n'.format(days.get(day).title()))
            else:
                print('\n--This data is not available, please try again.--\n')
                continue
            break
        except ValueError:
            print('\n--Please enter an integer.--\n')
        except KeyboardInterrupt:
            print('\n--Programm is closed. See you soon!--\n')
            sys.exit(0)
                    

    print('-'*40+'\n')
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    #load data
    df=pd.read_csv('all-project-files/'+CITY_DATA.get(city.lower()))
    
    #Convert the 'Start Time' column
    df['Start Time']=pd.to_datetime(df['Start Time'])
    
    #Adding a 'Month' column
    df['Month']=df['Start Time'].dt.month
    
    #Adding a 'Day column. weekday +1 to aline the value to the dictionary key
    df['Day']=df['Start Time'].dt.weekday+1    

    #Adding an 'hour' column
    df['Hour']=df['Start Time'].dt.hour

    #Filter the data if not 'all' selected
    if month > 0 :
        df=df[df['Month']==month]
              
    if day > 0 :
        df=df[df['Day']== day]
    
    df['Route']=df[['Start Station', 'End Station']].agg(' to '.join, axis=1)
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month=df['Month'].mode()[0]
    print('The most common month is {}.'.format(months.get(most_common_month)))
    
    # TO DO: display the most common day of week
    most_common_day = df['Day'].mode()[0]
    print('The most common day is {}.'.format(days.get(most_common_day)))

    # TO DO: display the most common start hour
    most_common_hour = df['Hour'].mode()[0]
    print('The most common hour is {} o\'clock.'.format(most_common_hour))

    print("\nThis took %s seconds.\n" % round((time.time() - start_time),2))
    print('-'*40+'\n')


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station=df['Start Station'].mode()[0]
    print('Most commonly used start station: {}'.format(most_common_start_station))

    # TO DO: display most commonly used end station
    most_common_end_station=df['End Station'].mode()[0]
    print('Most commonly used end station: {}'.format(most_common_end_station))
    
    # TO DO: display most frequent combination of start station and end station trip
    most_common_route=df['Route'].mode()[0]
    print('Most commonly used route: {}'.format(most_common_route))

    print("\nThis took %s seconds.\n" % round((time.time() - start_time),2))
    print('-'*40+'\n')


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time=df['Trip Duration'].sum()
    print('Total travel time: {} seconds'.format(round(total_travel_time,2)))

    # TO DO: display mean travel time
    mean_travel_time=df['Trip Duration'].mean()
    print('Mean travel time: {} seconds'.format(round(mean_travel_time,2)))

    print("\nThis took %s seconds.\n" % round((time.time() - start_time),2))
    print('-'*40+'\n')


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types=df['User Type'].value_counts()
    print('The following user types exist:\n{}\n'.format(user_types))

    # If the dataset has a 'gender' column
    if 'Gender' in df.columns:
        # TO DO: Display counts of gender
        user_gender=df['Gender'].value_counts()
        print('The following gender types exist:\n{}\n'.format(user_gender))
    else:
        print('No data available about the gender of the users.\n')
    
    # If the dataset has a 'year column'
    if 'Birth Year'  in df.columns:
        # TO DO: Display earliest, most recent, and most common year of birth
        oldest_year_of_birth=int(df['Birth Year'].min())
        youngest_year_of_birth=int(df['Birth Year'].max())
        most_common_year_of_birth=int(df['Birth Year'].mode()[0])
        print('The oldest user was born in {} and the youngest user was born in {}. The most common birth year is in {}.'.format(oldest_year_of_birth, youngest_year_of_birth, most_common_year_of_birth))
    else:
        print('No data is available about the birth year of the users.\n')
    print("\nThis took %s seconds.\n" % round((time.time() - start_time),2))
    print('-'*40+'\n')
    
    
def display_raw_data(df):
    """ Disyplay 5 rows of the raw data files """
    i = 0
    raw = input("Would you like to see the content of the raw data file? Choose yes or no.\n").lower() 
    pd.set_option('display.max_columns',200)
    
    while True:            
        if raw == 'no':
            break
        elif raw == 'yes':
            print(df.iloc[i:(i+5)],['Start Time', 'End Time', 'Trip Duration', 'Route', 'User Type'])
            raw = input("\nWould you like to see 5 more rows?\n").lower() 
            i += 5
        else:
            raw = input("\n--Your input is invalid. Please enter only 'yes' or 'no'--\n").lower()


def main():
    while True:
       city, month, day = get_filters()
       df = load_data(city, month, day)

       time_stats(df)
       station_stats(df)
       trip_duration_stats(df)
       user_stats(df)
       display_raw_data(df)

       restart = input('\nWould you like to restart? Enter yes or no.\n')
       if restart.lower() != 'yes' or restart.title() != 'Yes' or restart.upper() !='YES':
            break


if __name__ == "__main__":
	main()

