import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://agilemanifesto.org/')
except urllib.error.URLError:
    print('O site não está ok')
else:
    print('O site está ok')



