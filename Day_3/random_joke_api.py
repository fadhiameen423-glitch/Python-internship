import requests
url = "https://official-joke-api.appspot.com/random_joke"
response = requests.get(url)
response.raise_for_status()
joke=response.json()
print(f"Setup: {joke.get('setup')}")
print(f"Punchline: {joke.get('punchline')}")