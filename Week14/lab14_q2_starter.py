# Tanzeem Shaikh- 101585484

import urllib.request

# Required security headers
required_headers = [
    "X-Frame-Options",
    "Content-Security-Policy",
    "X-Content-Type-Options",
    "Strict-Transport-Security"
]


# Step 1: Check headers
def check_headers(url):
    try:
        response = urllib.request.urlopen(url)
        headers = dict(response.headers)

        results = {}

        for header in required_headers:
            if header in headers:
                results[header] = True
            else:
                results[header] = False

        return results

    except Exception as e:
        print("Error:", e)
        return None


# Step 2: Generate report
def generate_report(url, results):
    print(f"\n🔍 Checking: {url}")

    for header, present in results.items():
        if present:
            print(f"✓ {header} is present")
        else:
            print(f"✗ {header} is missing")


# 🔹 MAIN
if __name__ == "__main__":
    url = input("Enter website URL: ")

    results = check_headers(url)

    if results:
        generate_report(url, results)