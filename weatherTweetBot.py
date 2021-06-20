from typing import Text
import tweepy
from bs4 import BeautifulSoup
import requests
def tweetWeather():
    page=requests.get("https://forecast.weather.gov/MapClick.php?lat=41.260680000000036&lon=-95.94025999999997")
    soup=BeautifulSoup(page.content,"html.parser")
    highTempText=soup.find("p",class_="temp temp-high").text
    lowTempText=soup.find("p",class_="temp temp-low").text
    auth = tweepy.OAuthHandler("consumer_key", "consumer_secret")
    auth.set_access_token("key", "secret")
    api=tweepy.API(auth)
    print("Authentication OK")
    api.update_status("The weather today:\n"+highTempText+"\n"+lowTempText+"\nvia National Weather Service")

tweetWeather()
