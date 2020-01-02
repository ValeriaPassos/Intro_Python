#lista

#select sorted

lista = [500,2,3,9,23,70,3,2,1]

for i in range(i+1,len(lista)):

    menor = i

    for j in range(len(lista)):
        
        if lista[j] < lista[menor]:
            menor = j
            
    if lista[i] != lista[menor]:        
        aux = lista[i]
        lista[i] = lista[menor]
        lista[menor] = aux

    print(lista)
