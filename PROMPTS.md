# Registro de Prompts

En este archivo debés documentar los prompts que usaste con herramientas de IA
(GitHub Copilot, ChatGPT, etc.) durante el desarrollo del TP.

**¿Por qué?** Queremos que aprendas a trabajar con IA de forma reflexiva:
que sepas qué le pediste, qué obtuviste, y si tuviste que corregirlo.

---

## Formato para cada entrada

```
### [Número] - [Módulo]

**Herramienta**: GitHub Copilot / ChatGPT / otra

**Prompt usado**:
> Escribí acá exactamente lo que le pediste a la IA

**Resultado obtenido**:
Describí brevemente qué generó (código, explicación, etc.)

**¿Lo usaste tal cual o lo modificaste?**
Explicá qué cambios hiciste y por qué (o por qué no cambiaste nada).
```

---

## Mis prompts

### 1 - variables.py

**Herramienta**: Google Gemini

**Prompt usado**:
> como retornar en python el tipo de dato que ingresas, hacemelo en codigo y explicame paso por paso como funciona, resumido

**Resultado obtenido**: 

Explicación Paso a Paso
Función type(elemento): Es una función propia de Python que analiza el objeto en memoria y devuelve su clase. Por ejemplo, si le pasás un número, te devuelve <class 'int'>.

Atributo .__name__: Como type() devuelve un objeto de clase y vos solo querés el texto (por ejemplo, "int" en lugar de <class 'int'>), usamos este atributo especial que guarda el nombre legible de la clase.

Retorno Dinámico: A diferencia de otros lenguajes donde tenés que declarar el tipo antes, Python averigua el tipo en tiempo de ejecución, lo que hace que esta función sirva para cualquier dato que le envíes.


**¿Lo usaste tal cual o lo modificaste?**
 Ya tenía la función definida, solo necesitaba saber cómo retornar el tipo de valor, que nunca supe hacer.

---

### 2 - condicionales.py

**Herramienta**: Google Gemini

**Prompt usado**:
> Quiero implementar la función es_bisiesto(anio: int) -> bool en Python 3.13.

Antes de escribir el código, haceme 3 preguntas clave para confirmar:

-Cómo manejar los años que son divisibles por 100 pero no por 400 (ejemplo: 1900).

-Será una estructura de código con múltiples if/else anidados o una sola expresión booleana (una sola línea de return).

-Qué tipo de validación debemos hacer si el usuario ingresa un número negativo o un valor que no sea un entero.

**Resultado obtenido**:
1. El filtro del "Siglo" (Divisibilidad por 100 y 400)
Según el calendario gregoriano, los años divisibles por 100 no son bisiestos, a menos que también sean divisibles por 400.

La pregunta: ¿Quieres que la función siga estrictamente la regla gregoriana (donde 1900 es falso y 2000 es verdadero), o necesitas algún manejo especial para fechas históricas muy antiguas?

2. Estilo de implementación
En Python 3.13, la legibilidad es ley, pero hay dos caminos muy comunes para este problema.

Opción A (Estructural): Usar if/else anidados. Es muy fácil de leer paso a paso y de depurar.

Opción B (Pythonic/Funcional): Una sola expresión lógica con and, or y not. Es elegante y concisa.

La pregunta: ¿Con cuál de los dos enfoques te sientes más cómodo para este proyecto?

3. Robustez y validación de tipos
Dado que Python es de tipado dinámico (aunque uses type hints), el usuario podría pasar un string o un número negativo.

La pregunta: ¿Prefieres que la función simplemente lance un error estándar si el dato es inválido, o quieres que manejemos una excepción personalizada (como un ValueError con un mensaje amigable) o que devuelva False por defecto?

**¿Lo usaste tal cual o lo modificaste?**
Ya tenía conocimientos más o menos y me daba una idea de cómo resolverlo, pero igual está el prompt

---

### 3 - listas.py

**Herramienta**: 

**Prompt usado**:
> Estoy resolviendo el ejercicio filtrar_pares(numeros) en Python con estas reglas:

Debe retornar una nueva lista que contenga solo los números pares de la lista original.
Un número es par si el resto de su división por 2 es 0.
¿Podés actuar como mi verificador cognitivo para este problema?

Casos borde: Enumerá qué tipos de listas debería testear (por ejemplo, listas vacías, listas sin pares o listas con números negativos).

Errores típicos: Decime qué fallas comunes ocurren al filtrar (por ejemplo, modificar la lista original por error o problemas con el número 0).

