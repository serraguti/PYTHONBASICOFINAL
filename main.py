import services.servicedepartamentos as service
from models.departamento import Departamento

print("Ejemplo completo Python")
#Creamos un nuevo departamento
deptNew: Departamento = Departamento()
deptNew.id = int(input("Introduzca un Id departamento: "))
deptNew.nombre = input("Nombre de departamento: ")
deptNew.localidad = input("Localidad: ")
status = service.insertDepartamento(deptNew)
print(f"Status insert: {status}")
#MODIFICAMOS UN DEPARTAMENTO
deptUpdate: Departamento = Departamento()
deptUpdate.id = 51
deptUpdate.nombre = "NUEVO"
deptUpdate.localidad = "GIJON"
status_update = service.updateDepartamento(deptUpdate)
print(f"Status update {status_update}")
#Eliminamos el departamento 99
status_delete = service.deleteDepartamento(99)
print(f"Status delete {status_delete}")
departamentos:list[Departamento] = service.getDepartamentos()
for dept in departamentos:
    print(f"Id: {dept.id}, Nombre: {dept.nombre}, Localidad: {dept.localidad}")
print("Fin de programa")