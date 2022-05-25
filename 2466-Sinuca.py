qntd_de_bolas_inicial = int(input())
cores = list(map(int, input().split()))
fileiras = []

for i in cores:
    fileiras.append(i)

while qntd_de_bolas_inicial > 1:
    fileiras_seguintes = []
    for i in range(qntd_de_bolas_inicial - 1):
        if fileiras[i] == fileiras[i+1]:
            fileiras_seguintes.append(1)
        else:
            fileiras_seguintes.append(-1)
    fileiras = fileiras_seguintes
    qntd_de_bolas_inicial -= 1

if fileiras[0] == 1:
    print("preta")
elif fileiras[0] == -1:
    print("branca")