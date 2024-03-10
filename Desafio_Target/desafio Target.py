
def menu():
    questao = input("Menu : \n 1. Questão 1 \n 2. Questão 2 \n 3. Questão 3 \n 4. Questão 4 \n 5. Questão 5 \n Digite o numero referente a questão desejada ou 0 para sair! ")
    return int(questao)
def primeiraQuestao():

    indice = 13
    soma = 0
    k = 0

    while k < indice:
        k = k + 1

        soma = soma + k

    return print('RESPOSTA: O resultado da soma é: ',  soma)

def segundaQuestao():

    num = int(input("Qual o numero a ser verificado?"))
    if isFibonacci(num):
        return print("RESPOSTA: O numero faz parte da sequência de Fibonacci!")
    else:
        return print("RESPOSTA: O numero não faz parte da sequência de Fibonacci!")

def isFibonacci(num):
    aux = [0, 1]
    n = 0
    while aux[n] <= num:

        if aux[n] == num:
            return True
        elif n == 1:
            aux.append(1)
        elif n >= 2:
            prox = aux[n] + aux[n-1]
            aux.append(prox)

        n = n + 1

    return False


def quintaQuestao():
    f = str(input("Digite a palavra a ser invertida: "))
    oldF = f
    aux = []
    n = 0
    while len(f) > 0:
        aux.append(f[-1])
        f = f[:-1]
    resultado = ''.join(aux)
    return print("RESPOSTA: a palavra ", oldF, "invertida fica:", resultado)



play = True
while play:
    questao = menu()
    if questao == 0:
        print("Finalizando a aplicação. Até mais! :)")
        play = False
    elif questao == 1:
        primeiraQuestao()

    elif questao == 2:
        segundaQuestao()

    elif questao == 3:
        print("A resposta para a Terceira questão está no arquivo READ ME :)")

    elif questao == 4:
        print("A resposta para a Quarta questão está no arquivo READ ME :)")

    elif questao == 5:
        quintaQuestao()

    else:
        print("Invalido, por favor tente novamente")




