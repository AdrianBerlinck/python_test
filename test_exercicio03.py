from exercicio03 import exercicio03
import pytest

@pytest.mark.parametrize('valor',[(50000),(65000),(80000),(95000),(110000),(125000)])
@pytest.mark.parametrize('imposto',[(0.3),(0.2),(0.15),(0.15),(0.18),(0.38)])
@pytest.mark.parametrize('desconto',[(0.01),(0.06),(0.09),(0.02),(0.05),(0.07)])
@pytest.mark.parametrize('comissao',[(0),(0.1),(0.12),(0.19),(0.25),(0.15)])

def test_exercicio01(valor,imposto,desconto,comissao):
    expect = valor+(valor*comissao)+(valor*imposto)+(valor*desconto)
    assert exercicio03(valor,imposto,desconto,comissao) == expect
    
    