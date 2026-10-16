
import requests


# Part A1: Send the first HTTP GET request

base_url = "http://localhost:3000"

response = requests.get(base_url, timeout=5)

print("HTTP status:", response.status_code)
print("Response length:", len(response.content), "bytes")


# Part A2: Read response headers and content

print()
print("Content type:", response.headers.get("Content-Type"))

print("First 100 characters:", response.text[:100])


# Part A2: Change 100 to 50 and compare

print()
print("First 50 characters:", response.text[:50])


# Part A3: Send a search parameter using apple

print()
print("=== Search for apple ===")

search_url = base_url + "/rest/products/search"

r = requests.get(
    search_url,
    params={"q": "apple"},
    timeout=5
)

print("Requested URL:", r.url)
print("Status:", r.status_code)
print("Content type:", r.headers.get("Content-Type"))
print("First 150 characters:", r.text[:150])


# Part A3 Practice A: Change search term to banana

print()
print("=== Search for banana ===")

banana_response = requests.get(
    search_url,
    params={"q": "banana"},
    timeout=5
)

print("Requested URL:", banana_response.url)
print("Status:", banana_response.status_code)
print("Content type:", banana_response.headers.get("Content-Type"))
print("First 150 characters:", banana_response.text[:150])


# Part A4: Send a POST request to the search endpoint

print()
print("=== GET vs POST ===")

post_response = requests.post(
    search_url,
    data={"q": "apple"},
    timeout=5
)

print("GET status:", r.status_code)
print("POST status:", post_response.status_code)
print("POST response length:", len(post_response.content))
