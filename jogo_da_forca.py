import math
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
    
    def mostrar(tempo):
        os.system('cls') or None

        cabeca = ''
        barriga = ''
        perna = ''

        def criaForca(limpa):
            if limpa == True :
                os.system('cls') or None

            lst_forca = ['+-------+', '\n|	|', '\n|	', cabeca, '\n|      ', barriga, '\n|      ', perna, '\n|']
            print(''.join(lst_forca))
            print('|', ' '.join(lst_texto))
            print('\nLetras inseridas:', ', '.join(lst_letra))

            if tempo == True :
                time.sleep(0.5)

        criaForca(False)

        if errou >= 1 :
            cabeca = 'O'
            criaForca(True)

        if errou >= 2:
            barriga = ' |'
            criaForca(True)

        if errou >= 3:
            barriga = '/|'
            criaForca(True)

        if errou >= 4:
            barriga += '\\'
            criaForca(True)

        if errou >= 5:
            perna += '/'
            criaForca(True)

        if errou == 6:
            perna += ' \\'
            criaForca(True)
        
    mostrar(False)

    while lst_texto != lst_palavra and errou < max_erro:
        letra = str(input('\nInsira uma letra: ')).upper()
        acertou = False

        while len(letra) > 1 or letra == '':
            os.system('cls') or None
            mostrar(False)
            letra = str(input('\nInsira uma letra: ')).upper()

        if letra in lst_letra:
            mostrar(False)
            print('**Você já inseriu a letra',letra)
        else:
            if letra not in lst_palavra:
                errou += 1
                acertou = False
                lst_letra.append(letra)
                mostrar(True)

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
                mostrar(False)

        if acertou == True:
            pontos += 1
        
        if lst_texto == lst_palavra:
            if pontos == 0:
                pontos = 1

            time.sleep(1)
            os.system('cls') or None
            print('Parabéns! Você encontrou a palavra', palavra,'e fez',pontos,'ponto(s)!')

    if errou >= max_erro:
        time.sleep(1)
        os.system('cls') or None
        print('Infelizmente você perdeu! :(')
        print('A palavra secreta era:', palavra)
    
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

jogar()
