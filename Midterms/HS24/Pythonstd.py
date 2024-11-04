from urllib import parse
import urllib

def encode(s):
    return urllib.parse.quote(s, safe='/', encoding=None, errors=None)


print( encode("/El Niño/") )
print( encode("Hello, world!") )