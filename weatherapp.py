import requests
print("------ WEATHER APP ------")
api_key = "dac075e14cdaf79bc98b897e873339bc"
city = input("\nEnter city name: ")
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
response = requests.get(url)
data = response.json()
if data["cod"] == 200:
    city_name = data["name"]
    country = data["sys"]["country"]
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    weather = data["weather"][0]["description"]
    wind = data["wind"]["speed"]
    print("\n------ WEATHER REPORT ------\n")
    print("City:", city_name, ",", country)
    print("Temperature:", temp, "°C")
    print("Humidity:", humidity, "%")
    print("Condition:", weather)
    print("Wind:",wind,"\n")
else:
    print("City not found")

