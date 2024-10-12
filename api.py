import os
from dotenv import load_dotenv
import requests

load_dotenv()

API_KEY = os.getenv('NASA_API_KEY')

def fetch_mars_photos(rover, sol):
    """Recupera fotos de Marte da API da NASA"""
    url = f'https://api.nasa.gov/mars-photos/api/v1/rovers/{rover}/photos'
    params = {
        'sol': sol,
        'api_key': API_KEY
    }
    response = requests.get(url, params=params)
    response.raise_for_status()

    return response.json().get('photos', [])
