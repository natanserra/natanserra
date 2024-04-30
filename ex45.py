from time import sleep
from random import randint
print(""" ============= \033[1;36mSUAS OPÇÕES\033[m =============
\033[1;33m[ 0 ] PEDRA\033[m
\033[1;34m[ 1 ] PAPEL\033[m
\033[1;35m[ 2 ] TESOURA\033[m
""")
tabela = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
jogador = int(input('\033[1mQual é a sua jogada?\033[m '))

print('\033[1;33mJO\033[m')
sleep(0.7)
print('\033[1;33mKEN\033[m')
sleep(0.7)
print('\033[1;33mPÔ!\033[m')
print('='*30)
print(f'O jogador escolheu {tabela[jogador]}')
print(f'O computador escolheu {tabela[computador]}')

pedra = 0
papel = 1
tesoura = 2
# Todas as situações em que o computador ganha
if computador == pedra and jogador == tesoura or computador == papel and jogador == pedra or computador == tesoura and jogador == papel:
    print('COMPUTADOR VENCEU!')
elif computador == jogador:
    print('EMPATE!')
elif computador == pedra and jogador == papel or computador == papel and jogador == tesoura or computador == tesoura and jogador == pedra:
    print('JOGADOR VENCEU!')
