import requests
from requests import get

def getexternalip():
    ip = get('https://api.ipify.org').text
    url = 'http://freegeoip.net/json/'+ip
    return url

def getlocation():
    url = getexternalip()
    locationinfo = requests.get(url)
    locationinfo = locationinfo.json()
    country = locationinfo['country_name']
    city = locationinfo['city']
    return(locationinfo)
