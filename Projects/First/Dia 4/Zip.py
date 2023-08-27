nombres=['Ana','Hugo','Valeria']
edad=[23,13,16]
ciudades=['USA','Mexico','HND']

combinados=list(zip(nombres,edad,ciudades))
print(combinados)
for n,e,c in combinados:
    print(n+" tiene "+str(e)+ " anios y vive en : "+c)
