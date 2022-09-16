### JOKENPO GAME ################################
### Por Adriano Baumart
### Versão: 1.0.0       Data: 15/09/2022
### Desafio do Curso de Pyhton
#################################################
from random import randint
from time import sleep
jogada = {1: 'PEDRA', 2: 'PAPEL', 3: 'TESOURA'}
nomedojogo = ' JOKENPO '

print('#'*20 + nomedojogo + '#'*20)
print('#'*35)
print('ESCOLHA SUA JOGADA')
print('#'*35)
print('[ 1 ] - PEDRA | [ 2 ] PAPEL | [ 3 ] TESOURA')
print('#'*35)
pessoa = int(input('Selecione sua mão: '))
computador = randint(1, 3)
vencedor = 'COMPUTADOR'

print('JO...', end='')
sleep(1)
print('KEN...', end='')
sleep(1)
print('PÔ...')
sleep(1)

print('VOCÊ:  {} \nCOMPUTADOR:  {}'.format(jogada[pessoa], jogada[computador]))

if jogada[pessoa] == jogada[computador]:
    vencedor = 'EMPATE! NINGUÉM'
elif jogada[pessoa] == 'PEDRA' and jogada[computador] == 'TESOURA':
    vencedor = 'VOCÊ'
elif jogada[pessoa] == 'PAPEL' and jogada[computador] == 'PEDRA':
    vencedor = 'VOCÊ'
elif jogada[pessoa] == 'TESOURA' and jogada[computador] == 'PAPEL':
    vencedor = 'VOCÊ'

print('{} VENCEU!'.format(vencedor))
