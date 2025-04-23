
def exercicio05(idade):
    
    
    if(idade <16) :
        return 'NÃO PODE VOTAR'
    
    elif(idade >=16 and idade <=17) :
        return 'PODE VOTAR'
    
    elif(idade >=18 and idade <=34 ) :
        return 'DEVE VOTAR MAS NÃO PODE SER PRESIDENTE'
    
    elif(idade >34 and idade < 71) :
        return 'DEVE VOTAR E PODE SER PRESIDENTE'
    
    else:
        return 'PODE VOTAR E PODE SER PRESIDENTE'