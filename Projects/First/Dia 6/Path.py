from pathlib import Path
base=Path.home()
guia=Path(base,"Barcelona","Sagrada_Familia",Path("Madrid.txt"))
guia2=guia.with_name("La_Pedrera.txt")
print(base)
print(guia)
print(guia.parent)
print(guia2)