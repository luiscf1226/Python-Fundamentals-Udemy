from pathlib import Path
ruta = Path("C:/Users/Usuario/Desktop")
Navegación
ruta = Path("C:/Users/Usuario/Desktop") / "archivo.txt"
Es posible concatenar objetos Path y strings con el delimitador "/" para construir rutas
completas.
Algunos métodos y propiedades sobre objetos Path
read_text( ): lee el contenido del archivo sin necesidad de abrirlo y cerrarlo
name: devuelve el nombre y extensión del archivo
suffix: devuelve la extensión del archivo (sufijo)
stem: devuelve el nombre del archivo sin su extensión (sufijo)
exists( ): verifica si el directorio o archivo al que referencia el objeto Path existe y devuelve
un booleano de acuerdo al resultado (True/False)