# fetch-score.py : Retrieve a JSON from a website and parse it to determine the win-loss
#                  record for Notre Dame for the season
#
# Name: Lewin Kelley
# E-Mail: jkelley9@nd.edu
#

import requests

# Make a GET request to the website
response = requests.get("http://ns-mn1.cse.nd.edu/cse34468/hw-01/score.json")

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON data
    data = response.json()

    # Process the JSON data to determine the win-loss record for Notre Dame

    ###################################
    # Your code goes HERE

    # You may delete this line - this is just here to show you that it retrieved the file
    #print(data)

    ################

else:
    print("Failed to retrieve the JSON data")

# Problem 2
nd_wins = 0
nd_lose=0
for ix in range(len(data)):
  if data[ix]["ND"]>data[ix]["Other"]:
     nd_wins+=1
  else:
     nd_lose+=1
print("Notre Dame's record is: "+str(nd_wins)+"-"+str(nd_lose))

