import requests

city = input("Konsa city? ")
url = "https://wttr.in/" + city + "?format=3"

try:
    response = requests.get(url, timeout=5)
    print(response.text)
except:
    print("Internet check karo ya thodi der baad try karo")