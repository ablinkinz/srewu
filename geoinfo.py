'''
doctest.testmod(srewu.geoinfo, verbose=True, optionflags=doctest.ELLIPSIS)
'''
import requests
from requests import get
import doctest
import docstring

def getexternalip():
    '''
    getexternalip() will make a call to ipify.org to return the external ip
    >>> getexternalip()
    u'http://...
    '''
    ip = get('https://api.ipify.org').text
    url = 'http://freegeoip.net/json/'+ip
    return url

def getlocation():
    '''
    getlocation() will make a call to ipify.org to return the external ip location info
    >>> getlocation()
    {...}
    '''
    url = getexternalip()
    locationinfo = requests.get(url)
    locationinfo = locationinfo.json()
    country = locationinfo['country_name']
    city = locationinfo['city']
    return(locationinfo)
