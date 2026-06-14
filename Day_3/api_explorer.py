import requests


def fetch_user(username: str) -> dict:
    url = f"https://api.github.com/users/{username}"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException:
        print("Error: Unable to fetch GitHub user data.")

def fetch_joke() -> tuple[str, str]:
    url = "https://official-joke-api.appspot.com/random_joke"

    try:
        response = requests.get(url)
        response.raise_for_status()
        joke = response.json()
        print(f"Setup: {joke.get('setup')}\nPunchline: {joke.get('punchline')}")

    except requests.exceptions.RequestException:
        print("Error: Unable to fetch joke.")

def display_user(user: dict) -> None:
    if not user:
        print("No user data available.")

    print("\nGitHub User Card")
    print("---------------------")
    print("Name         :", user.get("name"))
    print("Location     :", user.get("location"))
    print("Public Repos :", user.get("public_repos"))
    print("Created At   :", user.get("created_at"))
    print("---------------------")

username = input("Enter GitHub username: ")
user = fetch_user(username)
display_user(user)
fetch_joke()
