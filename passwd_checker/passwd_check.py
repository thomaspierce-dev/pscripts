import requests

url = 'https://api.pwnedpasswords.com/range/' + '771F4'

response = requests.get(url)

print(response)