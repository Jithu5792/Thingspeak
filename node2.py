import time
import requests
import random

THINGSPEAK_API_KEY = ''  # Replace with your actual API key for Node 2
THINGSPEAK_URL = 'https://api.thingspeak.com/update'

def send_data_to_thingspeak(light=None, humidity=None):
    params = {
        'api_key': THINGSPEAK_API_KEY
    }
    
    # Only include fields that have data to send
    if light is not None:
        params['field1'] = light
    if humidity is not None:
        params['field2'] = humidity

    response = requests.get(THINGSPEAK_URL, params=params)
    print(f"Response: {response.text}")

# Counter for the number of data entries
light_count = 0
humidity_count = 0

# Timestamps for controlling the timing
start_time = time.time()
last_light_time = start_time
last_humidity_time = start_time

# We want 15 entries for each data type
while light_count < 15 or humidity_count < 15:
    current_time = time.time()

    # Send Light Intensity every 30 seconds (if still under 15 entries)
    if current_time - last_light_time >= 30 and light_count < 15:
        light = random.uniform(200, 1000)  # Random light intensity between 200 and 1000 lux
        send_data_to_thingspeak(light=light)
        print(f"Light Intensity Sent: {light:.2f} lux")
        last_light_time = current_time
        light_count += 1

    # Send Humidity every 25 seconds (if still under 15 entries)
    if current_time - last_humidity_time >= 25 and humidity_count < 15:
        humidity = random.uniform(40, 70)  # Random humidity between 40% and 70%
        send_data_to_thingspeak(humidity=humidity)
        print(f"Humidity Sent: {humidity:.2f}%")
        last_humidity_time = current_time
        humidity_count += 1

    # Wait for a second before checking again
    time.sleep(1)
