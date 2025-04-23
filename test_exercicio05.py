from exercicio05 import exercicio05
import pytest

@pytest.mark.parametrize('idade',[(15),(16),(18),(35),(72)])

def test_exercicio01(idade):
    
        
    if(idade <16) :
        expect =  'NÃO PODE VOTAR'
    
    elif(idade >=16 and idade <=17) :
        expect = 'PODE VOTAR'
    
    elif(idade >=18 and idade <=34 ) :
        expect = 'DEVE VOTAR MAS NÃO PODE SER PRESIDENTE'
    
    elif(idade >34 and idade < 71) :
        expect = 'DEVE VOTAR E PODE SER PRESIDENTE'
    
    else:
        expect = 'PODE VOTAR E PODE SER PRESIDENTE'
    
    assert exercicio05(idade) == expect