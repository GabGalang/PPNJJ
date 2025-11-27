import requests

url = "https://ula-fumed-steadfastly.ngrok-free.dev/quote"
response = requests.get(url).json()

print(response["quote"])
print(response["author"])