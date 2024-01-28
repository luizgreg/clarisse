import random
import time
yy = input('qual seu nome')
print('ola {} eu sou a clarisse'.format(yy))
print('se diver duvida e so escrever manual')
zxy = input('diga um lembrete. para ver ele digita ver lembrete')
aa44 = ('manual',  'calculadora',  'jogo1',  'jogo 2',  'hora', 'ver lembrete', 'bingo', 'alarme', 'jogo da memoria', )
n = input('como posso te ajudar')
while n not in ('fim'):
    if n not in aa44:
        print('comado invalido')
        print('se tiver duvida escreva manual')
    n = input('como posso te ajudar')
    if n == ('ver lembrete'):
        print(zxy)
    if n == ('calculadora'):
        p = input('qual operaçao matematica adiçao,subtraçao,diviçao,multiplicaçao')
        n2 = int(input('digite um numero'))
        n3 = int(input('digite um numero'))
        if p == ('adiçao'):
            a = n2 + n3
            print(a)
        elif ('subtraçao'):
            b = n2 - n3
            print(b)
        elif ('multiplicaçao'):
            c = n2 * n3
            print(c)
        else:
            d = n2 / n3
            print(d)
    elif n == ('jogo1'):

        a = ('papel', 'tesora', 'pedra')
        computador = random.randint(0, 2)
        print('suas opiçoes  sao [0]pedra  [1]papel  [2]tesoura')
        print('=-' * 11)
        a = int(input('qual voce quer'))
        if computador == 0:
            if a == 0:
                print('empate')
            elif a == 1:
                print('voce ganhou')
            elif a == 2:
                print('eu ganhei')

        elif computador == 1:
            if a == 1:
                print('empate')
            elif a == 2:
                print('voce ganhou')
            elif a == 0:
                print('eu ganhei')


        elif computador == 2:
            if a == 2:
                print('empate')
            elif a == 0:
                print('voce ganhou')
            elif a == 1:
                print('eu ganhei')
        print('=-' * 11)
        print(computador)


    elif n == ('manual'):
        print(aa44)

    if n == ('bingo'):
        for gg in range(75):
            x = random.randint(1,76)
            print(x)
            time.sleep(5)
    if n == ('hora'):
        x = time.localtime()
        print('a hora e:' + str(x[3]))
        print('os minutos sao:' + str(x[4]))
        print('e os segudos sao:' + str(x[5]))
    if n == ('jogo 2'):
            s = ('sim')
            n = ('nao')
            print('escolha um número de 1 a 9')
            a = input('o seu número é par sim ou nao')
            if a == s:
                b = input('seu número é divisivel por 4')
                if b == s:
                    c = input('seu numero tem 4 letras')
                    if c == s:
                        print('seu numero e 8')
                    if c == n:
                        print('seu numero e 4')
                if b == n:
                    d = input('seu numero começa com d')
                    if d == n:
                        print('seu numero e 6')

                    if d == s:
                        print('seu numero e 2')

            if a == n:

                e = input('seu número é divisivel por 3')
                if e == s:
                    f = input('seu numero e primo')
                    if f == s:
                        print('seu numero e 3')
                    if f == n:
                        print('seu numero e 9')
                if e == n:
                    g = input('seu numero começa com c')
                    if g == n:
                        h = input('seu numero e maior que 6')
                        if h == s:
                            print('seu numero e 7')
                        if h == n:
                            print('seu numero e 1')

                    if g == s:
                        print('seu numero e 5')
            print('parebens')
    if n == ('jogo da memoria'):
        nsee = random.randint(1, 100)
        print(nsee)
        time.sleep(5)
        nse = random.randint(1, 1000)
        for q in range(99):
            print(nse)
        qwq = int(input('qual era o numero'))
        if qwq == nsee:
            print('parabens')
        else:
            print('tente de novo')