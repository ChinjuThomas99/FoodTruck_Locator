import requests
import argparse

def get_food_trucks(latitude, longitude):
    response = requests.get(f'http://127.0.0.1:8000/api/foodtrucks/?latitude={latitude}&longitude={longitude}')
    data = response.json()
    for truck in data:
        print(f"Name: {truck['name']}\nDescription: {truck['description']}\nAddress: {truck['address']}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Find food trucks nearby.')
    parser.add_argument('latitude', type=float, help='Latitude of the location')
    parser.add_argument('longitude', type=float, help='Longitude of the location')
    args = parser.parse_args()
    get_food_trucks(args.latitude, args.longitude)
