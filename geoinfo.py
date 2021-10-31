'''
doctest.testmod(srewu.geoinfo, verbose=True, optionflags=doctest.ELLIPSIS)
'''
import requests
from requests import get
import doctest

def getexternalip():
    '''
    getexternalip() will make a call to ipify.org to return the external ip
    >>> getexternalip()
    u'http://...
    '''
    ip = get('https://api.ipify.org').text
    return {"external_ip": ip}

def getlocation():
    '''
    getlocation() will make a call to ipify.org to return the external ip location info
    >>> getlocation()
    {...}
    '''
    ip = get('https://api.ipify.org').text
    url = 'http://ipinfo.io/json?ip='+ip
    locationinfo = requests.get(url)
    locationinfo = locationinfo.json()
    return(locationinfo)
