import collections
erro, valor = map(int, input().split())
lista_vazia = []

while erro!= 0 and valor != 0:
    erro = str(erro)
    valor = str(valor)
    for i in range(len(str(erro))):
        valor = valor.replace(erro[i],"")
    
    lista_com_zeros = ["0"] * len(str(valor))
    if collections.Counter(str(valor)) == collections.Counter(lista_vazia):
        print(0)
    
    elif collections.Counter(str(valor)) == collections.Counter(lista_com_zeros):
        print(0)
    
    elif collections.Counter(str(valor)) != collections.Counter(lista_vazia) and collections.Counter(str(valor)) != collections.Counter(lista_com_zeros):
        print(int(valor))
    
    erro, valor = map(int, input().split())