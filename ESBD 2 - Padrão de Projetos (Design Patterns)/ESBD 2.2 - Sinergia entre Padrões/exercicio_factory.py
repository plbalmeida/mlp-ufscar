class Cliente:
    def return_id() -> str:
        raise NotImplementedError

class Juridico(Cliente):

    def __init__(self, cnpj):
        self.cnpj = cnpj

    def return_id(self):
        return self.cnpj

class Fisico(Cliente):

    def __init__(self, cpf):
        self.cpf = cpf

    def return_id(self):
        return self.cpf

class ClienteFactory:
    def create_client(self, id) -> Cliente:
        raise NotImplementedError

class JuridicoFactory(ClienteFactory):
    def create_client(self, cnpj) -> Cliente:
        return Juridico(cnpj)

class FisicoFactory(ClienteFactory):
    def create_client(self, cpf) -> Cliente:
        return Fisico(cpf)

if __name__ == "__main__":

    Juridico1 = JuridicoFactory().create_client("12.123.123/0001-00")

    Fisico1 = FisicoFactory().create_client("123.123.123-12")

    print(Juridico1.return_id())

    print(Fisico1.return_id())