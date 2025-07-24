import httpx
import re

def fingerprint(subdomains_data):
    print("[+] Fingerprinting web technologies...")
    for entry in subdomains_data:
        sub = entry["subdomain"]
        url = f"http://{sub}"
        try:
            r = httpx.get(url, timeout=5, follow_redirects=True)
            headers = r.headers
            html = r.text.lower()

            tech = []

            # Basic detection logic (expandable)
            server = headers.get("server")
            if server:
                tech.append(f"Server: {server}")

            if "wordpress" in html:
                tech.append("WordPress")
            if "drupal" in html:
                tech.append("Drupal")
            if "react" in html or "react-dom" in html:
                tech.append("ReactJS")
            if "angular" in html:
                tech.append("Angular")
            if "vue" in html:
                tech.append("Vue.js")
            if "jquery" in html:
                tech.append("jQuery")
            if re.search(r"/wp-admin", html):
                tech.append("WordPress (admin exposed)")

            entry["technologies"] = tech if tech else ["Unknown"]
        except Exception as e:
            entry["technologies"] = ["Error"]
            entry["fingerprint_error"] = str(e)

    return subdomains_data
