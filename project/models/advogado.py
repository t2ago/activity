from project.models.endereco import Endereco
from project.models.enums.estado_civil import EstadoCivil
from project.models.enums.setor import Setor
from project.models.enums.sexo import Sexo
from project.models.funcionario import Funcionario

class Advogado(Funcionario):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco, sexo: Sexo, estadocivil: EstadoCivil, datanascimento: str, cpf: str, rg: str, matricula: str, setor: Setor, salario: int, oab: str) -> None:
        super().__init__(id, nome, telefone, email, endereco, sexo, estadocivil, datanascimento, cpf, rg, matricula, setor, salario)
        self.oab = self._verificar_oab(oab)

    def _verificar_oab(self,valor):
        self._verificar_oab_tipo_invalido(valor)

        self.oab = valor
        return self.oab

    def _verificar_oab_tipo_invalido(self,valor):
        if not isinstance(valor, str):
            raise TypeError("Oab inválida!")

    def __str__(self) -> str:
        return (f"{super().__str__()}"
                f"\nOab: {self.oab}")