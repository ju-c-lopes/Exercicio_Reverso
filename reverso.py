x = int(input("Digite o numero: "))
w = x
teste = -1
unidade = -1
dezena = -1
centena = -1

while teste != x:
    if x > 999:
        teste = x
        unidade = 0
        dezena = 0
        centena = 0
    else:
        if 9 >= x >= 0:
            unidade = x
            dezena = 0
            centena = 0
            x = -1
            teste = -1

        else:
            while (unidade < 0) or (unidade > 10):
                # if x == 0:
                #    unidade = x
                # else:
                if x > 9:
                    while x > 9:
                        x = x - 10
                        unidade = x
                x = w

            while (dezena < 0) or (dezena >= 10):
                if x > 9:
                    while x > 99:
                        x = x - 100
                    if x != 0:
                        while x > 9:
                            x = x // 10
                            dezena = x
                    else:
                        dezena = x
                x = w

            while (centena < 0) or (centena > 10):
                if x > 9:
                    while x > 9:
                        x = x // 100
                centena = x
        x = w

        teste = (centena * 100) + (dezena * 10) + unidade

    print(centena, " ", dezena, " ", unidade)
    print('\n')

    reverso = (unidade * 100) + (dezena * 10) + centena

print(reverso)
