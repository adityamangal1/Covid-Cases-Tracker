import datetime  # for reading present date
from time import sleep
import requests  # for retreiving coronavirus data from web
from plyer import notification  # for getting notification on your PC
from termcolor import cprint
# let there is no data initially
covidData = None
cprint("#"*40, 'yellow')
cprint("Covid Cases Tracker".center(40), 'red')
cprint("#"*40, 'yellow')
sleep(2)
cprint("Fetching data....", 'yellow')
sleep(1)

try:
    covidData = requests.get("https://corona-rest-api.herokuapp.com/Api/india")
    # print(covidData)

except:
    # if the data is not fetched due to lack of internet
    cprint("Please! Check your internet connection", 'blue')
# if we fetched data
if (covidData != None):
    # converting data into JSON format
    data = covidData.json()['Success']


    # repeating the loop for multiple times
    while(True):
        notification.notify(
            # title of the notification,
            title="COVID19 Stats on {}".format(datetime.date.today()),
            # the body of the notification
            message="Total cases : {totalcases}\nToday cases : {todaycases}\nToday deaths :{todaydeaths}\nTotal active :{active}".format(
                totalcases=data['cases'],
                todaycases=data['todayCases'],
                todaydeaths=data['todayDeaths'],
                active=data["active"]),
            app_icon='icon.ico',
            # the notification stays for 50sec
            timeout=50
        )
        # sleep for 4 hrs => 60*60*4 sec
        # notification repeats after every 4hrs
        sleep(60*60*4)
