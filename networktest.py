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
    return {"download speed":ul}