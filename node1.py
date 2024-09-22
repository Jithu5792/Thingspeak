import time
import requests
import random

THINGSPEAK_API_KEY = 'Your API Key'  # Replace with your actual API key
THINGSPEAK_URL = 'https://api.thingspeak.com/update'

def send_data_to_thingspeak(temperature=None, soil=None, voltage=None):
    params = {
        'api_key': THINGSPEAK_API_KEY
    }
    
    # Only include fields that have data to send
    if temperature is not None:
        params['field1'] = temperature
    if soil is not None:
        params['field2'] = soil
    if voltage is not None:
        params['field3'] = voltage

    response = requests.get(THINGSPEAK_URL, params=params)
    print(f"Response: {response.text}")

# Counter for the number of data entries
temperature_count = 0
soil_count = 0
voltage_count = 0

# Timestamps for controlling the timing
start_time = time.time()
last_temperature_time = start_time
last_soil_time = start_time
last_voltage_time = start_time

# We want 15 entries for each data type
while temperature_count < 15 or soil_count < 15 or voltage_count < 15:
    current_time = time.time()

    # Send Temperature every 30 seconds (if still under 15 entries)
    if current_time - last_temperature_time >= 30 and temperature_count < 15:
        temperature = random.uniform(20, 35)  # Random temperature between 20°C and 35°C
        send_data_to_thingspeak(temperature=temperature)
        print(f"Temperature Sent: {temperature:.2f}°C")
        last_temperature_time = current_time
        temperature_count += 1

    # Send Soil Moisture every 25 seconds (if still under 15 entries)
    if current_time - last_soil_time >= 25 and soil_count < 15:
        soil = random.uniform(30, 80)  # Random soil moisture between 30% and 80%
        send_data_to_thingspeak(soil=soil)
        print(f"Soil Moisture Sent: {soil:.2f}%")
        last_soil_time = current_time
        soil_count += 1

    # Send Analog Voltage every 20 seconds (if still under 15 entries)
    if current_time - last_voltage_time >= 20 and voltage_count < 15:
        voltage = random.uniform(2.5, 5.0)  # Random voltage between 2.5V and 5.0V
        send_data_to_thingspeak(voltage=voltage)
        print(f"Voltage Sent: {voltage:.2f}V")
        last_voltage_time = current_time
        voltage_count += 1

    # Wait for a second before checking again
    time.sleep(1)
