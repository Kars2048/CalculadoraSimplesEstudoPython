print('-----------------------------------------------------')
print('         Sistema Simples de Calculadora              ')
print('-----------------------------------------------------')

#FUNÇÕES DE CALCULOS
def calculo_soma(a, b):
    return a+b

def calculo_sub(a, b):
    return a-b

def calculo_mult(a):
    resultados = []
    for _ in range(11):
        resultado = a*_
        resultados.append(f'{a} X {_} = {resultado}')
    return resultados

def calculo_div(a, b):
    if (b==0):
        return('NÃO É POSSIVEL FAZER DIVISÃO POR ZERO!')
    return a/b


#FUNÇÕES DE ENTRADA
def perguntas_cal():
    try:
        n1 = int(input('DIGITE O PRIMEIRO NÚMERO: '))
        n2 = int(input('DIGITE O SEGUNDO NÚMERO: '))
        return n1, n2
    except:
        print('NÃO É POSSIVEL LETRAS!')
        return None, None

def pergunta_cal():
    try:
        n1 = int(input('DIGITE UM NÚMERO: '))
        return n1
    except:
        print('NÃO É POSSIVEL LETRAS!')
        return None

#FUNÇÕES PARA HISTÓRICO
def opc_historico():
    try:
        n = int(input('[1] VER HISTÓRICO\n[2] APAGAR HISTORICO\nESCOLHA A OPÇÃO: '))
        return n
    except:
        print('NÃO É POSSIVEL LETRAS!')
        return None

def opc_ver_apagar(a):
    if (a == 1):
        print('HISTÓRICO:')
        for _ in historico:
            print(_)
    elif (a == 2):
        historico.clear()
        print('HISTÓRICO APAGADO!!!')
    else:
        print('OPCÃO INVÁLIDA!')

#SISTEMA PRINCIPAL
historico = []

while True:
    print('[1] SOMA')
    print('[2] SUBTRAÇÃO')
    print('[3] MULTIPLICAÇÃO')
    print('[4] DIVISÃO')
    print('[5] HISTÓRICO')
    print('[6] SAIR')

    try:
        opc = int(input('ESCOLHA A OPÇÃO: '))
    except:
        print('NÃO É POSSIVEL LETRAS')
        continue

    if (opc == 1):
        n1, n2 = perguntas_cal()
        if n1 is not None:
            print('A SOMA ENTRE OS NÚMEROS: ', calculo_soma(n1, n2))
            historico.append(f'SOMA: {n1} + {n2} = {calculo_soma(n1, n2)}')

    elif(opc == 2):
        n1, n2 = perguntas_cal()
        if n1 is not None:
            print('A SUBTRAÇÃO ENTRE OS NÚMEROS É: ', calculo_sub(n1, n2))
            historico.append(f'SUBTRAÇÃO: {n1} - {n2} = {calculo_sub(n1, n2)}')

    elif (opc == 3):
        n1 = pergunta_cal()
        if n1 is not None:
            print('A TABUADA DESSE NÚMERO É:\n', calculo_mult(n1))
            historico.append(f'TABUADA: {calculo_mult(n1)}')

    elif (opc == 4):
        n1, n2 = perguntas_cal()
        if n1 is not None:
            print(f'A DIVISÃO É: ', calculo_div(n1, n2))
            historico.append(f'DIVISÃO: {n1} / {n2} = {calculo_div(n1, n2)}')

    elif (opc == 5):
        n = opc_historico()
        if n is not None:
            print(opc_ver_apagar(n))

    elif (opc == 6):
        print('SAINDO...')
        break
        
    





















    