Validación de resultados: Proponé 3 tests con entradas (listas de ejemplo) y las salidas esperadas, pero no escribas el código todavía, solo ayudame a verificar que mi plan lógico sea correcto.

**Resultado obtenido**:
1. Casos Borde (Edge Cases)Para que tu función sea robusta, no basta con probar [1, 2, 3, 4]. Deberías verificar qué sucede con:Lista Vacía ([]): El resultado debería ser otra lista vacía sin lanzar errores.Lista sin Pares ([1, 3, 5, 7]): Debe retornar una lista vacía.Lista de solo Pares ([2, 4, 6]): Debe retornar una copia idéntica (o una nueva lista con los mismos valores).Números Negativos ([-2, -1, 0, 1, 2]): Recordá que $-2$ y $0$ son técnicamente pares.Listas con el número 0: El cero suele confundir, pero $0 \pmod 2 = 0$, por lo que es par.

2. Errores Típicos (Pitfalls)
Estos son los "pecados capitales" que suelen ocurrir en este ejercicio:

Efectos secundarios (Mutación): Modificar la lista numeros original usando .remove() mientras la iterás. Esto hace que el "puntero" del bucle se salte elementos. Regla de oro: Siempre creá una lista nueva.

Confusión de Operadores: Usar / (división flotante) en lugar de % (módulo). Recordá que buscamos que n % 2 == 0.

Olvidar el return: Parece obvio, pero a veces uno imprime los resultados (print) en lugar de devolverlos, lo que rompe la cadena de datos si otra función necesita esa lista.

. Validación de Resultados (Plan de Testeo)Antes de programar, confirmemos que estos resultados son los que esperás:Entrada (Lista original)Proceso LógicoSalida Esperada[1, 2, 3, 4, 5, 6]Filtra 2, 4 y 6[2, 4, 6][0, -2, -3, 10]0, -2 y 10 cumplen la condición[0, -2, 10][1, 7, 13]Ninguno es divisible por 2[]

**¿Lo usaste tal cual o lo modificaste?**
Sinceramente no lo comprendí del todo y le tuve que pedir ayuda a mis compañeros

---

### 4 - diccionarios.py

**Herramienta**: 

**Prompt usado**:
> Generá 5 ejemplos distintos de diccionarios en Python que contengan pares clave-valor de diferentes tipos (por ejemplo, str: int, str: str, int: float).

Para cada ejemplo:

-Mostrá el diccionario original.
-Mostrá cómo quedaría el diccionario invertido (donde lo que era valor ahora sea clave y viceversa).
-Incluí al menos un ejemplo donde los valores originales sean idénticos para ver qué sucede en la inversión.

Finalmente, basándote en estos ejemplos, extraé una regla general o una limitación técnica que deba tenerse en cuenta al implementar la función invertir_diccionario(d).

**Resultado obtenido**:
Ejemplo 1: El Inventario (String a Int)
Este es el caso más común, útil para conteos o stock.

Original: {'manzanas': 50, 'peras': 30, 'naranjas': 25}

Invertido: {50: 'manzanas', 30: 'peras', 25: 'naranjas'}

Ejemplo 2: Diccionario de Traducción (String a String)
Mapeo simple entre palabras de distintos idiomas.

Original: {'red': 'rojo', 'blue': 'azul', 'green': 'verde'}

Invertido: {'rojo': 'red', 'azul': 'blue', 'verde': 'green'}

Ejemplo 3: Escala de Precisión (Int a Float)
Mapeo de identificadores numéricos a valores decimales.

Original: {1: 10.5, 2: 20.75, 3: 5.0}

Invertido: {10.5: 1, 20.75: 2, 5.0: 3}

Ejemplo 4: Colisión de Valores (Valores Idénticos)
¿Qué pasa cuando dos llaves apuntan al mismo valor?

Original: {'Alice': 25, 'Bob': 30, 'Charlie': 25}

Invertido: {25: 'Charlie', 30: 'Bob'}

Nota cognitiva: Observá que 'Alice' desapareció. En Python, al invertir, la última clave procesada pisa a la anterior si los valores eran iguales.

Ejemplo 5: El caso del "Un-hashable" (Valor que no puede ser Clave)
Intentemos usar una lista como valor.

Original: {'id_1': [1, 2, 3], 'id_2': [4, 5, 6]}

Invertido: Error de Python (TypeError: unhashable type: 'list').

Explicación: Una lista es mutable, por lo tanto no puede ser una "clave" en un diccionario.

