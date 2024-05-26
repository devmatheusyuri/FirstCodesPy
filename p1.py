from random import randint
from time import sleep
aleatório = ["PEDRA","PAPEL","TESOURA"]
escolha = "0"

while True:
    escolha = str(input("Você quer jogar pedra,papel,tesoura? ")).strip().upper()
    if escolha in "SIM" or escolha in "NÃO":
        break

while escolha in "SSIM":
    print(f"-="*20)
    print(f"{"PEDRA,PAPEL OU TESOURA":^40}")
    print(f"-="*20)
    print("""As escolhas são: 
[ 1 ] - PEDRA
[ 2 ] - PAPEL
[ 3 ] - TESOURA""")
    jogada = str(input("\n>>>>A sua jogada vai ser: "))
    computador = randint(0,2)
    sleep(0.5)
    
    if jogada.isnumeric():
        jogada = int(jogada)
        
        while jogada not in range(1,4):
            jogada = int(input("\n>>>>Você digitou um número fora das escolhas,tente novamente: "))
            sleep(1)
        
        else:
            print(f"="*20)
            print(f"O computador escolheu: {aleatório[computador]}")
            print(f"O jogador escolheu {aleatório[jogada - 1]}")
            print(f"="*20)
        
        if jogada == 1 and computador == 2 or jogada == 2 and computador == 0 or jogada == 3 and computador == 1:
            print(f"O jogador ganhou!\n")
        
        elif jogada == 1 and computador == 0 or jogada == 2 and computador == 1 or jogada == 3 and computador == 2:
            print(f"Foi empate!\n")
        
        else:
            print(f"O computador ganhou!\n")
        escolha = str(input("Você quer continuar jogando? ")).strip().upper()
        
        if escolha not in "SSIM" and escolha not in "NNÃO":
            
            while escolha not in "SSIM" and escolha not in "NNÃO":
                escolha = str(input("Inválido,quer continuar jogando? ")).strip().upper()
        
        if escolha in "SSIM":
            0
        
        elif escolha in "NNÃO":
            break        
   
    else:
        jogada = str(jogada)
        print(f"\n>>>>Inválido,tente novamente.\n")
        sleep(1)

if escolha in "NÃO":
    print("\nObrigado pela atenção! :)\n")
