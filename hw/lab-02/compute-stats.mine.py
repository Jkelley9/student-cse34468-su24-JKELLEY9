# compute-stats.mine.py : Compute the speed statistics for the given data
#
# Name: Lewin Kelley
# E-Mail: jkelley9@nd.edu
#

# Import numpy which is a well-supported, well-used numerical support library
# for computing various statistics and mathematical operations. The np refers to
# the name when we wish to access numpy functions
import numpy as np

# Import the requests library which is a simple HTTP library for Python that allows
# for simple web fetches
import requests

# Support for CSV parsing in Python
import csv

def compute_stats(data):
    """
    Compute the statistics for the given data
    :param data: A list of integers
    :return: A dictionary containing the statistics
    """

    # Compute the statistics
    stats = {
        'count' : 0,
        'mean': 0,
        'median': 0,
        'min': 0,
        'max': 0,
        'std': 0
    }

    # Save the number of data points
    stats['count'] = len(data)

    # Compute the mean
    stats['mean'] = np.mean(data)

    # Compute the median
    stats['median'] = np.median(data)
    # Compute the minimum
    stats['min'] = np.min(data)
    # Compute the maximum
    stats['max'] = np.max(data)
    # Compute the standard deviation
    stats['std'] = np.std(data)
    # Return the statistics as a dictionary
    return stats

# Print out the statistics using the dictionary format specified in the 
# compute_stats function
def print_stats(theStatInfo):

    # Print out the number of data points
    print('Count:', round(theStatInfo['count'],2))

    # Print out the mean
    print("Mean:", round(theStatInfo['mean'],2),'mbps')

    # TODO: print out the rest of the information
    print("Median:", round(theStatInfo['median'],2),'mbps')
    print('Minimum:', round(theStatInfo['min'],2),'mbps')
    print('Maximum:', round(theStatInfo['max'],2),'mbps')
    print('Standard Deviation:', round(theStatInfo['std'],2),'mbps')

# Main Code - Do our real work here

# Make a GET request to the website for the content that we want
#
#  Remember the four different files - replace this with the one that you want
#    data-100.csv, data-1k.csv., data-10k.csv, and data-all.csv
#

FetchURL = 'http://ns-mn1.cse.nd.edu/cse34468/lab-02/data-all.csv'
print('Starting the web fetch for ' + FetchURL)

# Get the content and decode it
theWebData = requests.get(FetchURL).content.decode('utf-8')

print('  Web fetch now complete of ' + str(len(theWebData)) + ' bytes')

# Drop this into a dictionary reader as a BIG block of memory
reader = csv.DictReader(theWebData.split('\n'))

# Turn this into a list of dictionaries
csv_dict_list = list(reader)

# Set each of the lists of downlink speeds to be empty

allSpeeds = []
wiredSpeeds = []
wifiSpeeds = []

# Iterate through the big list and figure out what to put where
for theRow in csv_dict_list:
    # Uncomment if you want to see the entire raw row
    #print(theRow)

    # Print out key fields
    #   Note: Make sure to comment this out later since printing out 60k entries, probably
    #         isn't a good idea with data-all.csv
    #print('Interface was ', theRow['interface'], ' and the speed was ', theRow['tput_mbps'], ' Mbps')

    # How do we determine what goes where?
    if theRow['direction']=='downlink':
        if theRow['interface'] == 'eth0':
            wiredSpeeds.append(float(theRow['tput_mbps']))
        if theRow['interface'] == 'wlan0':
            wifiSpeeds.append(float(theRow['tput_mbps']))
    # For now, just put everything into the allSpeeds list.  
    # 
    # Consider: Is there a pre-condition that we need to evaluate such as 
    # direction or interface before blindly placing it here?

    # Wrapping this in float ensures that it is a number (floating point)
        allSpeeds.append(float(theRow['tput_mbps']))

################################################
# Compute the statistics for all data
theStatResult = compute_stats(allSpeeds)
 
# Print the statistics for all data
print('Statistics for all data (Wired and Wireless)')
print_stats(theStatResult)

################################################
# Compute the statistics for the wired data
theStatResult = compute_stats(wiredSpeeds)
# Print the statistics for the wired data
print('\nStatistics for wired data')
print_stats(theStatResult)


################################################
# Compute the statistics for the wireless data
theStatResult = compute_stats(wifiSpeeds)
# Print the statistics for the wireless data
print("\nStatistics for wireless data")
print_stats(theStatResult)