**¿Lo usaste tal cual o lo modificaste?**


---

### 5 - loops.py

**Herramienta**: google gemini

**Prompt usado**:
> P1: como obtengo determinados N numeros de una lista?
P2: como hago para que al determinar un numero por finalizado, no me tome en cuenta los numeros repetidos o negativos?

**Resultado obtenido**:
P1: ¿Cómo obtengo determinados N números de una lista?La forma más eficiente es mediante el slicing. La sintaxis básica es lista[inicio:fin].Los primeros $N$ elementos: lista[:N]Los últimos $N$ elementos: lista[-N:]Un rango específico: lista[2:5] (obtiene desde el índice 2 hasta el 4).

P2: ¿Cómo evitar números repetidos o negativos?Aquí es donde aplicamos la lógica de limpieza. Para resolver esto, lo más "Pythonic" es seguir este orden: Filtrar negativos → Eliminar repetidos → Obtener los N números.El "Combo" de herramientas:Sets (Conjuntos): Al transformar una lista a un set(), Python elimina automáticamente todos los duplicados.List Comprehension: Una forma rápida de filtrar los negativos.

**¿Lo usaste tal cual o lo modificaste?**
lo tuve en cuenta tal cual

---

### 6 - funciones.py

**Herramienta**: google gemini

**Prompt usado**:
> > Necesito una función para `def memoizar(func): cache = {}` en Python 3.13.  
> Quiero comparar enfoques y elegir uno simple y performante para un TP:  
> - split + count  
> - recorrer manualmente  
> - regex 
Analiza pros y contras(performance + simplicidad + edge cases como puntuación)
Luego recomendá UNO y escribí el código con docstring, No uses librerias externas

**Resultado obtenido**:
Asumiendo que el objetivo es contar la frecuencia de palabras en un texto (el uso más común para comparar estos métodos)

**Muestra una tabla de Split + Count, recorrer manualmente y regex**

Recomendación: Recorrido Manual con Diccionario
Para un TP, te recomiendo el Recorrido Manual con un Diccionario.
¿Por qué?

Eficiencia Lineal: A diferencia de count, que es lentísimo en textos largos, el diccionario busca términos de forma casi instantánea.

Sin Librerías: Regex requiere import re. El recorrido manual es Python puro.

Transparencia: Demuestra que entendés cómo funcionan las estructuras de datos.

**¿Lo usaste tal cual o lo modificaste?**


---

### 7 - operaciones.py

**Herramienta**: 

**Prompt usado**:
> Tengo que implementar es_palindromo(texto: str) -> bool. Compará estos 3 enfoques:

A) Enfoque Slicing: Usar texto[::-1] para comparar el string con su versión invertida.

B) Enfoque Iterativo (Two-Pointers): Usar un bucle y comparar caracteres desde los extremos hacia el centro (índice i e índice -i-1) sin crear copias del string.

C) Enfoque Funcional: Usar reversed() y all() para comparar las mitades del texto.

Analizá pros y contras (performance de memoria, legibilidad y facilidad de testeo). Elegí el más adecuado para un entorno de producción con textos muy largos y escribí el código final con pytest.

**Resultado obtenido**:
Implementar un verificador de palíndromos es un ejercicio clásico para entender la gestión de memoria en Python. Cuando hablamos de entornos de producción con textos muy largos, la eficiencia de memoria pasa a ser el factor determinante.

Aquí tenés el análisis comparativo de los tres enfoques:

**lista de criterios, memoria, rendimiento, legibilidad y textos largos**

**¿Lo usaste tal cual o lo modificaste?**
lo usé tal cual, tomé en cuenta como está escrito en readme.md pero lo modifiqué a uno de los problemas

---

## Reflexión final

Respondé brevemente (3-5 oraciones):

- ¿Qué aprendiste sobre cómo formular buenos prompts?
- ¿En qué casos la IA fue útil y en cuáles no?
- ¿Qué harías diferente la próxima vez?

Una vez sabes lo que buscas o las dudas que queres hacerle es más sencillo pedir que te explique de cierta forma para poder entenderlo, usualmente te tira lo más recomendado y hasta incluso no se entiende, la ia fue util en mayoría de casos pero en unos cuantos es complicado interpretarlo bien y recurro a que me lo explique mejor, lo que haría diferente la próxima es darle más limitaciones y buscar la forma de que lo explique con alguna comparativa o analogia con un lenguaje que yo ya entienda y pueda interpretar facilmente