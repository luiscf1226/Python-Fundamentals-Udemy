from collections import Counter,defaultdict,namedtuple
numeros=[1,2,3,4,5,65,5,5,5,4,4,4]
print(Counter(numeros))
print(Counter('missisipi'))
frase =' al pan pan y al vino vino'
print(Counter(frase.split()))
serie=Counter([1,1,1,1,1,12,2,2,2,3,3,3,4,4])
print(list(serie))
print(serie.most_common())

mi_dic=defaultdict(lambda :'nada')
mi_dic['uno']='verde'
print(mi_dic['dos'])

mi_tupla=(500,18,34)
print(mi_tupla[1])

Persona=namedtuple('Persona',['nombre','altura','peso'])
ariel=Persona('Ariel',1.76,79)

print(ariel.altura)
