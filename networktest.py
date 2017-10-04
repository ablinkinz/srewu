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
    import socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((address,port))
    if result == 0:
        return{"Connected":address}
    else:
        return{"Connection Refused/Unavailable":address}