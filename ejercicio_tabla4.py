lista=[]
for x in range (5):
    valor=int(input('Ingrese un numero: '))
    lista.append(valor)
    if lista [x]<0:
        print('No se aceptan numeros negativos, vuelva a digitar.')
        lista [x]=int(input('Por favor digite un numero positivo: '))
while lista[x]<0:
    print('No se aceptan numeros negativos, vuelva a digitar.')
    lista[x]=int(input('Digite un numero positivo: '))
print(lista)        