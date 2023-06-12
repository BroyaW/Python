import random
from random import randint
n = randint(1,10)
num = 0
print("{:=^40}".format(' Jogo de adivinhação '))
while num != n:
    num = int(input("Em qual numero estou pensando? (1 a 10) "))
    while num > 10 or num < 1:
        print("[Erro] digite um numero de 1 a 10 burro!")
        num = int(input("Digite um valor certo: "))
    if(num != n):
        print("[ERROU]\n")
    else:
        print("Acertou\n")
print("Fim do jogo.")
