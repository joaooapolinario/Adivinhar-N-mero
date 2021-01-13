import random

print('TENTE ADIVINHAR O NÚMERO EM QUE A MAQUINA ESTÁ PENSANDO!!')

começar = str(input('QUER INICIAR?[S/N] ')).upper()
r = começar
if começar == 'n':  
    input('Tecle ENTER para sair')
    
while r == 'S':
    n1 = int(input(' Digite um numero de 1 à 5>>'))
    n = random.randint(1, 5)
    if n1 == n:
        print('Você acertou!!')
    else:
        print('Você errou;-;')
    r = str(input('Quer continuar?[S/N] ')).upper()
print('Até mais')
input('Digite ENTER para sair!')

