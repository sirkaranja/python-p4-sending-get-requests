import requests
import json

url = "https://learn-co-curriculum.github.io/json-site-example/endpoints/locations.json"

response = requests.get(url) #get request to display courses in the above url

json_content = json.loads(response.text)

print(json.dumps(json_content, indent=4))
