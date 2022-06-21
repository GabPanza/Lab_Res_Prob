def preencheTemp(N):
    temperatura = []
    for k in range(N):
        temperatura.append(int(input()))
    return temperatura

def calculaSomasTemp(N,M,temperatura):
    somas = []
    soma=0
    for j in range(M):
        soma += temperatura[j]
    somas.append(soma)
    for i in range(N-M):
        soma += temperatura[i+M] - temperatura[i]
        somas.append(soma)
    return somas

def calcMaiorMenor(somas, maior, menor):
    for i in somas:
        if i > maior:
            maior = i
        if i < menor:
            menor = i
    return maior,menor

lista_menores_maiores = []
N, M = map(int, input().split())
while N!=0 and M!=0:
    maior= -201
    menor = 201
    
    # Chamo minhas funçoes
    temperatura = preencheTemp(N)
    somas = calculaSomasTemp(N,M,temperatura)
    maior,menor = calcMaiorMenor(somas,maior,menor)
    
    # Salvo os maiores e menores
    lista_menores_maiores.append(int(menor/M))
    lista_menores_maiores.append(int(maior/M))
    
    # Reseto o loop
    N, M = map(int, input().split())
cont=1
for i in range(0,len(lista_menores_maiores),2):
    print("Teste", cont)
    print(lista_menores_maiores[i], lista_menores_maiores[i+1])
    print()
    cont+=1