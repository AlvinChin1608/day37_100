import requests
from datetime import datetime

# https://pixe.la/v1/users/alvin1608/graphs/graph1.html

USERNAME = "alvin1608"
TOKEN = "abcdeFGHIJ12345"
GRAPH_ID = "graph1"

# https://pixe.la/
PIXELA_ENDPOINT = "https://pixe.la/v1/users"

# the post API is quite unique, instead of Auth key we create our own
user_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# # Since we are only using this to create an account, we can comment this out
# response = requests.post(url=PIXELA_ENDPOINT, json=user_parameters)
# print(response.text)

graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

grap_config = {
    "id": "graph1",
    "name": "Running Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

# Here is our Request Header, it essential making it more secure
headers = {
    "X-USER-TOKEN": TOKEN
}

# # We can comment this out, because graph has been created
# response = requests.post(url=graph_endpoint, json=grap_config, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"

# today = datetime(year=2024, month=6, day=14) # let's say we want to a specific date to input yesterday's data
today = datetime.now()
print(today) # output: 2024-06-15 20:29:43.105123
print(today.strftime("%Y%m%d")) # 20240615

pixel_data = {
    "date": today.strftime("%Y%m%d"), # format yyyymmdd
    "quantity": "15",  # km
}

# # To add data
# response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)  # Use the correct endpoint
# print(response.text)

update_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"  # Corrected URL

new_pixel_data = {
    "quantity": "4.5"
}
# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)

delete_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"  # Corrected URL
response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)