intNCamas = []
precoCamas = []
camas = []
cama = False
participantes, orcamento, NHotel, NSemanas = map(int, input().split())

for i in range(NHotel):
    precoPer = int(input())
    intNCamas = list(map(int, input().split()))
    precoTotal = participantes * precoPer
    for k in intNCamas:
        if participantes <= k and precoTotal <= orcamento:
            camas.append(precoTotal)
            precoCamas = set(camas)
            cama = True
menor = 500000
for g in precoCamas:
    if g < menor:
        menor = g
if cama:
    print(menor)
else:
    print("stay home")
