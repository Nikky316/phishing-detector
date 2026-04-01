from flask import Flask, request, render_template, redirect, url_for
import pickle
from features import extract_features, explain_url
import logging
from datetime import datetime

app = Flask(__name__)

# Logging setup
logging.basicConfig(
    filename="logs/requests.log",
    level=logging.INFO,
    format="%(asctime)s — %(message)s"
)

# Load model
model = pickle.load(open("model.pkl", "rb"))

@app.route('/', methods=['GET', 'POST'])
def home():
    # ---- GET request handling ----
    result = request.args.get("result")
    reasons_arg = request.args.get("reasons")
    reasons = reasons_arg.split("|") if reasons_arg else None

    # ---- POST request handling ----
    if request.method == 'POST':
        url = request.form['url']
        features = extract_features(url)

        prob = model.predict_proba([features])[0][1]
        score = round(prob, 3)

        # ---- FIXED: REAL PYTHON OPERATORS ----
        suspicious_override = (
            any(word in url.lower() for word in ["verify", "update", "confirm"])
            and any(word in url.lower() for word in ["bank", "banking", "finance"])
            and prob >= 0.75        # FIXED
            and not any(word in url.lower() for word in ["login", "reset", "password"])
            and not any(char.isdigit() for char in url)
        )

        # ---- FIXED: REAL PYTHON OPERATORS ----
        if prob < 0.25:            # FIXED
            result = f"🟢 SAFE — Risk Score: {score}"
        elif suspicious_override:
            result = f"🟡 SUSPICIOUS — Risk Score: {score}"
        elif prob < 0.75:          # FIXED
            result = f"🟡 SUSPICIOUS — Risk Score: {score}"
        else:
            result = f"🔴 PHISHING — Risk Score: {score}"

        # Explanation list
        reasons = explain_url(url)

        # Logging
        logging.info(f"URL: {url} — Result: {result} — Score: {score}")

        # POST → Redirect → GET (PRG pattern)
        return redirect(url_for(
            "home",
            result=result,
            reasons="|".join(reasons)
        ))

    # ---- Render GET Template ----
    return render_template(
        "index.html",
        result=result,
        reasons=reasons
    )

if __name__ == '__main__':
    app.run(debug=True)