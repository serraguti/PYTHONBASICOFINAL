import requests
api_url = "https://apicruddepartamentoscore.azurewebsites.net/api/Departamentos/10"
response = requests.get(api_url)
datos = response.json()
print(datos)