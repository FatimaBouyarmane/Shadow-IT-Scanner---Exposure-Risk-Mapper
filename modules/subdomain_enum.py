import requests

def get_subdomains(domain):
    subdomains = set()

    # --- Try crt.sh ---
    print(f"[+] Enumerating subdomains from crt.sh...")
    crtsh_url = f"https://crt.sh/?q=%25.{domain}&output=json"
    try:
        r = requests.get(crtsh_url, timeout=15)
        if r.status_code == 429:
            raise Exception("Rate limited by crt.sh")
        data = r.json()
        for entry in data:
            name = entry['name_value'].lower()
            for sub in name.split('\n'):
                if domain in sub:
                    subdomains.add(sub.strip())
        if subdomains:
            print(f"[+] Found {len(subdomains)} subdomains via crt.sh")
            return list(subdomains)
    except Exception as e:
        print(f"[!] crt.sh failed: {e}")

    # --- Fallback: HackerTarget ---
    print("[+] Trying fallback: HackerTarget API...")
    fallback_url = f"https://api.hackertarget.com/hostsearch/?q={domain}"
    try:
        r = requests.get(fallback_url, timeout=10)
        if "error" in r.text.lower():
            raise Exception("API limit or domain not found")
        lines = r.text.splitlines()
        for line in lines:
            sub = line.split(',')[0].strip()
            if sub and domain in sub:
                subdomains.add(sub)
        print(f"[+] Found {len(subdomains)} subdomains via fallback")
        return list(subdomains)
    except Exception as e:
        print(f"[!] Fallback failed: {e}")

    return []
