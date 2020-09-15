from random import *
game = 1
while game == 1:
    print("Welcome do Guessing Game!,\n I'm thinking in a number and you have to guess,\nit's between 1 and 9\n")
    numero = randint(1,1000)
    numerojogador = 0
    vezesquejogou = 1
    while numerojogador != numero:
        numerojogador = int(input("Adivinhe o numero...\n"))
        if numerojogador > numero:
            vezesquejogou += 1
            print("Está muito alto...\n")
        elif numerojogador < numero:
            vezesquejogou += 1
            print("Está muito baixo...\n")
    if numerojogador == numero:
        print("Você acertou depois de {} tentativas! Quer jogar de novo? [S/N]\n".format(vezesquejogou))
        jogardenovo = input()
        if jogardenovo == "n" or jogardenovo == "N":
            game = 0
            
    
