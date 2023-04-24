import urllib2
from googlesearch import search
import requests
import wikipedia
import wolframalpha
import webbrowser
import win32com.client
import time
#My data
from Secure import *

def get_latest_news():
    try:
        news_headlines = []
        res = requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey="+NEWS_API_KEY+"&category=general").json()
        articles=res["articles"]



        for article in articles:
            news_headlines.append(article["title"])

        return news_headlines
    except requests.exceptions.ConnectionError:
        errormsg = "Sorry there is no internet connection"

        return errormsg

def search_on_wikipedia(wiki_query):
    try:
        results = wikipedia.summary(wiki_query, sentences=1)

        return results

    except requests.exceptions.ConnectionError:
        errormsg = "Sorry there is no internet connection"

        return errormsg


def long_search_on_wikipedia(wiki_query):
    try:
        results = wikipedia.summary(wiki_query, sentences=5)

        return results

    except requests.exceptions.ConnectionError:
        errormsg = "Sorry there is no internet connection"

        return errormsg

def get_weather_reports():
    try:
        res = requests.get("https://api.openweathermap.org/data/2.5/find?q=austin&units=imperial&appid="+OPEN_WEATHER_APP_ID).json()

        what_i_need = res["list"]
        for i in what_i_need:
            city_name = what_i_need[0]["name"]
            rain_yesorno = what_i_need[0]["rain"]
            temp = what_i_need[0]["main"]["temp"]
            temp_max = what_i_need[0]["main"]["temp_max"]
            temp_min = what_i_need[0]["main"]["temp_min"]
            humidity = what_i_need[0]["main"]["humidity"]
            feels_like = what_i_need[0]["main"]["feels_like"]

            if rain_yesorno=='None':
                rain_yesorno='There will not be rain today,'
            else:
                rain_yesorno = 'There will be rain today,'

            for j in what_i_need[0]["weather"] :
                weather_main = what_i_need[0]["weather"][0]["main"]
                weather_descrip = what_i_need[0]["weather"][0]["description"]

        s_weather = "For Weather in "+str(city_name)+" "+str(rain_yesorno)+" The temperature is, \n"\
                    +str(temp)+ " degrees Fahrenheit, the max temperature is "+str(temp_max)+" degrees Fahrenheit, the minimum temperature is\n "\
                    +str(temp_min)+" degrees Fahrenheit, it feels like, "+str(feels_like)+" degrees Fahrenheit "" and lastly, the humidity is\n "\
                    +str(humidity)+" RH. In conclusion, the weather is "+weather_main+" and "+str(weather_descrip)+"."



        return s_weather
    except requests.exceptions.ConnectionError:
        errormsg = "Sorry there is no internet connection"

        return errormsg

def get_temperature():
    try:
        res = requests.get(
        "https://api.openweathermap.org/data/2.5/find?q=austin&units=imperial&appid="+OPEN_WEATHER_APP_ID).json()

        what_i_need = res["list"]
        for i in what_i_need:
             city_name = what_i_need[0]["name"]
             rain_yesorno = what_i_need[0]["rain"]
             temp = what_i_need[0]["main"]["temp"]
             temp_max = what_i_need[0]["main"]["temp_max"]
             temp_min = what_i_need[0]["main"]["temp_min"]
             humidity = what_i_need[0]["main"]["humidity"]
             feels_like = what_i_need[0]["main"]["feels_like"]

             if rain_yesorno == 'None':
                 rain_yesorno = 'There will not be rain today,'
             else:
                 rain_yesorno = 'There will be rain today,'

             for j in what_i_need[0]["weather"]:
                 weather_main = what_i_need[0]["weather"][0]["main"]
                 weather_descrip = what_i_need[0]["weather"][0]["description"]

        s_temp = " The temperature is, " +str(temp)+ " degrees Fahrenheit, but it feels like "+str(feels_like)+"degrees Fahrenheit"

        return s_temp
    except requests.exceptions.ConnectionError:
        errormsg = "Sorry there is no internet connection"

        return errormsg

def Wolframalpha(query):
    try:
        client = wolframalpha.Client(WOLFRAM_ID)
        res = client.query(query)
        for pod in res.pods:
            for sub in pod.subpods:
                answer = next(sub.results).text

        return(answer)


    except AttributeError:
        return ("Search could not be found")

def more_Wolframalpha(query):
    try:
        client = wolframalpha.Client(WOLFRAM_ID)
        res = client.query(query)
        for pod in res.pods:
            for sub in pod.subpods:
                return(sub.plaintext)

    except urllib2.URLError:
        return("Could'nt connect, check your connection")


def search_on_google(google_query):

    for gee in search(google_query, tld="co.in", num=1, stop=1, pause=2):
        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"))
        webbrowser.get('chrome').open_new(gee)

def say (saythis):
    speaker = win32com.client.Dispatch("SAPI.SpVoice")

    s = saythis
    speaker.Speak(s)

def timer(wastetime):
    tik1 = time.time()
    toc = time.time()

    time_elapsed = tik1 - toc
    print("Total time elapsed is: ", time_elapsed)

    if time_elapsed>35:
        say(wastetime)

print(get_temperature())