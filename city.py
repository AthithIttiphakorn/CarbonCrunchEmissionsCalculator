# from dotenv import load_dotenv #env for env file
# from pprint import pprint
# import requests
# import os
# import json

# load_dotenv()

# def call_city_aqi(city="Bangkok"):
#     request_url = f'http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=5&appid={os.getenv("API_KEY")}'
#     coords = requests.get(request_url).json()

#     global lat
#     global lon
#     lat = coords[0]['lat']
#     lon = coords[0]['lon']
#     print(city, lat, lon)

#     request_city_aqi = f'http://api.openweathermap.org/data/2.5/air_pollution/forecast?lat={lat}&lon={lon}&appid={os.getenv("API_KEY")}'
#     city_aqi = requests.get(request_city_aqi).json()
#     aqi_val = city_aqi["list"][0]["main"]["aqi"]
#     print("AQI value is ", aqi_val)

#    # print(json.dumps(city_aqi, indent=2))
#     return aqi_val

# def historical_temp(city):
#     start = 315507600
#     end = start + 24*60
    
#     temp_l = []

#     for i in range(20):
#         request_temp = f'https://history.openweathermap.org/data/2.5/history/city?lat={lat}&lon={lon}&type=hour&start={start}&end={end}&appid={os.getenv("API_KEY")}'
#         hist_temp = requests.get(request_temp).json()
#         print(hist_temp.keys())
#         print(hist_temp)
#         temp_l.append( hist_temp["message"][0]["main"]["temp"] - 273.15 )
#         print(temp_l)

#         start += 513,000
#         end = start + 24*60
#     print(hist_temp)
