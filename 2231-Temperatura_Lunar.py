lista_menores_maiores = []
cont=1
while True:
    N, M = map(int, input().split())
    temperatura = []
    somas= []
    soma=0
    maior= -201
    menor = 201
    if N==0 and M==0:
        break
    else:
        for k in range(N):
            temperatura.append(int(input()))    
        for j in range(M):
            soma += temperatura[j]
        somas.append(soma)
        for i in range(N-M):
            soma += temperatura[i+M] - temperatura[i]
            somas.append(soma)    
        for l in somas:
            if l > maior:
                maior = l
            if l < menor:
                menor = l    
        # Salvo os maiores e menores
        lista_menores_maiores.append(int(menor/M))
        lista_menores_maiores.append(int(maior/M))

for i in range(0,len(lista_menores_maiores),2):
    print("Teste {}".format(cont))
    print(lista_menores_maiores[i], lista_menores_maiores[i+1])
    print()
    cont+=1