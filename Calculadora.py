while True:
    numero = float(input('digite um numero: '))
    numero2 = float(input('digite outro numero: '))
    escolha = input('escolha se deseja somar,subtrair, multiplicar ou dividir: \n 1: soma \n 2: subtração \n 3: multiplicação\n 4: divisao \n ')
    
    if escolha == 1:
        resultado = numero + numero2
        print(f'soma será: {resultado}')
    elif escolha == 2:
        resultado = numero - numero2
        print(f'a subtração será: {resultado}')
    elif escolha == 3:
        resultado = numero * numero2
        print(f'a multiplicação será: {resultado}')
    elif escolha == 4:
        resultado = numero / numero2
        print(f'a divisao será: {resultado}')
    else:
        print('Digite uma opção dentre as alternativas')

    final = input('deseja encerrar o programa? S ou N: ')
    if final == 'S':
        break

    
        


