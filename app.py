import os
import subprocess
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

DEMO_FOLDER = "data/demo_calls"
ONBOARDING_FOLDER = "data/onboarding_calls"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload_files():

    demo = request.files["demo"]
    onboarding = request.files["onboarding"]

    if demo:
        demo.save(os.path.join(DEMO_FOLDER, demo.filename))

    if onboarding:
        onboarding.save(os.path.join(ONBOARDING_FOLDER, onboarding.filename))

    subprocess.run(["python", "scripts/run_pipeline.py"])

    return redirect("/outputs")


@app.route("/outputs")
def outputs():

    accounts_path = "outputs/accounts"

    accounts = os.listdir(accounts_path) if os.path.exists(accounts_path) else []

    return render_template("index.html", accounts=accounts)


if __name__ == "__main__":
    app.run(debug=True)
