import httpx

def scan(subdomains):
    print("[+] Checking which subdomains are alive...")
    results = []
    for sub in subdomains:
        try:
            url = f"http://{sub}"
            r = httpx.get(url, timeout=5)
            if r.status_code:
                results.append({
                    "subdomain": sub,
                    "status_code": r.status_code,
                    "title": r.text[:100].strip().replace('\n', ' ')
                })
        except Exception:
            continue
    print(f"[+] {len(results)} subdomains responded to HTTP")
    return results
