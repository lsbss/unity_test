from src.model.store import Store
from src.model.user import User


class ServiceUser:

    def __init__(self):
        self.store = Store()

    def check_user(self, nome):
        for user in self.store.bd:
            if user.name == nome:
                return user
        return None

    def add_user(self, name, job):
        if name is not None and job is not None:
            if type(name) is str and type(job) is str:
                user_bd = self.check_user(name)
                if user_bd is None:
                    user = User(name=name, job=job)
                    self.store.bd.append(user)
                    return "Usuario adicionado com sucesso"
                else:
                    return "Usuario ja existente"
            return "Nome e Job devem ser String"
        else:
            return "Usuario nao adicionado"

    def remove_user(self, name):
        user_bd = self.check_user(name)
        if user_bd is not None:
            self.store.bd.remove(user_bd)
            return "Usuario removido com sucesso"
        else:
            return "Usuario nao encontrado"

    def select_user(self, name):
        user_bd = self.check_user(name)
        if user_bd is not None:
            return "Job: " + user_bd.job
        else:
            return "Usuario nao encontrado"

    def update_user(self, name, new_job):
        user_bd = self.check_user(name)
        if user_bd is not None:
            user_bd.job = new_job
            return "Job atualizado com sucesso"
        else:
            return "Usuario nao encontrado"
