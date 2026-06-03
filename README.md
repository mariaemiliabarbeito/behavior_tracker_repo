# behavior\_tracker\_repo

Integrantes: Maria Emilia Barbeito y Matilde Urrestarazu

Detalle del proyecto:
Objetivo: el objetivo del trabajo es analizar el comportamiento de los usuarios en el uso de las aplicaciones. Los datos se obtienen desde un archivo CSV, el cual contiene por participante su registro de uso de las aplicaciones. Los datos son id, fecha, aplicacion, cantidad de uso, tiempo de uso. Primero se leerá el archivo y cada linea se transforma en un registro. Luego se validara que cada unon de  los datos sean correctos y que esten en el tipo de dato correspondiente. Otra funcion, sera la encargada de seleccionar los datos de un participante especifico. Finalmente se calculara el tiempo total de uso de las aplicaciones, se calculara el promedio, y se calculara la cantidad de uso por aplicacion.

"Errores y Validaciones":

cargar\_datos: identificamos filenotfounderror para que aparezca en caso que el archivo no exista. También Exception por si no se logra abrir el archivo. Por otro lado, también se utilizó Valueerror por si el archivo se encuentra vacío.

parsear\_linea: se utilizó valué error por si la línea está vacía o si no tiene la cantidad de columnas necesarias

validar\_datos: identificamos errores como ValueError para controlar que los datos esten dentro del valor correcto. Tambien se lo utilizo para verificar que sea del tipo de dato correcto
TypeError: se lo utilizo para verificar que el valor sea del tipo de dato correcto

metricas: indentificamos ZeroDivisionError para el promedio. De esta manera si el divisor es igual a cero salta este error.
todas las funciones tienen un except exception por si no se atrapo algun error inesperado.

Uso de IA: Se la utilizó como herramienta de consulta pero no se hizo “copy, paste” de ninguna parte del código. Si nos surgia alguna duda a medida que realizamos el trabajo, le preguntabamos si estaba bien encaminado lo que pensamos. También se tomaron recomiendaciones como: encontrado = False en la función filtrar\_por participante porque se nos dificultó pensar esa parte del codigo y luego de entenderlo nos pareció la mejor alternativa. Además, antes de hacer main se utilizó chat para entender la teoría de cómo manejar los errores en el programa principal y después nosotras pensamos cómo aplicarlo al trabajo que estamos realizando.
En  carga\_datos reemplazamos como leíamos el archivo con “with open” dentro de la función cargar datos que también generaba una lista de diccionario con los datos de los participantes a partir de un archivo por “ módulo os” y pandas. Pandas recibe la ruta correcta del archivo, lo abre, lee y devuelve un DataFrame.

Cambios que se harían usando Pandas:
En procesamiento\_datos  se reemplazará todo lo de la función filtrar por participante utilizando Pandas pasándole el filtro del participante que ingresa el usuario para conseguir  la serie del Data Frame filtrada.

En validacion\_datos en vez de recorrer registro por registro, ahora recorre columna por columna y en cada una se valida lo que es necesario.

En metricas,

calcular\_tiempo\_total:  antes teníamos una lista de diccionarios y ahora tiempo total es una columna así que directamente se  suman todos los valores de la columna.

En calcular\_promedio\_uso :  En vez de recorrer con un for , hacemos la suma directamente de las columna cantidad\_uso.

calcular\_uso\_por\_app: En vez de utilizar el for y realizar el diccionario manualmente ahora,  agrupamos con groupby las apps y la cantidad de uso , y sumamos el uso de cada app.

Main: Main también se simplifica porque las funciones trabajan con Dataframe y no con listas y diccionarios



En cuanto a los errores:

Antes: los errores podian surgir de listas y diccionarios

Ahora:  De los DataFrames por ejemplo estar vacios o no tener las columnas necesarias



**Actualización con streamlit:**

Guia de Ejecución de la Interfaz web

Streamlit es una librería de Python para crear apps web simples. Permite construir dashboards. Con Streamlit se puede: subir archivos CSV, mostrar tablas ,mostrar métricas ,agregar filtros, mostrar gráficos y  crear una app interactiva.

El comando que debe correr el usuario en la terminal para desplegar el sistema es el siguiente:

En primer lugar se debe asegurar de tener Streamlit instalado, si no, correr en la terminal: pip install streamlit

Para correr el dashboard en la terminal donde esta el archivo app.py se debe correr: streamlit run app.py . Al hacer esto se abrirá el dashboard en el buscador (google, safari, etc). Si no se abre solo, se debe copiar la direccion que aparece en la terminal y pegarla en el buscador

