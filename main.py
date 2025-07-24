import argparse
from modules import subdomain_enum, port_scanner, fingerprint, risk_score, reporter

def main():
    parser = argparse.ArgumentParser(description="🔍 Shadow IT Scanner & Risk Mapper")
    parser.add_argument("--domain", required=True, help="Target domain (e.g., example.com)")
    args = parser.parse_args()
    domain = args.domain

    print("="*50)
    print(f"[START] Shadow IT Scan for: {domain}")
    print("="*50)

    # Step 1: Subdomain enumeration
    subdomains = subdomain_enum.get_subdomains(domain)
    if not subdomains:
        print("[!] No subdomains found. Exiting.")
        return

    # Step 2: Port and status scan
    scanned = port_scanner.scan(subdomains)
    if not scanned:
        print("[!] No live subdomains found. Exiting.")
        return

    # Step 3: Fingerprinting
    fingerprinted = fingerprint.fingerprint(scanned)

    # Step 4: Risk scoring
    scored = risk_score.score(fingerprinted)

    # Step 5: Generate report
    reporter.generate(scored, domain)

    print("="*50)
    print("[DONE] Report generated successfully.")
    print("="*50)

if __name__ == "__main__":
    main()
