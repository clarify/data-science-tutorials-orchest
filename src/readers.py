import requests
from models import MeasurementResponse, OpenWeatherCurrentResponse

def read_measurements(**kargs):
    headers = {"accept" : "application/json" }
    url = "https://docs.openaq.org/v2/measurements"
    response = requests.get(url, params = kargs, headers = headers)
    if response.ok:
        results = MeasurementResponse(**response.json()).results
        return results
    return None

def read_openweather_current(**kargs):
    headers = {"accept" : "application/json" }
    url = "http://api.openweathermap.org/data/2.5/weather"
    response = requests.get(url, params = kargs, headers = headers)
    if response.ok:
        results = OpenWeatherCurrentResponse(**response.json())
        return results
    return None