Se realiza una actualización al script principal **run_regressor_evaluation.py**.

Hasta el momento, la métrica utilizada (mean absolute error MAE) estaba fija para todo. Calcular una nueva métrica (como R2, o root mean square error RMSE) sólo es posible modificando la clase de ModelEvaluation directamente, y no de forma dinámica. Para solucionar esto se generaliza la lógica de la evaluación para hacer configurable.

Se provee una o más métricas para evaluar el modelo, todo esto puesto en una nueva clase ``Metric``. Cada métrica elegida tiene que tener definido lo siguiente:

* El cálculo de la métrica (método ``compute_value``dentro de la clase).
* Si una buena métrica es un número menor o mayor (método ``is_larger_better``dentro de la clase).
* El nombre de la métrica para ponerlo en una tabla, para poder reportarlo (método ``get_name``dentro de la clase).

En el contexto de una clase, el símbolo ``@``se usa comúnmente como un **decorador** de un método. Es una forma de modifucar o extender el comportamiento de una función. En este caso particular, se utiliza **@abstractmethod**, que es una clase base abstracta (ABC) en python. Es una clase que no puede ser instanciada directamente y está diseñada para ser heredada por otras clases. Puedo contener métodos abstractos, declarados pero no implementados, que las subclases deben implementar. Pueden contener métodos concretos, con implementación que pueden ser heredados directamente por las subclases. 
Todo esto obliga a las subclases a implementar una interfaz común.