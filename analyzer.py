# analyzer.py

def analyze_user_data(user_data, repos_data):
    if not user_data:
        return None

    analysis = {
        "name": user_data.get("name") or "N/A",
        "username": user_data.get("login"),
        "bio": user_data.get("bio") or "No bio",
        "public_repos": user_data.get("public_repos"),
        "followers": user_data.get("followers"),
        "following": user_data.get("following"),
        "total_stars": 0,
        "top_languages": {},
        "profile_score": 0  # new
    }

    language_count = {}
    total_stars = 0

    for repo in repos_data:
        lang = repo.get("language")
        if lang:
            language_count[lang] = language_count.get(lang, 0) + 1
        total_stars += repo.get("stargazers_count", 0)

    # Top 5 languages
    top_langs = sorted(language_count.items(), key=lambda x: x[1], reverse=True)[:5]

    analysis["top_languages"] = dict(top_langs)
    analysis["total_stars"] = total_stars

    # Profile Score Logic (0-100)
    score = 0
    if user_data.get("bio"):
        score += 10
    if analysis["public_repos"] >= 5:
        score += 20
    if analysis["followers"] >= 10:
        score += 20
    if total_stars >= 10:
        score += 20
    if len(top_langs) >= 1:
        score += 10
    if len(top_langs) >= 3:
        score += 20

    analysis["profile_score"] = min(score, 100)
    return analysis
