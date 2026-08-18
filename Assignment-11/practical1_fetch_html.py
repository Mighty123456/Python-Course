import requests

url = "https://example.com"

response = requests.get(url)

print("Status Code:", response.status_code)
print("\nHTML Content:\n")
print(response.text)
