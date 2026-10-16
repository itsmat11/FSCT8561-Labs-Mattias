
# Part B1: Lists and loops

search_terms = ["apple", "banana", "orange", "lemon"]

for term in search_terms:
    print("Search term:", term)


import requests


# Part B2: Create a dictionary for an HTTP request

base_url = "http://localhost:3000"
search_url = base_url + "/rest/products/search"

r = requests.get(
    search_url,
    params={"q": "apple"},
    timeout=5
)

observation = {
    "method": "GET",
    "endpoint": "/rest/products/search",
    "status_code": r.status_code,
    "response_length": len(r.content),
    "content_type": r.headers.get("Content-Type")
}

print()
print("=== Part B2: Dictionary ===")
print(observation)
print("Status:", observation["status_code"])
print("Content type:", observation["content_type"])


# Part B3: Store multiple HTTP request results

records = []

for term in ["apple", "banana"]:

    result = requests.get(
        search_url,
        params={"q": term},
        timeout=5
    )

    records.append({
        "input": term,
        "status_code": result.status_code,
        "response_length": len(result.content)
    })


print()
print("=== Part B3: List of Records ===")

for record in records:
    print(record)



# Part B4: Create a function to return HTTP status

def get_status(search_word):

    result = requests.get(
        search_url,
        params={"q": search_word},
        timeout=5
    )

    return result.status_code


# Part B4: Test the function with apple and banana

print()
print("=== Part B4: Function ===")

print("Apple status:", get_status("apple"))
print("Banana status:", get_status("banana"))


# Part B5: Handle network errors

print()
print("=== Part B5: Network Error Handling ===")

try:
    test_response = requests.get(
        base_url,
        timeout=5
    )

    print("Connected. Status:", test_response.status_code)

except requests.RequestException as error:
    print("Could not connect:", error)
