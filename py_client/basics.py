import requests
endpoint="127.0.0.1"

get_response = requests.get(endpoint)

print(get_response.json())