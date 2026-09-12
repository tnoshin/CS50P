import sys
import requests

try:
    n=float(sys.argv[1])
except (ValueError, IndexError):
    sys.exit('Error!')

try:
    r = requests.get('https://rest.coincap.io/v3/assets/bitcoin?apiKey=9243578cfbcf406526cfa36eef1ad6e3c2377ed9f4bbc77c97a6c768febb1e69')
    info = r.json()
except requests.RequestException:
    sys.exit('Error!')

final = float(info['data']['priceUsd'])
cost = n*final

print(f'${cost:,.4f}')


'''
import sys
import requests

try:
    n=float(sys.argv[1])
except (ValueError, IndexError):
    sys.exit('Error!')
try:
    response = requests.get('https://rest.coincap.io/v3/assets/bitcoin?apiKey=9243578cfbcf406526cfa36eef1ad6e3c2377ed9f4bbc77c97a6c768febb1e69')
    data= response.json()
except requests.RequestException:
    sys.exit('Error!')
price = float(data['data']['priceUsd'])
result= n*price
print(f'${result:,.4f}')'''



    

