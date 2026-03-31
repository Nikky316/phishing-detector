import re
import urllib.parse

def extract_features(url):
    features = {}
    parsed = urllib.parse.urlparse(url)

    # Feature 1: URL length
    features["url_length"] = len(url)

    # Feature 2: Number of dots
    features["dot_count"] = url.count(".")

    # Feature 3: Has HTTPS
    features["https"] = 1 if url.startswith("https") else 0

    # Feature 4: Contains IP address
    ip_pattern = r"(\d{1,3}\.){3}\d{1,3}"
    features["has_ip"] = 1 if re.search(ip_pattern, url) else 0

    # Feature 5: Hyphens in domain
    features["hyphen_count"] = url.count("-")

    # Feature 6: Suspicious keywords
    suspicious_words = ["login", "verify", "update", "secure", "account", "bank", "free", "alert"]
    features["keyword_flag"] = 1 if any(word in url.lower() for word in suspicious_words) else 0

    # Feature 7: Length of domain
    features["domain_length"] = len(parsed.netloc)

    return list(features.values())

# --------------------------------------------
# ⬇⬇⬇ EXPLAIN FUNCTION BELOW THIS LINE
# --------------------------------------------

def explain_url(url):
    reasons = []

    # Suspicious keywords
    if any(word in url.lower() for word in ["verify", "update", "confirm"]):
        reasons.append("Contains suspicious keyword (verify/update/confirm)")

    # Banking-related terms
    if any(word in url.lower() for word in ["bank", "banking", "finance"]):
        reasons.append("Banking-related term detected")

    # Hyphens
    if "-" in url:
        reasons.append("Hyphens present in domain (phishing indicator)")

    # HTTPS check
    if not url.startswith("https"):
        reasons.append("URL does not use HTTPS (unsecured connection)")

    # IP address detection
    ip_pattern = r"(\d{1,3}\.){3}\d{1,3}"
    if re.search(ip_pattern, url):
        reasons.append("URL contains an IP address")

    # Uncommon TLDs
    uncommon_tlds = [".xyz", ".top", ".support", ".click", ".rest", ".win"]
    if any(url.lower().endswith(tld) for tld in uncommon_tlds):
        reasons.append("Uncommon TLD used (.support, .xyz, etc.)")

    # Long URL
    if len(url) > 60:
        reasons.append("URL is unusually long")

    if len(reasons) == 0:
        reasons.append("No major red flags detected")

    return reasons