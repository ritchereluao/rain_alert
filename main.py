import requests
from twilio.rest import Client

OWM_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = ""
account_sid = ""
auth_token = ""

weather_params = {
    "lat": 1,
    "lon": 123,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(url=OWM_endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

# weather_twelve_hours = weather_data["hourly"][slice(12)]
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
        print("It will rain")
    # else:
    #     weather_description = hour_data["weather"][0]["description"]
    #     print(weather_description)

if will_rain:
    client = Client(account_sid, auth_token)
    numbers = ["+", "+", "+"]
    for each_number in numbers:
        message = client.messages \
            .create(
                body="It's going to rain today. Remember to bring an ☔️",
                from_="+",
                to=each_number
            )

print(message.status)
