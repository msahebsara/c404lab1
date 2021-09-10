import requests 

print(requests.__version__)

print(requests.get("http://www.google.com/").text)

print(requests.get("https://raw.githubusercontent.com/msahebsara/c404lab1/master/script.py").text)