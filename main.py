from src.model.store import Store
from src.service.service_user import ServiceUser

store = Store()

#Insert
#Sucesso
name = "Leonardo"
job = "Gigolo"

service = ServiceUser()
print(service.add_user(name=name, job=job))

#Invalido
name = "Leonardo"
job = None

service = ServiceUser()
print(service.add_user(name=name, job=job))

#Já existe
name = "Leo"
job = "Tester"

service = ServiceUser()
print(service.add_user(name=name, job=job))

# Delete
#Sucesso
name = "Leo"
job = "Tester"

service = ServiceUser()
print(service.remove_user(name=name))

#Não Existe
name = "Leleco"
job = "Tester"

service = ServiceUser()
print(service.remove_user(name=name))

# Busca
#Sucesso
name = "Leo"
job = "Tester"

service = ServiceUser()
print(service.select_user(name=name))

#Não Existe
name = "Leleco"
job = "Tester"

service = ServiceUser()
print(service.select_user(name=name))

# Update
#Sucesso
name = "Leo"
job = "Testinho"

service = ServiceUser()
print(service.update_user(name=name, new_job=job))

#Não Existe
name = "Leleco"
job = "Testinho"

service = ServiceUser()
print(service.update_user(name=name, new_job=job))
