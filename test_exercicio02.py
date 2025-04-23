
from exercicio02 import exercicio02


def test_exercicio02():
    assert exercicio02(3000,'dev',4,'18000') == 'Júnior'
    assert exercicio02(5000,'dev',7,'18001') == 'Sênior'
    assert exercicio02(11000,'dev',11,'18002') == 'Pleno'
    assert exercicio02(11000,'dev',11,'1880-2') == 'Inválido'

    