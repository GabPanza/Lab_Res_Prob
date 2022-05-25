Mx, My, Rx, Ry = map(int, input().split())
coordenada_x = Rx - Mx
coordenada_y = Ry - My

if coordenada_x < 0:
    coordenada_x = (Rx - Mx) * (-1)
if coordenada_y < 0:
    coordenada_y = (Ry - My) * (-1)

cruzamentos = coordenada_x + coordenada_y

print(cruzamentos)
