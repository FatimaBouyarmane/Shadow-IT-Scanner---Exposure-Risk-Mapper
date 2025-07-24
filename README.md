#  Shadow IT Scanner & Risk Mapper

A simple Python tool that discovers exposed subdomains, checks if they’re online, identifies technologies used, and assigns risk levels. It helps detect forgotten or misconfigured assets (Shadow IT) in any organization.

---

##  Features

- Subdomain enumeration (with fallback)
- Live host detection
- Technology fingerprinting (CMS, frameworks, etc.)
- Risk scoring based on exposure
- Markdown report generation

---

##  Example Use

```bash
python main.py --domain example.com
