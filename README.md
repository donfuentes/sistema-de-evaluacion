# sistema-de-evaluacion
Sistema de evaluación desarrollado en Python utilizando listas y diccionarios

# Descripción del proyecto
Crea un módulo para un sistema de evaluación educativo que muestre una estructura de preguntas con respuesta de selección múltiple y al final muestre el resultado de cantidad de respuestas correctas y cantidad de respuestas equivocadas, teniendo en cuenta las siguientes condiciones:
* Cada pregunta tiene 4 opciones de respuesta en la cual una es correcta y tres son
erradas.
* A medida que pasa entre las preguntas se van acumulando los resultados correctos.
* Cada evaluación debe tener mínimo 5 preguntas.
* Para cargar las preguntas y opciones de respuesta de las evaluaciones se debe contar con una API local para realizar su lectura y visualización.

# Desarrollo de la solución
Se creó el sistema solicitado utilizando Python. Para lo cual se agregaron las siguientes características:
- Evalúa el mínimo de preguntas y la límita al máximo de preguntas cargadas
- Si no se ingresa un valor permitido (número mayor o igual a 5) se genera una advertencia para que ingrese el nuevo valor. Se tienen 3 oportunidades para ingresar el valor. Si se agotan las oportunidades se sale de la prueba.
- Las preguntas se generan aleatoriamente sin permitir preguntas repetidas
- Se aumentaron las opciones de respuesa a 5 respuestas únicas seleccionadas aleatoriamente de un diccionario de respuestas.
- Se evalúa la validez de la opción de respuesta, permitiendo unicamente respuestas de la A a la E
- Califica la prueba indicando si se aprobó o no mostrando una clasificación en 3 niveles: ALTO, MEDIO y BAJO
- Se remplazó el cambio de preguntas desde una API, por listas y diccionarios.

# Instrucciones

1. Ingresar la cantidad de preguntas. Se tienen 3 oportunidades.

![image](https://user-images.githubusercontent.com/84164187/137815801-b265f34b-ce0c-4aeb-979a-9cedf937c236.png)

2. Ingresar la respuesta de la pegunta. Solo letras de la A a la E.

![image](https://user-images.githubusercontent.com/84164187/137817165-26094041-7819-4031-80a7-8b5968db9ce2.png)

3. Al final podrás ver tus resultados

![image](https://user-images.githubusercontent.com/84164187/137817287-78ed5080-b7b3-435d-9f20-8cff019db6db.png)


