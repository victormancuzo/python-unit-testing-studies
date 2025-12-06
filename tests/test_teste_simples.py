# pip install pytest
import pytest


def dobrar(x: int) -> int:
    if not isinstance(x, int):
        raise TypeError("Variável x deve ser do tipo int")
    return x * 2


def test_dobrar_retorna_o_dobro():
    assert dobrar(5) == 10


def test_dobrar_lanca_erro_quando_x_diferente_int():
    with pytest.raises(TypeError):
        dobrar("5")  # Retorno: passed

    with pytest.raises(TypeError):
        dobrar(5.5)  # Retorno: passed

    with pytest.raises(TypeError):
        dobrar(5)  # Retorno: failed
