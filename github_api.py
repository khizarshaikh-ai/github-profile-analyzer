import requests
from config import BASE_URL, GITHUB_API_TOKEN

def fetch_github_user(username):
    headers = {"Authorization": f"token {GITHUB_API_TOKEN}"} if GITHUB_API_TOKEN else {}
    response = requests.get(f"{BASE_URL}{username}", headers=headers)
    if response.status_code == 200:
        return response.json()
    return None

def fetch_user_repos(username):
    headers = {"Authorization": f"token {GITHUB_API_TOKEN}"} if GITHUB_API_TOKEN else {}
    response = requests.get(f"{BASE_URL}{username}/repos", headers=headers)
    if response.status_code == 200:
        return response.json()
    return []
