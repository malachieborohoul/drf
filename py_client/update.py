import requests
endpoint="http://localhost:8000/api/products/2/"
data ={
    "title":"This is dope man",
    "price":208.02,
}
# get_response = requests.get(endpoint,  json={"title":"Hello world", })
get_response = requests.put(endpoint, json=data)

print(get_response.json()) 

 