import json

with open('weather.json')as f:
    data = json.load(f)

current_temp = data['main']['temperature']
humidity = data['main']['humidity']
desc = data['weather'][0]['description']

print(f"Current temperature is:{current_temp}C")
print(f"Current humidity level is {humidity}")
print(f"weather Description is: {desc}")
