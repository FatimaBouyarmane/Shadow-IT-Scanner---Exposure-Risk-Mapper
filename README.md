# 🔍 Shadow IT Scanner & Risk Mapper

A Python-based tool to autonomously discover and assess exposed infrastructure (subdomains, ports, technologies) tied to a company domain. Designed for cybersecurity interns or professionals working in environments without a dedicated security team.

## Features

- Subdomain enumeration via `crt.sh`
- Alive check & open port scan using `httpx`
- Technology fingerprinting (optional)
- Basic risk scoring per subdomain
- Generates Markdown risk report

## Requirements

- Python 3.8+
- Internet access
- (Optional) Tools: `subfinder`, `nmap`, `nuclei`, `gowitness`

## Setup

```bash
pip install -r requirements.txt
```

## How use?

```bash
python main.py --domain example.com  
```