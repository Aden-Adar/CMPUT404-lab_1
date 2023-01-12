import requests

print(requests.__version__)
response = requests.get("https://raw.githubusercontent.com/Aden-Adar/CMPUT404-lab_1/main/lab1.py")
print(response.text)
