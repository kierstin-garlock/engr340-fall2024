import sys

import numpy as np
import pandas as pd

def parse_nyt_data(file_path=''):
    """
    Parse the NYT covid database and return a list of tuples. Each tuple describes one entry in the source data set.
    Date: the day on which the record was taken in YYYY-MM-DD format
    County: the county name within the State
    State: the US state for the entry
    Cases: the cumulative number of COVID-19 cases reported in that locality
    Deaths: the cumulative number of COVID-19 death in the locality

    :param file_path: Path to data file
    :return: A List of tuples containing (date, county, state, cases, deaths) information
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
            entry = (date,county,state, int(cases), int(deaths))
        except ValueError:
            print('Invalid parse of ', entry)

        # place entries as tuple into list
        data.append(entry)


    return data

def first_question(data):
    """
    # Write code to address the following question: Use print() to display your responses.
    # When was the first positive COVID case in Rockingham County?
    # When was the first positive COVID case in Harrisonburg?
    :return:
    """

    # your code here
    # load data as a data frame
    df = pd.DataFrame(data, columns = ['date', 'county', 'state', 'cases', 'deaths'])

    # Select data by state and county for Rockingham and Harrisonburg using '&' as referenced in the Python Date
    # Science Handbook under chapter 3 data manipulation with pandas data indexing and selection
    rockingham_data = df[(df['state'] == 'Virginia') & (df['county'] == 'Rockingham')]
    harrisonburg_data = df[(df['state'] == 'Virginia') & (df['county'] == 'Harrisonburg city')]


    # Find the first positive COVID case in Rockingham and Harrisonburg using the .min() function which is referenced in the
    # pandas cheat sheet
    first_rh = rockingham_data['date'].min()
    first_hburg = harrisonburg_data['date'].min()

    # print out the answer to the first question as a string
    print('The first positive Covid Case in Rockingham County was on ' + str(first_rh))
    print('The first positive Covid Case in Harrisonburg City was on ' + str(first_hburg))

    return

def second_question(data):
    """
    # Write code to address the following question: Use print() to display your responses.
    # What day was the greatest number of new daily cases recorded in Harrisonburg?
    # What day was the greatest number of new daily cases recorded in Rockingham County?
    :return:
    """

    # your code here
    # load data as a data frame
    df = pd.DataFrame(data, columns=['date', 'county', 'state', 'cases', 'deaths'])

    # Select data by state and county for Rockingham and Harrisonburg and put data into NumPy to analyze
    rockingham_data = df[(df['state'] == 'Virginia') & (df['county'] == 'Rockingham')].to_numpy()
    harrisonburg_data = df[(df['state'] == 'Virginia') & (df['county'] == 'Harrisonburg city')].to_numpy()

    # Select just the cumulating cases data from each data set using slicing
    cases_rh = rockingham_data[:, 3]
    cases_hb = harrisonburg_data[:,3]

    # Create a variable for each data set to hold the daily cases from each county
    daily_cases_rh = []
    daily_cases_hb = []

    # use a for loop to iterate through the cases data from rockingham county and return an array with new daily cases
    for c in range(len(cases_rh)):
        if c == 0:
            daily_cases_rh.append(cases_rh[0]) # Append the new list with the first value of the cumulating as they are the same
        elif c not in daily_cases_rh: # Use boolean comparison logic to find the first occurrence of a value in cases
            daily_cases_rh.append(cases_rh[c] - cases_rh[c - 1]) # If first occurrence, append list with calculated daily value
        else:
            daily_cases_rh.append(0) # If not first occurrence, append with a value of zero

    # use argmax() to find the index of the greatest number of new daily cases
    max_daily_cases_rh = np.argmax(daily_cases_rh)

    # use the index of the greatest number of new daily cases to find the corresponding date in rockingham data using slicing
    max_date_rh = rockingham_data[max_daily_cases_rh, 0]

    # repeat steps for harrisonburg data
    for c in range(len(cases_hb)):
        if c == 0:
            daily_cases_hb.append(cases_hb[0])
        elif c not in daily_cases_hb:
            daily_cases_hb.append(cases_hb[c] - cases_hb[c - 1])
        else:
            daily_cases_hb.append(0)
    max_daily_cases_hb = np.argmax(daily_cases_hb)
    max_date_hb = harrisonburg_data[max_daily_cases_hb, 0]

    # print the greatest number of new daily cases for both rockingham and harrisonburg and use str() for the dates
    print('The day the greatest number of new daily cases recorded in Rockingham County was on ' + str(max_date_rh))
    print('The day the greatest number of new daily cases recorded in Harrisonburg City was on ' + str(max_date_hb))

    return

def third_question(data):
    # Write code to address the following question:Use print() to display your responses.
    # What was the worst 7-day period in either the city and county for new COVID cases?
    # This is the 7-day period where the number of new cases was maximal.

    # load data as a data frame
    df = pd.DataFrame(data, columns=['date', 'county', 'state', 'cases', 'deaths'])

    # Select data by state and county for Rockingham and Harrisonburg
    rockingham_data = df[(df['state'] == 'Virginia') & (df['county'] == 'Rockingham')].to_numpy()
    harrisonburg_data = df[(df['state'] == 'Virginia') & (df['county'] == 'Harrisonburg city')].to_numpy()

    # Select just the cumulating cases data from each data set using slicing
    cases_rh = rockingham_data[:, 3]
    cases_hb = harrisonburg_data[:, 3]

    # Create a variable for each data set to hold the daily cases from each county
    daily_cases_rh = []
    daily_cases_hb = []

    # use a for loop to iterate through the cases data from rockingham county and return an array with new daily cases
    for c in range(len(cases_rh)):
        if c == 0:
            daily_cases_rh.append(cases_rh[0]) # Append the new list with the first value of the cumulating as they are the same
        elif c not in daily_cases_rh: # Use boolean comparison logic to find the first occurrence of a value in cases
            daily_cases_rh.append(cases_rh[c] - cases_rh[c - 1]) # If first occurrence, append list with calculated daily value
        else:
            daily_cases_rh.append(0) # If not first occurrence, append with a value of zero
    # use argmax() to find the index of the greatest number of new daily cases then +/- 3 from the index to find a 7-day window
    max_daily_cases_rh = np.argmax(daily_cases_rh)
    lower_rh = max_daily_cases_rh - 3
    upper_rh = max_daily_cases_rh + 3
    # use the index window to find the dates in rockingham data using slicing
    lower_date_rh = rockingham_data[lower_rh, 0]
    upper_date_rh = rockingham_data[upper_rh, 0]

    # repeat steps for harrisonburg data
    for c in range(len(cases_hb)):
        if c == 0:
            daily_cases_hb.append(cases_hb[0])
        elif c not in daily_cases_hb:
            daily_cases_hb.append(cases_hb[c] - cases_hb[c - 1])
        else:
            daily_cases_hb.append(0)
    max_daily_cases_hb = np.argmax(daily_cases_hb)
    lower_hb = max_daily_cases_hb - 3
    upper_hb = max_daily_cases_hb + 3
    lower_date_hb = rockingham_data[lower_hb, 0]
    upper_date_hb = rockingham_data[upper_hb, 0]

    # print the worst 7-day periods
    print('The worst 7-day period for new Covid Cases in Rockingham County was from ' + str(lower_date_rh) + ' to ' + str(upper_date_rh))
    print('The worst 7-day period for new Covid Cases in Harrisonburg was from ' + str(lower_date_hb) + ' to ' + str(upper_date_hb))

    return


if __name__ == "__main__":
    data = parse_nyt_data('us-counties.csv')

    #for (date, county, state, cases, deaths) in data:
        #print('On ', date, ' in ', county, ' ', state, ' there were ', cases, ' cases and ', deaths, ' deaths')


    # write code to address the following question: Use print() to display your responses.
    # When was the first positive COVID case in Rockingham County?
    # When was the first positive COVID case in Harrisonburg?
    first_question(data)


    # write code to address the following question: Use print() to display your responses.
    # What day was the greatest number of new daily cases recorded in Harrisonburg?
    # What day was the greatest number of new daily cases recorded in Rockingham County?
    second_question(data)

    # write code to address the following question:Use print() to display your responses.
    # What was the worst seven day period in either the city and county for new COVID cases?
    # This is the 7-day period where the number of new cases was maximal.
    third_question(data)


