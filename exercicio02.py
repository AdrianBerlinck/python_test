

def exercicio02(salario,cargo,tempo,matricula):
    
    if '@' in matricula or '$' in matricula or '#' in matricula or '-' in matricula or '_' in matricula:
        return 'Inválido'

    elif salario < 4000 or tempo < 5:
        return 'Júnior'

    elif salario >= 4000.01 and salario <=10000 or tempo >=6 and tempo <= 10:
        return 'Sênior'
    
    elif salario > 10000 or tempo >10:
        return 'Pleno'
