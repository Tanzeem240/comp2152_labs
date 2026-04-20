# Tanzeem Shaikh - 101585484
import urllib.request
import json

# Step 1: Make request to API
def make_request(url):
    try:
        response = urllib.request.urlopen(url)

        body = response.read().decode()
        status = response.status
        headers = dict(response.headers)

        return {
            "status": status,
            "headers": headers,
            "body": body
        }

    except Exception as e:
        print("Error:", e)
        return None


# Step 2: Parse JSON
def parse_json(body):
    try:
        return json.loads(body)
    except:
        print("Invalid JSON")
        return None


# Step 3: Check API security info
def check_api_info(response):
    headers = response["headers"]

    print("\n🔍 Security Checks:")

    # Server info
    if "Server" in headers:
        print("⚠ Server exposed:", headers["Server"])
    else:
        print("✓ Server header not exposed")

    # Technology info
    if "X-Powered-By" in headers:
        print("⚠ Technology exposed:", headers["X-Powered-By"])
    else:
        print("✓ No technology info exposed")

    # CORS check
    if "Access-Control-Allow-Origin" in headers:
        if headers["Access-Control-Allow-Origin"] == "*":
            print("⚠ CORS open to all (*)")
        else:
            print("✓ CORS restricted")
    else:
        print("✓ No CORS header")


# 🔹 MAIN
if __name__ == "__main__":
    url = input("Enter API URL: ")

    response = make_request(url)

    if response:
        print("\nStatus Code:", response["status"])

        data = parse_json(response["body"])
        if data:
            print("\nSample Data:", data)

        check_api_info(response)