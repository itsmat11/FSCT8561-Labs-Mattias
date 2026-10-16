
import requests


# Part C1: Set up the local Juice Shop target

base_url = "http://localhost:3000"
search_url = base_url + "/rest/products/search"


# Part C1: Test reflected input using a harmless marker

marker = "fsct8561-marker-123"

marker_response = requests.get(
    search_url,
    params={"q": marker},
    timeout=5
)

print("=== Part C1: Reflected Input Test ===")

if marker in marker_response.text:
    print("Marker appears in the response - investigate its context")
else:
    print("Marker was not found in this response")


# Part C1 Practice H: Test non-executable HTML input

html_input = "<u>fsct8561-test</u>"

html_response = requests.get(
    search_url,
    params={"q": html_input},
    timeout=5
)

print()
print("=== Part C1: HTML Input Test ===")

if html_input in html_response.text:
    print("HTML input appears unchanged in the response")
else:
    print("HTML input was not found unchanged in the response")


# Part C2: Compare normal input with SQL syntax probe

print()
print("=== Part C2: SQL Injection Indicators ===")

normal_input = "apple"
probe_input = "'"

normal = requests.get(
    search_url,
    params={"q": normal_input},
    timeout=5
)

probe = requests.get(
    search_url,
    params={"q": probe_input},
    timeout=5
)

print("Normal input status:", normal.status_code)
print("Probe input status:", probe.status_code)

print("Normal response length:", len(normal.content))
print("Probe response length:", len(probe.content))


# Part C3: Check for database error messages

print()
print("=== Part C3: Database Error Check ===")

error_phrase = "SQLITE_ERROR"

if error_phrase.lower() in probe.text.lower():
    print("Database-related error text found; manual review required")
else:
    print("No matching database error text in this response")


# Part C3 Practice J: Check two additional error phrases

other_errors = ["SQL syntax", "database error"]

for error in other_errors:

    if error.lower() in probe.text.lower():
        print("Possible database error found:", error)
    else:
        print("No matching error found for:", error)

# Part C4: Check security response headers

print()
print("=== Part C4: Security Headers ===")

# Get the homepage response

response = requests.get(
    base_url,
    timeout=5
)

# Check for security headers

headers_to_check = [
    "Content-Security-Policy",
    "X-Content-Type-Options"
]

for name in headers_to_check:

    if name in response.headers:
        print(name, "is present")
    else:
        print(name, "is not present; investigate its relevance")


# Part C4 Practice K: Check the Server header

print()
print("=== Part C4: Server Header ===")

server_header = response.headers.get("Server")

print("Server header:", server_header)


# Part C5: Avoid duplicate security alerts

print()
print("=== Part C5: Avoid Duplicate Alerts ===")

alerts = []
seen = set()

for message in [
    "Missing CSP",
    "Missing CSP",
    "Missing X-Content-Type-Options"
]:

    if message not in seen:

        seen.add(message)
        alerts.append(message)


print("Alerts:", alerts)
print("Total unique alerts:", len(alerts))

# Part C6: Write observations to a CSV file

import csv

print()
print("=== Part C6: Save CSV File ===")

practice_records = [
    {"endpoint": "/", "status": 200},
    {"endpoint": "/example", "status": 404}
]

with open("practice_records.csv", "w", newline="", encoding="utf-8") as file:

    writer = csv.DictWriter(
        file,
        fieldnames=["endpoint", "status"]
    )

    writer.writeheader()
    writer.writerows(practice_records)

print("Saved practice_records.csv")
