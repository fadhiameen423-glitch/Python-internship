import requests
url = "https://api.github.com/users/octocat"
response = requests.get(url)
response.raise_for_status()
data=response.json()
print(f"Name: {data.get('name')}")
print(f"Location: {data.get('location')}")
print(f"Public repos: {data.get('public_repos')}")
print(f"Created at: {data.get('created_at')}")
