# sistema-de-evaluacion
Sistema de evaluación desarrollado en Python utilizando con listas y diccionarios

# Descripción del proyecto
Crea un módulo para un sistema de evaluación educativo que muestre una estructura de preguntas con respuesta de selección múltiple y al final muestre el resultado de cantidad de respuestas correctas y cantidad de respuestas equivocadas, teniendo en cuenta las siguientes condiciones:
* Cada pregunta tiene 4 opciones de respuesta en la cual una es correcta y tres son
erradas.
* A medida que pasa entre las preguntas se van acumulando los resultados correctos.
* Cada evaluación debe tener mínimo 5 preguntas.
* Para cargar las preguntas y opciones de respuesta de las evaluaciones se debe contar con una API local para realizar su lectura y visualización.

# Desarrollo de la solución
Se creó el sistema solicitado utilizando Python. Para lo cual se agregaron las siguientes características:
- Evalúa el mínimos de preguntas y la límita al máximo de preguntas cargadas
- Las preguntas se generan aleatoriamente sin permitir preguntas repetidas
- Se aumentaron las opciones de respuesa a 5 respuestas únicas seleccionadas aleatoriamente de un diccionario de preguntas.
- Se evalúa la validez de la opción de respuesta, permitiendo unicamente respuestas de la A a la E
- Indica si la pruueba se aprobó indicando una clasificación en 3 niveles: ALTO, MEDIO y BAJO

# Instrucciones
