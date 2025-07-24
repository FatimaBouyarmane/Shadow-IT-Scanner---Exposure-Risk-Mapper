def score(results):
    print("[+] Scoring risk of discovered subdomains...")
    for entry in results:
        score = 0
        if entry["status_code"] in [200, 302]:
            score += 1
        if "admin" in entry["title"].lower():
            score += 2
        if "login" in entry["title"].lower():
            score += 2
        entry["risk_score"] = score
        if score >= 4:
            entry["risk_level"] = "High"
        elif score >= 2:
            entry["risk_level"] = "Medium"
        else:
            entry["risk_level"] = "Low"
    return results
