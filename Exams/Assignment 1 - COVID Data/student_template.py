from datetime import datetime, timedelta
import os
from sqlite3 import Date
import sys

"""
Create a program which will provide answers to the questions posed in the assignment description.
We've provided a function which will parse the NYT covid database file (named "us-counties.csv"); 
however, its correct implementation will be up to you. DO NOT MODIFY THIS FUNCTION.
Your code needs to be successful as well as sufficiently commented/documented to receive full credit.
"""


def parse_nyt_data(file_path=''):
    """
    Parse the NYT covid database and return a list of tuples. Each tuple describes one entry in the source data set.
    Date: the day on which the record was taken in YYYY-MM-DD format
    County: the county name within the State
    State: the US state for the entry
    Cases: the cumulative number of COVID-19 cases reported in that locality
    Deaths: the cumulative number of COVID-19 death in the locality

    :param file_path: Path to data file
    :return: A List of tuples containing (date,county, state, fips, cases, deaths) information

    ____________________ DO NOT MODIFY THIS FUNCTION ___________________
    """
    # data point list
    data=[]

    # open the NYT file path
    try:
        fin = open(file_path)
    except FileNotFoundError:
        print('File ', file_path, ' not found. Exiting!')
        sys.exit(-1)

    # get rid of the headers
    fin.readline()

    # while not done parsing file
    done = False

    # loop and read file
    while not done:
        line = fin.readline()

        if line == '':
            done = True
            continue

        # format is date,county,state,fips,cases,deaths
        (date,county, state, fips, cases, deaths) = line.rstrip().split(",")

        # clean up the data to remove empty entries
        if cases=='':
            cases=0
        if deaths=='':
            deaths=0

        # convert elements into ints
        try:
            entry = (date,county,state, fips, int(cases), int(deaths))
        except ValueError:
            print('Invalid parse of ', entry)

        # place entries as tuple into list
        data.append(entry)


    return data

### YOUR CODE HERE ###

state_var = 'Virginia' #select state to phocus on 
 
 
def daily_new_cases(data, county):#define fxn to phocus on new cases for a specific county
    cumulative = {}
    for (date, cty, state, fips, cases, deaths) in data:
        if cty in (county, county + ' city') and state == state_var:#filter based on state, include cty with city in name so hburg data is not missed
             cumulative[date] = cases
 
    if not cumulative:
        return {}
 
    # take day by day difference
    days = sorted(cumulative)
    current = datetime.fromisoformat(days[0])
    last = datetime.fromisoformat(days[-1])
 
    daily = {}
    previous_total = 0
    while current <= last:
        date_str = current.strftime('%Y-%m-%d')      # match file format 
        total = cumulative.get(date_str, previous_total)   
        daily[date_str] = total - previous_total
        previous_total = total
        current += timedelta(days=1)
    return daily
 
 
## Question 1: first positive case
def first_positive_case(data, county):
    """Return the earliest date with more than 0 cases"""
    daily = daily_new_cases(data, county)
    for date in sorted(daily):
        if daily[date] > 0:
            return date
    return None
 
 
## Question 2: day with the greatest number of new cases
def peak_day(data, county):
    """Return the date with the most new cases"""
    daily = daily_new_cases(data, county)
    best_date = max(daily, key=daily.get)
    return best_date, daily[best_date]
 
 
## Question 3: worst seven-day period
def worst_seven_days(data, county):
    """
    Return (start_date, end_date, total) for the 7 consecutive days with the
    most new cases
    """
    daily = daily_new_cases(data, county)
    dates = sorted(daily)
    max_cases = -1
    worst_period = None
    for i in range(len(dates) - 6):
        seven_day_sum = sum(daily[dates[j]] for j in range(i, i + 7))
        if seven_day_sum > max_cases:
            max_cases = seven_day_sum
            worst_period = (dates[i], dates[i + 6], seven_day_sum)
    return worst_period
 
 
def main():
    csv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'us-counties.csv')
    data = parse_nyt_data(csv_path) 

    for county in ['Harrisonburg', 'Rockingham']:#Call all fxns for each county and print results
        print(f"--- {county} ---")
        print("First positive case:", first_positive_case(data, county))
 
        date, cases = peak_day(data, county)
        print(f"Most new cases in one day: {cases} on {date}")
 
        start, end, total = worst_seven_days(data, county)
        print(f"Worst 7-day period: {start} to {end} ({total} new cases)")
        print()
            
    data = parse_nyt_data(csv_path)
 
if __name__ == '__main__':
    main()
 