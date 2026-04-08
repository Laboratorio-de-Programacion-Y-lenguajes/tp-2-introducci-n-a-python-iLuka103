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

**Herramienta**: 

**Prompt usado**:
> 

**Resultado obtenido**:


**¿Lo usaste tal cual o lo modificaste?**


---

### 3 - listas.py

**Herramienta**: 

**Prompt usado**:
> 

**Resultado obtenido**:


**¿Lo usaste tal cual o lo modificaste?**


---

### 4 - diccionarios.py

**Herramienta**: 

**Prompt usado**:
> 

**Resultado obtenido**:


**¿Lo usaste tal cual o lo modificaste?**


---

### 5 - loops.py

**Herramienta**: 

**Prompt usado**:
> 

**Resultado obtenido**:


**¿Lo usaste tal cual o lo modificaste?**


---

### 6 - funciones.py

**Herramienta**: 

**Prompt usado**:
> 

**Resultado obtenido**:


**¿Lo usaste tal cual o lo modificaste?**


---

### 7 - operaciones.py

**Herramienta**: 

**Prompt usado**:
> 

**Resultado obtenido**:


**¿Lo usaste tal cual o lo modificaste?**


---

## Reflexión final

Respondé brevemente (3-5 oraciones):

- ¿Qué aprendiste sobre cómo formular buenos prompts?
- ¿En qué casos la IA fue útil y en cuáles no?
- ¿Qué harías diferente la próxima vez?
