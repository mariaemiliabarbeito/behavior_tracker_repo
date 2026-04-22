# behavior_tracker_repo

Integrantes: Maria Emilia Barbeito y Matilde Urrestarazu

Detalle del proyecto:
Objetivo: el objetivo del trabajo es analizar el comportamiento de los usuarios en el uso de las aplicaciones. Los datos se obtienen desde un archivo CSV, el cual contiene por participante su registro de uso de las aplicaciones. Los datos son id, fecha, aplicacion, cantidad de uso, tiempo de uso. Primero se leerá el archivo y cada linea se transforma en un registro. Luego se validara que cada unon de  los datos sean correctos y que esten en el tipo de dato correspondiente. Otra funcion, sera la encargada de seleccionar los datos de un participante especifico. Finalmente se calculara el tiempo total de uso de las aplicaciones, se calculara el promedio, y se calculara la cantidad de uso por aplicacion. 

"Errores y Validaciones":

cargar_datos: identificamos filenotfounderror para que aparezca en caso que el archivo no exista. También Exception por si no se logra abrir el archivo. Por otro lado, también se utilizó Valueerror por si el archivo se encuentra vacío.

parsear_linea: se utilizó valué error por si la línea está vacía o si no tiene la cantidad de columnas necesarias

validar_datos: identificamos errores como ValueError para controlar que los datos esten dentro del valor correcto. Tambien se lo utilizo para verificar que sea del tipo de dato correcto
TypeError: se lo utilizo para verificar que el valor sea del tipo de dato correcto

metricas: indentificamos ZeroDivisionError para el promedio. De esta manera si el divisor es igual a cero salta este error.
todas las funciones tienen un except exception por si no se atrapo algun error inesperado.

Uso de IA: Se la utilizó como herramienta de consulta pero no se hizo “copy, paste” de ninguna parte del código. Si nos surgia alguna duda a medida que realizamos el trabajo, le preguntabamos si estaba bien encaminado lo que pensamos. También se tomaron recomiendaciones como: encontrado = False en la función filtrar_por participante porque se nos dificultó pensar esa parte del codigo y luego de entenderlo nos pareció la mejor alternativa. Además, antes de hacer main se utilizó chat para entender la teoría de cómo manejar los errores en el programa principal y después nosotras pensamos cómo aplicarlo al trabajo que estamos realizando.
