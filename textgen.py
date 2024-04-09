# Import the Python SDK
import google.generativeai as genai
from jinja2 import Template
import json

genai.configure(api_key='AIzaSyDrsDc0li7SUydZ97zGrbZuOHSBlDkb1Is')

model = genai.GenerativeModel('gemini-pro')

state = "North India"

response = model.generate_content(f"give 20 {state} education news headlines and their summary in 500 words in json format (If any news contains double quotes, then change it to single quote) ")
data = response.text

data = data.replace('```json\n', '').replace('\n```', '')

data_json = json.loads(data)

print(json.dumps(data_json, indent=4))

for key in list(data_json.keys()):
    formatted_data=data_json[key]

with open("data.json", "w") as json_file:
    json.dump(formatted_data, json_file, indent=4)

