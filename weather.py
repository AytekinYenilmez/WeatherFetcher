import requests


API_KEY = "5ad665fcf01a068ddf6d8a74ada509f7"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"

response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    main = data['main']
    temperature = round(main['temp']  - 273.15, 2)
    humidity = main['humidity']
    pressure = main['pressure']
    weather = data['weather'][0]['description']
    print(f"Weather Details for {city}: ")
    print(f"Temperature: {temperature} celsius")
    print(f"Humidity: {humidity}")
    print(f"Pressure: {pressure}")
    print(f"Weather: {weather}")
else:
    print("Error in fetching data")