def preencheTemp(temperatura):
    for k in range(N):
        temperatura.append(int(input()))
    return temperatura

def calculaSomasTemp(temperatura):
    somas = []
    for i in range(N-(M-1)):
        soma=0
        for j in range(i, (i+M)):
            soma += temperatura[j]
        somas.append(soma)
    return somas

def calcMaiorMenor(somas, maior, menor):
    for i in somas:
        if i > maior:
            maior = i
        if i < menor:
            menor = i
    return maior,menor

cont=0
N, M = list(map(int, input(). split()))
while N!=0 and M!=0:
    temperatura = []
    maior= -201
    menor = 201
    
    # Chamo minhas funçoes
    temperatura = preencheTemp(temperatura)
    somas = calculaSomasTemp(temperatura)
    maior,menor = calcMaiorMenor(somas,maior,menor)
    
    # Imprimo os testes
    cont += 1
    print ("Teste",cont)
    print(int(menor/M), ' ', int(maior/M), '\n')
    N, M = list(map(int, input(). split()))