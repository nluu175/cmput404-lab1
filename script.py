import requests

print(requests.__version__)

response = requests.get("http://google.com/")

print(response)

response_to_script = requests.get(
    "https://raw.githubusercontent.com/nluu175/cmput404-lab1/main/script.py"
)

print(response_to_script.content)
