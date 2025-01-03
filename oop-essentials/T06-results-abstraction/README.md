Se realiza una actualización al script principal **run_regressor_evaluation.py**.

El objeto de **results** del script tenía un tipo de pandas DataFrame, para el cual información importante es un poco inconveniente de recuperar. En particular, se menciona que rescatar el nombre del mejor modelo del dataframe no algo muy trivial. En este apartado se introduce una abstracción para la evaluacion, para hacer esto más conveniente.

* Todavía se tiene acceso al dataframe y todavía se imprime de manera normal, a manera de reporte.
* Adicionalmente, se recupera el nombre del mejor modelo (el que tenga mejor métrica), así como su valor.

De esta forma, el código para la evaluación finalmente es más flexible, donde los parámetros son más fácilmente puestos. Por ejemplo, uno pudiera rápidamente cambiar los parámetros del split y las métricas dentro de las líneas del modelo muy fácilmente. Esta abstracción permite hacer un componente reutilizable, que pueden ser utilizadas en contextos completamente diferentes (ponen de ejemplo una optimización de hiperparámetros de modelos). 

Cada una de las clases que se introdujeron representan conceptos significativos en está área, y cada una tiene un propósito bien definido y razonablemente conciso, haciéndolo relativamente fácil de mantener.