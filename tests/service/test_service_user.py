from src.service.service_user import ServiceUser


class TestServiceUser():

    def test_add_user(self):
        name = "Leonardo"
        job = "Gigolo"
        resultado_esperado = "Usuario adicionado com sucesso"

        service = ServiceUser()
        resultado_encontrado = service.add_user(name=name, job=job)

        assert resultado_encontrado == resultado_esperado

    def test_add_user_invalid_job(self):
        name = "Leonardo"
        job = None
        resultado_esperado = "Usuario nao adicionado"

        service = ServiceUser()
        resultado_encontrado = service.add_user(name=name, job=job)

        assert resultado_encontrado == resultado_esperado

    def test_add_user_invalid_name(self):
        name = None
        job = "Teste"
        resultado_esperado = "Usuario nao adicionado"

        service = ServiceUser()
        resultado_encontrado = service.add_user(name=name, job=job)

        assert resultado_encontrado == resultado_esperado

    def test_add_user_invalid_type_job(self):
        name = "Leonardo"
        job = 1
        resultado_esperado = "Nome e Job devem ser String"

        service = ServiceUser()
        resultado_encontrado = service.add_user(name=name, job=job)

        assert resultado_encontrado == resultado_esperado

    def test_add_user_invalid_Typename(self):
        name = 1
        job = "Teste"
        resultado_esperado = "Nome e Job devem ser String"

        service = ServiceUser()
        resultado_encontrado = service.add_user(name=name, job=job)

        assert resultado_encontrado == resultado_esperado

    def test_add_exist_user(self):
        name = "Leo"
        job = "Tester"
        resultado_esperado = "Usuario ja existente"

        service = ServiceUser()
        resultado_encontrado = service.add_user(name=name, job=job)

        assert resultado_encontrado == resultado_esperado

    def test_delete(self):
        name = "Leo"
        job = "Tester"
        resultado_esperado = "Usuario removido com sucesso"

        service = ServiceUser()
        resultado_encontrado = service.remove_user(name=name)

        assert resultado_encontrado == resultado_esperado

    def test_delete_not_found(self):
        name = "Leleco"
        job = "Tester"
        resultado_esperado = "Usuario nao encontrado"

        service = ServiceUser()
        resultado_encontrado = service.remove_user(name=name)

        assert resultado_encontrado == resultado_esperado

    def test_get_user(self):
        # Sucesso
        name = "Leo"
        resultado_esperado = "Job: Tester"

        service = ServiceUser()
        resultado_encontrado = service.select_user(name=name)

        assert resultado_encontrado == resultado_esperado

    def test_get_user_not_found(self):
        name = "Leleco"
        job = "Tester"
        resultado_esperado = "Usuario nao encontrado"

        service = ServiceUser()
        resultado_encontrado = service.select_user(name=name)

        assert resultado_encontrado == resultado_esperado

    def test_update_user(self):
        name = "Leo"
        job = "Testinho"
        resultado_esperado = "Job atualizado com sucesso"

        service = ServiceUser()
        resultado_encontrado = service.update_user(name=name, new_job=job)

        assert resultado_encontrado == resultado_esperado

    def test_update_user_not_found(self):
        name = "Leleco"
        job = "Testinho"
        resultado_esperado = "Usuario nao encontrado"

        service = ServiceUser()
        resultado_encontrado = service.update_user(name=name, new_job=job)

        assert resultado_encontrado == resultado_esperado