from datetime import datetime
import os

def generate(results, domain):
    os.makedirs("reports", exist_ok=True)
    filename = f"reports/report.md"
    with open(filename, "w") as f:
        f.write(f"# Shadow IT Risk Report – {domain}\n")
        f.write(f"_Generated: {datetime.utcnow()} UTC_\n\n")
        for entry in results:
            f.write(f"### {entry['subdomain']}\n")
            f.write(f"- **Status**: {entry['status_code']}\n")
            f.write(f"- **Title Snippet**: `{entry['title']}`\n")
            f.write(f"- **Risk Level**: `{entry['risk_level']}` (Score: {entry['risk_score']})\n\n")
    print(f"[+] Report saved to {filename}")
