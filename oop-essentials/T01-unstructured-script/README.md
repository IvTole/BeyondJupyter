Se considera un script **run_regressor_evaluation.py** sin mucha estructura. Hay una sola función main que hace todo lo siguiente:

* Carga un dataset
* Se escalan los datos
* Hace un split del dataset
* Se crean y se evaluan 4 tipos de modelos

Hay varios puntos a tratar,

* La legibilidad, aunque el código no es muy extenso.
* Hay algo de repetición. Se repite el mismo código para los cuatro modelos
* Si alguien quisiera modificar los parámetros de la evaluación, como la métrica, uno tendría que cambiar los cuatro modelos.
* No hay parametrización y todos los parametros de la evaluacion se encuentran fijos
* No hay una forma simple de reutilizar el código para la evaluación.
* Todo el pipeline se encuentra "hard-coded" y se usa para todos los modelos de manera simultánea. No hay una manera simple de adaptar el pre-procesamiento solamente para un modelo en específico.
