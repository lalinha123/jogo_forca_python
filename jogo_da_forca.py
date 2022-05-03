import os
import time
from sys import exit

def jogar():
    palavra = str(input('Insira a palavra secreta: ')).upper()
    len_palavra = len(palavra)
    lst_texto = list(len_palavra * '*')
    lst_letra = []
    max_tent = len_palavra + 4
    tentativas = 0
    pontos = 0
    
    def mostrar():
        os.system('cls') or None
        print(''.join(lst_texto))
        
    mostrar()

    while lst_texto != list(palavra) and tentativas < max_tent:
        letra = str(input('\nInsira uma letra: ')).upper()
        acertou = False

        while len(letra) > 1 or letra == '':
            os.system('cls') or None
            mostrar()
            letra = str(input('\nInsira uma letra: ')).upper()
            
            tentativas += 1
        #-------FIM WHILE--------

        if letra in lst_letra:
            lst_letra.append(letra)
            mostrar()
            print('Você já inseriu a letra',letra)
        else:
            x = 0
            while x < len_palavra:
                if palavra[x] == letra:
                    lst_texto[x] = letra
                    acertou = True
                x += 1
            
            lst_letra.append(letra)
            mostrar()
            
            #-------FIM WHILE--------
        #-------FIM IF ELSE--------

        if acertou == True:
                pontos += 1
        #-------FIM IF--------

        tentativas += 1
        
        if lst_texto == list(palavra):
            os.system('cls') or None
            print('Parabéns! Você encontrou a palavra', palavra,'e fez',pontos,'ponto(s)!')
        #-------FIM IF--------
    #-------FIM WHILE--------

    if tentativas >= max_tent:
        os.system('cls') or None
        print('Suas tentativas acabaram! Você fez',pontos,'ponto(s).')
        print('A palavra secreta era:', palavra)
    #-------FIM IF--------
    
    resp = str(input('\nJogar novamente?: '))
    if resp == 's' or resp == 'sim':
        os.system('cls') or None
        jogar()
    else:
        os.system('cls') or None
        print('Obrigado por jogar! :D')
        time.sleep(3)
        os.system('cls') or None
        exit(0)
        
    #-------FIM IF ELSE--------
#-------FIM DEF JOGAR()--------

jogar()
