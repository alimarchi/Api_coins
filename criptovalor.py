import requests 

endpoint = "https://rest.coinapi.io/v1/exchangerate/{}/{}?apikey=1CC2144C-EFE9-4EA3-9648-E1F177BB28AE"

moneda_from = input("Moneda de origen: ")

moneda_to = input("Moneda a conseguir: ")

r = requests.get(endpoint.format(moneda_from, moneda_to))

print(round(r.json()["rate"], 2))
print(r.json())
print(r.status_code)
print(round(r.json()["rate"], 2))