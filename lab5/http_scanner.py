
import requests
import csv


# Part D Task 1: Set up the HTTP scanner

BASE_URL = "http://localhost:3000"
TIMEOUT = 5

records = []


# Part D Task 1: Function to record HTTP results

def record_request(endpoint, method, input_data, response):

    record = {
        "endpoint": endpoint,
        "method": method,
        "input": input_data,
        "status_code": response.status_code,
        "response_length": len(response.content),
        "content_type": response.headers.get("Content-Type"),
        "server": response.headers.get("Server")
    }

    records.append(record)

    print()
    print("Endpoint:", record["endpoint"])
    print("Method:", record["method"])
    print("Input:", record["input"])
    print("Status code:", record["status_code"])
    print("Response length:", record["response_length"])
    print("Content type:", record["content_type"])
    print("Server:", record["server"])


print("=== HTTP Scanner ===")


# Part D Task 1: Send a GET request to the homepage

try:
    response = requests.get(
        BASE_URL,
        timeout=TIMEOUT
    )

    record_request(
        "/",
        "GET",
        "",
        response
    )

except requests.RequestException as error:
    print("Homepage request failed:", error)


# Part D Task 1: Test GET requests with search terms

search_url = BASE_URL + "/rest/products/search"

search_terms = ["apple", "banana"]

for term in search_terms:

    try:
        response = requests.get(
            search_url,
            params={"q": term},
            timeout=TIMEOUT
        )

        record_request(
            "/rest/products/search",
            "GET",
            term,
            response
        )

    except requests.RequestException as error:
        print("Search request failed:", error)


# Part D Task 1: Send a POST request to the search endpoint

try:
    response = requests.post(
        search_url,
        data={"q": "apple"},
        timeout=TIMEOUT
    )

    record_request(
        "/rest/products/search",
        "POST",
        "q=apple",
        response
    )

except requests.RequestException as error:
    print("POST request failed:", error)


# Part D Task 1: Save HTTP results to a CSV file

with open("http_scan_results.csv", "w", newline="", encoding="utf-8") as file:

    writer = csv.DictWriter(
        file,
        fieldnames=[
            "endpoint",
            "method",
            "input",
            "status_code",
            "response_length",
            "content_type",
            "server"
        ]
    )

    writer.writeheader()
    writer.writerows(records)


# Part D Task 1: Print the final summary

print()
print("=== HTTP Scan Summary ===")
print("Total successful HTTP responses recorded:", len(records))
print("Results saved to http_scan_results.csv")
print("Scan complete.")
