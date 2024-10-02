import pytest
from project.models.advogado import Advogado
from project.models.endereco import Endereco
from project.models.enums.estado_civil import EstadoCivil
from project.models.enums.sexo import Sexo
from project.models.enums.unidade_federativa import UnidadeFederativa
from project.models.enums.setor import Setor

@pytest.fixture
def advogado_valido():
    advogado = Advogado(333, "c", "3333-3333", "c@gmail.com", Endereco("Rua C", "3", "Térreo", "3333", "São Paulo", UnidadeFederativa.SAO_PAULO), Sexo.FEMININO, EstadoCivil.SOLTEIRO, "01/01/01", "1111", "2222", "3333", Setor.JURIDICO, 7000, "3333")
    return advogado

def test_oab_valido(advogado_valido):
    assert advogado_valido.oab == "3333"

def test_mudar_oab_valido(advogado_valido):
    advogado_valido.oab = "22222"
    assert advogado_valido.oab == "22222"

def test_oab_tipo_invalido():
    with pytest.raises(TypeError, match="Oab inválida!"):
        Advogado(333, "c", "3333-3333", "c@gmail.com", Endereco("Rua C", "3", "Térreo", "3333", "São Paulo", UnidadeFederativa.SAO_PAULO), Sexo.FEMININO, EstadoCivil.SOLTEIRO, "01/01/01", "1111", "2222", "3333", Setor.JURIDICO, 7000, 3333)