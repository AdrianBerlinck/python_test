from exercicio01 import exercicio01
import pytest

@pytest.mark.parametrize('num1,num2,signal,expect',[(2,3,'+',5),(4,3,'-',1),(2,3,'*',6),(4,2,'/',2)])

def test_exercicio01(num1,num2,signal,expect):
    assert exercicio01(num1,num2,signal) == expect
    
    