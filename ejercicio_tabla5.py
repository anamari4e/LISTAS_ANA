p=input('Digite la cadena: ')
p1=p.split()
p1=list(map(str.upper,p1))
print(p1)
sinduplicado=set(p1)
print(sinduplicado)