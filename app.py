# app.py
from flask import Flask, render_template, request
from github_api import fetch_github_user, fetch_user_repos
from analyzer import analyze_user_data

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        username = request.form.get("username")
        user_data = fetch_github_user(username)
        repos_data = fetch_user_repos(username)
        analysis = analyze_user_data(user_data, repos_data)
        if analysis:
            return render_template("result.html", analysis=analysis)
        else:
            return render_template("index.html", error="User not found")
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
