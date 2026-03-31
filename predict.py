import pickle
from features import extract_features, explain_url

# Load trained model
model = pickle.load(open("model.pkl", "rb"))

# Ask user for URL
url = input("Enter URL: ")

# Extract features
features = extract_features(url)

# Get phishing probability
prob = model.predict_proba([features])[0][1]
score = round(prob, 3)

# SUSPICIOUS override logic
suspicious_override = (
    any(word in url.lower() for word in ["verify", "update", "confirm"])
    and any(word in url.lower() for word in ["bank", "banking", "finance"])
    and prob >= 0.75
    and not any(word in url.lower() for word in ["login", "reset", "password"])
    and not any(char.isdigit() for char in url)
)

# Final classification
if prob < 0.25:
    print(f"🟢 SAFE — Risk Score: {score}")
elif suspicious_override:
    print(f"🟡 SUSPICIOUS — Risk Score: {score}")
elif prob < 0.75:
    print(f"🟡 SUSPICIOUS — Risk Score: {score}")
else:
    print(f"🔴 PHISHING — Risk Score: {score}")

# EXPLANATIONS
reasons = explain_url(url)
print("\nReasons:")
for r in reasons:
    print(f"- {r}")