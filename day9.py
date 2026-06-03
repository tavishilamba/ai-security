# Web scraper for security headers
# Checks if a website has proper security headers configured

import urllib.request

def check_security_headers(url):
    print("=" * 50)
    print(f"SECURITY HEADER CHECKER")
    print(f"Target: {url}")
    print("=" * 50)

    security_headers = [
        "Strict-Transport-Security",
        "X-Content-Type-Options",
        "X-Frame-Options",
        "Content-Security-Policy",
        "X-XSS-Protection"
    ]

    try:
        req = urllib.request.urlopen(url)
        headers = req.headers

        for header in security_headers:
            if header in headers:
                print(f"✓ {header}: {headers[header]}")
            else:
                print(f"✗ {header}: MISSING — vulnerable")

    except Exception as e:
        print(f"Error: {e}")

url = input("Enter website URL (e.g. https://google.com): ")
check_security_headers(url)