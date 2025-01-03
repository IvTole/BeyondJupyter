Se trabaja con la parte de carga de datos. Estas rutinas se encuentran en la carpeta ``songpop``, y se compone de tres archivos,

* **__init__.py**. Este archivo es utilizado para indicar que una carpeta debe de ser tratada como un paquete. En versiones anteriores de Python, la presencia de este archivo era obligatoria, y aunque actualmente ya no es necesario para paquetes simples, sigue siendo útil para personalizar y estructurar paquetes.

* **config.py**. Este archivo incluye funciones para regresar la localización de los datos utilizados, y no tener errores a la hora de utilizar paths relativos para localizar los datos.

* **data.py**. Este archivo incluye funciones relacionadas con el preprocesamiento de los datos. Dentro se encuentran las siguientes funciones.

1. El método \__init__(self) es un **método especial** (dunder o mágicos) que se utiliza para inicializar un nuevo objeto después de que se ha asignado memoria para él. En particular, dentro de una clase de Python, este es llamado el **constructor** de la clase. Se ejecuta automáticamente cuando se crea una instancia de la clase y sirve para inicializar los atributos del objeto, configurarlo, etc.

Cada una de las funciones definidas dentro de los archivos .py incluyen lo que se denomina un ``docstring``(documentation string, lo que se encuentra entre comillas triples ''' ó """). Es una cadena de texto utilizada para describir el propósito y comportamiento de la función, clase o módulo donde se encuentra. Una de los objetivos es documentar el propósito de la función y hacer accesible esta información mediante la función ``help()`` o similares.