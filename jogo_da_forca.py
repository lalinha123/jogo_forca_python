import os
import time
from sys import exit

def jogar():
    os.system('cls') or None
    palavra = str(input('Insira a palavra secreta: ')).upper()
    len_palavra = len(palavra)
    lst_palavra = list(palavra)
    lst_texto = list(len_palavra * '_')
    lst_letra = []
    pontos = 0
    errou = 0
    max_erro = 6
    
    def mostrar():
        os.system('cls') or None
        print('+-------+')
        print('|	|')
        
        match errou:
            case 0:
                print('|\n|\n|\n|')
            case 1:
                print('|	O')
                print('|\n|\n|')
            case 2:
                print('|	O')
                print('|       |')
                print('|\n|')
            case 3:
                print('|	O')
                print('|      /|')
                print('|\n|')
            case 4:
                print('|	O')
                print('|      /|\\')
                print('|\n|')
            case 5:
                print('|	O')
                print("|      /|\\")
                print('|      /')
                print('|')
            case 6:
                print('|	O')
                print("|      /|\\")
                print("|      / \\")
                print('|')

        print('|', ' '.join(lst_texto))
        print('\nLetras inseridas:', ', '.join(lst_letra))
        
    mostrar()

    while lst_texto != lst_palavra and errou < max_erro:
        letra = str(input('\nInsira uma letra: ')).upper()
        acertou = False

        while len(letra) > 1 or letra == '':
            os.system('cls') or None
            mostrar()
            letra = str(input('\nInsira uma letra: ')).upper()
        #-------FIM WHILE--------

        if letra in lst_letra:
            mostrar()
            print('**Você já inseriu a letra',letra)
        else:
            if letra not in lst_palavra:
                errou += 1
                acertou = False
                lst_letra.append(letra)
                mostrar()

                if pontos > 0:
                    pontos -= 1
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
        
        if lst_texto == lst_palavra:
            if pontos == 0:
                pontos = 1

            time.sleep(1)
            os.system('cls') or None
            print('Parabéns! Você encontrou a palavra', palavra,'e fez',pontos,'ponto(s)!')
        #-------FIM IF--------
    #-------FIM WHILE--------

    if errou >= max_erro:
        time.sleep(1)
        os.system('cls') or None
        print('Infelizmente você perdeu! :(')
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
