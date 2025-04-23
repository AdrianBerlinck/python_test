from exercicio01 import exercicio01
import pytest

@pytest.mark.parametrize('num1',[(4),(5),(10),(20),(25)])
@pytest.mark.parametrize('num2',[(33),(11),(14),(2),(5)])
@pytest.mark.parametrize('signal',[('+'),('-'),('*'),('/')])
def test_exercicio01(num1,num2,signal):
    
    if(signal == '+') :
        expect = num1+num2
    
    elif(signal == '-') :
        expect =  num1-num2
    
    elif(signal == '*') :
        expect =  num1*num2
    
    elif(signal == '/') :
        expect =  num1/num2
    
    else:
        expect =  ''
    
    assert exercicio01(num1,num2,signal) == expect
    
    