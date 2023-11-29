import requests
endpoint="http://localhost:8000/api/products/8/delete/"

# get_response = requests.get(endpoint,  json={"title":"Hello world", })
get_response = requests.put(endpoint, json=data)

print(get_response.json()) 

 