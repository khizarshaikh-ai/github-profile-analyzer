import os
from dotenv import load_dotenv

load_dotenv()

GITHUB_API_TOKEN = os.getenv("GITHUB_API_TOKEN")
BASE_URL = "https://api.github.com/users/"
