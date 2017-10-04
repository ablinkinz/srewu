#import pyspeedtest
import importlib
import pip
import socket

try:
        importlib.import_module('pyspeedtest')
        import pyspeedtest
except ImportError:
        import pip
        pip.main(['install', 'pyspeedtest'])
        import pyspeedtest

def download():
    st = pyspeedtest.SpeedTest()
    dl = st.download()
    dl = ((dl / 1024)/1024)
    return {"download speed":dl}

def upload():
    st = pyspeedtest.SpeedTest()
    ul = st.upload()
    ul = ((ul / 1024)/1024)
    return {"upload speed":ul}

def latency():
    st = pyspeedtest.SpeedTest()
    ping = st.ping()
    return {"latency":ping}

def tcp_check(address,port):
    s = socket.socket()
    try:
        s.connect((address,port))
    except Exception as e:
        return("Connection failed to %s:%d. Error message: %s" % (address,port,e))
    finally:
        s.close()