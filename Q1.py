import sys
espessuras = sys.stdin.readline()
listaEspessura = espessuras.split()
largura = float(listaEspessura[0])
comprimento = float(listaEspessura[1])

historico = str(sys.stdin.readline())
cartografia = { 90: "O",  180 : "N" , 270 : "L",  0: "S"}
posicao = 180
coordX = 0
coordY = 0

for i in range(len(historico)):
    if historico[i]=='D':
        posicao += 90
    if historico[i] == 'E':
        posicao -= 90
    if historico[i] == 'F':
        if cartografia[posicao%360] == "N" and (coordY+1)< comprimento:
            coordY += 1
        if cartografia[posicao%360] == "S" and (coordY-1) >= 0.0:
            coordY -= 1
        if cartografia[posicao%360] == "L" and (coordX+1)< largura:
            coordX += 1
        if cartografia[posicao%360] == "O" and (coordX-1) >= 0.0:
            coordX -= 1
    if historico[i] == 'T':
        if cartografia[posicao%360] == "N" and (coordY-1) >= 0.0:
            coordY -= 1
        if cartografia[posicao%360] == "S" and (coordY+1)< comprimento:
            coordY += 1
        if cartografia[posicao%360] == "L" and (coordX-1) >= 0.0:
            coordX -= 1
        if cartografia[posicao%360] == "O" and (coordX+1)< largura:
            coordX += 1

print (f'{cartografia[posicao%360]} {coordX} {coordY}')
