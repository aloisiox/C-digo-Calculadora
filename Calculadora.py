while True:
    numero = int(input('digite um numero: '))
    numero2 = int(input('digite outro numero: '))
    escolha = input('escolha se deseja somar,subtrair, multiplicar ou dividir: \n S: soma \n sub: subtração \n mult:multiplicação\n div: divisao \n ')

    if escolha == 'S':
        resultado = numero + numero2
        print(f'soma será: {resultado}')
    elif escolha == 'sub':
        resultado = numero - numero2
        print(f'a subtração será: {resultado}')
    elif escolha == 'mult':
        resultado = numero * numero2
        print(f'a multiplicação será: {resultado}')
    elif escolha == 'div':
        resultado = numero / numero2
        print(f'a divisao será: {resultado}')
    else:
        print('Digite uma opção dentre as alternativas')

    final = input('deseja encerrar o programa? S ou N: ')
    if final == 'S':
        break

    
        


