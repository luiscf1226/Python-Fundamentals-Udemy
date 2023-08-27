diccionario={'c1':'valor1','c2':'valor2'}
print(diccionario)
resultado=diccionario['c1']
print(resultado)

cliente={'nombre':'Juan','apellido':'Perez','peso':120,'talla':12.3}
consulta=cliente['nombre']
print(consulta)
dic={'c1':55,'c2':[10,20,30],'c3':{'s1':100,'s2':200}}
print(dic['c2'][1])
dic2={'c1':['a','b','c'],'c2':['d','e','f']}
print(dic2['c2'][1].upper())
dic={1:'a',2:'b'}
dic[3]='c'
print(dic)
dic[2]='B'
print(dic.keys())
print(dic.values())