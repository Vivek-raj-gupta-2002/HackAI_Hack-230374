"""
This file contains API call to get the temperature
"""

# To get the environment variables
from dotenv import load_dotenv
# to make request
from requests import get
import os

load_dotenv()

def getTemp(city_name):
    api_key = os.getenv('API_KEY')
    
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'

    try:
        response=get(url)
        data = response.json()
        return data['main']['temp'] - 273.15
    
    except Exception as error:
        return f'Something Went Wrong'

