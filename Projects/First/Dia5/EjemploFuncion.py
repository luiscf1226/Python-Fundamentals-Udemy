precios_cafe=[('capuchino',1.5),('Expresso',1.2),('Moka',1.9)]
def cafe_mas_caro(listap):
    precio_mayor=0
    cafec=''
    for cafe,precio in listap:
        if precio>precio_mayor:
            precio_mayor=precio
            cafec=cafe
        else:
            pass

    return (cafec,precio_mayor)
print(cafe_mas_caro(precios_cafe))