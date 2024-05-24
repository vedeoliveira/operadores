# Funcionamento dos operadoes básicos em python
sair = False
while not sair:
    vl_1 = eval(input("Digite o 1º valor "))
    vl_2 = eval(input("Digite o 2º valor "))
    print(50*'-')

    if vl_1 is vl_2:
        print('Os valores ocupam a mesma região de memória')
    else:
        print('Os valores NÂO ocupam a mesma região de memória')

    print(50*'-')

    #print('Qual operação executar?\n [1] - Somar\n [2] - Subtrair\n [3] - Multiplicação')
    #print(' [4] - Dividisão\n [5] - Resto da Divisão\n [6] - Expoente\n [7] - Divisão Inteira')

    print('''     Qual operação executar?
     [1] - Somar
     [2] - Subtrair
     [3] - Multiplicação
     [4] - Dividisão
     [5] - Resto da Divisão
     [6] - Expoente
     [7] - Divisão Inteira''')

    print(50*'-')

    operacao = int(input('Escolha: '))
    match operacao:
        case 1:
            print(f'A Soma é {vl_1 + vl_2}')
        case 2:
            print(f'A Subtração é {vl_1 - vl_2}')
        case 3:
            print(f'A Multiplicação é {vl_1 * vl_2}')
        case 4:
            print(f'A Divisão é {(vl_1 / vl_2):.2f}')
        case 5:
            print(f'O Resto da divisão é {vl_1 % vl_2}')
        case 6:
            print(f'A Exponenciação é {vl_1 ** vl_2}')
        case 7:
            print(f'A Divisão Inteira é {vl_1 // vl_2}')
        case _:
            print('Opção Inválida!')

    print(50*'-')

    pergunta = str(input('Deseja sair?[S/N]' )).lower()
    if pergunta == ('s'):
        sair = True
        print('Até logo.')    
        
"""
nome = 'Thiago Vicente Estevam de Oliveira'
frutas = ['limão', 'uva', 'maça']
print('' in nome)"""