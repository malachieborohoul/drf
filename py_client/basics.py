import requests
endpoint="http://localhost:8000/api/"

get_response = requests.post(endpoint,  json={"product_id":123})
# get_response = requests.get(endpoint, )

print(get_response.json()) 

