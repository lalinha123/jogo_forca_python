def jogar():
    palavra = str(input('Insira a palavra secreta: ')).upper()
    len_palavra = len(palavra)
    lst_texto = list(len_palavra * '*')
    lst_letra = []
    max_tent = len_palavra + 6
    tentativas = 0
    pontos = 0

    while lst_texto != list(palavra) and tentativas < max_tent:
        letra = str(input('\nInsira uma letra: ')).upper()
        acertou = False

        while len(letra) > 1 or letra == '':
            letra = str(input('Insira uma letra: ')).upper()
        #-------FIM WHILE--------

        if letra in lst_letra:
            print('Você já inseriu essa letra!')
        else:
            x = 0
            while x < len_palavra:
                if palavra[x] == letra:
                    lst_texto[x] = letra
                    acertou = True
                x += 1
            #-------FIM WHILE--------
        #-------FIM IF ELSE--------

        if acertou == True:
                pontos += 1
        #-------FIM IF--------

        lst_letra.append(letra)
        print(''.join(lst_texto))
        
        if lst_texto == list(palavra):
            print('Parabéns! Você encontrou a palavra', palavra,'e fez',pontos,'ponto(s)!')
        #-------FIM IF--------
    #-------FIM WHILE--------

    if tentativas >= max_tent:
        print('Suas tentativas acabaram! Você fez',pontos,'ponto(s).')
        print('A palavra secreta era:', palavra)
    #-------FIM IF--------

    resp = str(input('\nJogar novamente?: '))
    if resp == 's' or resp == 'sim':
        jogar()
    else:
        print('Obrigado por jogar! :D')
    #-------FIM IF ELSE--------
#-------FIM DEF JOGAR()--------

jogar()




    

