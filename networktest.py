'''
various network tests 
testing:
doctest.testmod(srewu.networktest, verbose=True, optionflags=doctest.ELLIPSIS)
'''
import importlib
import pip
import socket
import doctest
import docstring

try:
        importlib.import_module('pyspeedtest')
        import pyspeedtest
except ImportError:
        import pip
        pip.main(['install', 'pyspeedtest'])
        import pyspeedtest

def download():
    '''
    this function will test the download speeds from the internet
    >>> download()
    {'download speed': ...
    '''
    st = pyspeedtest.SpeedTest()
    dl = st.download()
    dl = ((dl / 1024)/1024)
    return {'download speed': dl}

def upload():
    '''
    this function will test the upload speeds to the internet
    >>> upload()
    {'upload speed': ...
    '''
    st = pyspeedtest.SpeedTest()
    ul = st.upload()
    ul = ((ul / 1024)/1024)
    return {"upload speed":ul}

def latency():
    '''
    this function will test latency
    >>> latency()
    {'latency': ...
    '''
    st = pyspeedtest.SpeedTest()
    ping = st.ping()
    return {"latency":ping}

def tcp_check(address,port):
    '''
    this function will test tcp connectivity
    >>> tcp_check("google.com", 80)
    {'Connect...
    '''
    import socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((address,port))
    if result == 0:
        return{"Connected":address}
    else:
        return{"Connection Refused/Unavailable":address}