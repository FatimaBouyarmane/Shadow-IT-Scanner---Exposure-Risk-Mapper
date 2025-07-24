import httpx
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm

def check_alive(subdomain):
    try:
        url = f"http://{subdomain}"
        r = httpx.get(url, timeout=5)
        if r.status_code < 400:
            return subdomain
    except Exception:
        return None

def scan(subdomains, limit=100, max_threads=20):
    subdomains = subdomains[:limit]
    alive = []

    print(f"[+] Checking up to {limit} subdomains with {max_threads} threads...")
    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        futures = {executor.submit(check_alive, sub): sub for sub in subdomains}

        for f in tqdm(as_completed(futures), total=len(futures), desc="Scanning"):
            result = f.result()
            if result:
                alive.append(result)

    print(f"[+] {len(alive)} subdomains responded to HTTP")
    return alive
