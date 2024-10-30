import requests

response = requests.get('https://api.openweathermap.org/data/2.5/weather?lat=4.2105&lon=101.9758&appid=92f67a0ed9dea38cf4be54a417b77fe6')
print(response.json())
