import requests
from models.departamento import Departamento

#Necesitamos nuestra variable de acceso al API
#Cada método tendrá un Endpoint, en cada método del service
#Llamaremos a cada EndPoint
api_url = "https://apicruddepartamentoscore.azurewebsites.net/"

#Realizamos un método para leer todos los departamentos
def getDepartamentos():
    #Necesitamos el Endpoint
    endpoint = "api/departamentos"
    response = requests.get(api_url + endpoint)
    #Este json lo interpreta como un diccionario
    json = response.json()
    #Transformamos nuestra lista/diccionario a Models
    #Tipamos la lista para control de errores
    data:list[Departamento] = []
    #Recorremos la lista y la transformamos en models
    for item in json:
        #Creamos un nuevo objeto Departamento
        dept: Departamento = Departamento()
        dept.id = int(item["numero"])
        dept.nombre = item["nombre"]
        dept.localidad = item["localidad"]
        data.append(dept)
    return data

def insertDepartamento(departamento: Departamento):
    endpoint = "api/departamentos"
    #Convertimos el model a diccionario
    jsonDept = {
        "numero": departamento.id,
        "nombre": departamento.nombre,
        "localidad": departamento.localidad
    }
    response = requests.post(api_url + endpoint, json=jsonDept)
    return response.status_code

def updateDepartamento(departamento: Departamento):
    endpoint = "api/departamentos"
    jsonDept = {
        "numero": departamento.id,
        "nombre": departamento.nombre,
        "localidad": departamento.localidad
    }
    response = requests.put(api_url + endpoint, json=jsonDept)
    return response.status_code

def deleteDepartamento(id: int):
    endpoint = f"api/departamentos/{id}"
    response = requests.delete(api_url + endpoint)
    return response.status_code