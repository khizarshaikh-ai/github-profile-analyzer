# GitHub Profile Analyzer

**A Python tool that analyzes GitHub profiles, shows top languages, total stars, and gives a profile strength score — perfect for developers who want insights at a glance.**

---

## **Table of Contents**
1. [Features](#features)  
2. [Demo](#demo)  
3. [Installation](#installation)  
4. [Usage](#usage)  
5. [Project Structure](#project-structure)  
6. [Technologies Used](#technologies-used)  
7. [Contributing](#contributing)  
8. [License](#license)  

---

## **Features**
- Fetch GitHub user profile info (name, bio, followers, following, public repos)  
- Analyze repositories to find **top languages**  
- Calculate **total stars** across repos  
- Generate a **profile strength score (0–100)**  
- Show **visual 5-star rating** based on profile score  
- Professional and responsive **frontend with Flask, HTML, CSS, JS**  

---

## **Demo**
<img width="1919" height="866" alt="image" src="https://github.com/user-attachments/assets/da63de67-d232-43fd-8683-4086e694e4a4" />

- Homepage: Enter GitHub username
  
<img width="1919" height="876" alt="image" src="https://github.com/user-attachments/assets/4dfe945d-1ff1-4514-bc04-95ab78de13a8" />

- Result page: Profile score, stars, top languages  

---

## **Installation**
1. Clone the repo:
```bash
git clone https://github.com/<your-username>/github-profile-analyzer.git
cd github-profile-analyzer
```
2. Create virtual environment:
```
python -m venv venv
```
3. Activate virtual environment:
```
Windows: venv\Scripts\activate
```
```
Mac/Linux: source venv/bin/activate
```
4. Install dependencies:
```
pip install -r requirements.txt
```
5. Create .env file in project root:
```
GITHUB_API_TOKEN=your_token_here
```
6. Run the app:
```
python app.py
```

Usage

Enter a GitHub username on the homepage

Click Analyze

View:

Profile Strength (0–100)

Total Stars (numeric + 5-star visual)

Top Languages and repo count

Project Structure
```
github-profile-analyzer/
│
├── app.py                 # Main Flask app
├── github_api.py          # GitHub API integration
├── analyzer.py            # Data analysis functions
├── config.py              # API token & settings
├── requirements.txt       # Dependencies
├── .env                   # Hidden API token
├── templates/
│   ├── index.html         # Homepage
│   └── result.html        # Result page
├── static/
│   ├── css/
│   │   └── style.css      # Styling
│   └── js/
│       └── main.js        # Optional JS interactivity
└── README.md              # Project documentation
```

Technologies Used: 
```
Python

Flask

Requests

Python-dotenv

HTML / CSS / JavaScript
```
---
License

MIT License © 2026 Khizar Shaikh

