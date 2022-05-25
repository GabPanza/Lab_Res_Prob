qntd_de_palavras = int(input())

for i in range(qntd_de_palavras):
    texto = input()
    qntd_que_avanca = int(input())
    palavra_decodificada = ""
    for j in texto:
        posicao = ord(j)-qntd_que_avanca

        if posicao < 65:
            palavra_decodificada += chr(91-(65-posicao))
        else:
            palavra_decodificada += chr(ord(j)-qntd_que_avanca)
    print(palavra_decodificada)