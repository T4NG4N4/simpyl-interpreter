```markdown name=GUIDE.md
## 1. Introducción a Simpyl
Simpyl es un lenguaje de programación diseñado para ser sencillo, flexible y fácil de entender. Está inspirado en lenguajes funcionales como Scheme, con una sintaxis mínima que hace que sea accesible tanto para programadores principiantes como avanzados.

Simpyl se ejecuta en un intérprete y tiene un enfoque basado en comandos. Aquí veremos cómo escribir y ejecutar código en Simpyl.

## 2. Sintaxis Básica
Simpyl utiliza una sintaxis basada en paréntesis para definir y ejecutar expresiones. Los comandos más comunes son:

- Definición de funciones: `(define ...)`
- Asignación de variables: `(var_name = ...)`
- Impresión de valores: `(print ...)`
- Llamadas a funciones: `(function_name ...)`

## 3. Comandos Básicos

### 3.1 Definir una Función
La sintaxis para definir una función es:

```simpyl
(define (function_name (param1, param2 ...)): (body_of_function))
```

Ejemplo:
```simpyl
(define (suma (a, b)):
    (a + b))
```

En este caso, la función `suma` recibe dos parámetros `a` y `b`, y devuelve su suma.

Ejemplo de llamada:
```simpyl
(suma (3, 4))  ; Resultado: 7
```

### 3.2 Asignar una Variable
Para asignar un valor a una variable, utilizamos la siguiente sintaxis:

```simpyl
(var_name = expression)
```

Ejemplo:
```simpyl
(x = 10)
```
Esto asigna el valor 10 a la variable `x`.

### 3.3 Imprimir un Valor
El comando `print` se usa para mostrar información en la salida estándar:

```simpyl
(print (expression))
```

Ejemplo:
```simpyl
(print ("Hola, mundo!"))  ; Imprime: Hola, mundo!
```

### 3.4 Llamada a Función
Las funciones se llaman con el siguiente formato:

```simpyl
(function_name (param1, param2 ...))
```

Ejemplo:
```simpyl
(suma (5, 10))  ; Resultado: 15
```

## 4. Expresiones y Operadores
Simpyl permite realizar operaciones matemáticas con operadores básicos como:

- `+` para sumar
- `-` para restar
- `*` para multiplicar
- `/` para dividir
- `%` para obtener el módulo
- `**` para exponenciación

Ejemplo:
```simpyl
(x = (5 + 10))  ; Asigna a x el valor de 5 + 10, es decir, 15
```

## 5. Condicionales (If-Else)
Simpyl también permite realizar decisiones condicionales usando `if`, `else` y `elif` (no obligatorio, pero útil en casos complejos):

```simpyl
(if (condition)
    (then_expression)
    (else_expression))
```

Ejemplo:
```simpyl
(if (10 > 5)
    (print ("10 es mayor que 5"))
    (print ("10 no es mayor que 5")))
```

## 6. Manejo de Funciones Avanzadas

### 6.1 Funciones con Parámetros Opcionales
Puedes definir funciones con parámetros opcionales y asignarles valores por defecto.

Ejemplo:
```simpyl
(define (saludar (nombre "Desconocido"))
    (print (string-append "Hola, " nombre)))
    
(saludar ("Carlos"))  ; Imprime: Hola, Carlos
(saludar)             ; Imprime: Hola, Desconocido
```

### 6.2 Funciones Recursivas
Las funciones recursivas son aquellas que se llaman a sí mismas dentro de su cuerpo. Aquí tienes un ejemplo de cómo hacer una función recursiva para calcular el factorial de un número:

```simpyl
(define (factorial n)
    (if (n <= 1)
        1
        (* n (factorial (n - 1)))))
```

Llamada:
```simpyl
(factorial 5)  ; Resultado: 120
```

## 7. Manejo de Módulos
En Simpyl, puedes importar módulos externos para extender la funcionalidad de tu programa.

```simpyl
(import ("module_name"))
```

Ejemplo:
```simpyl
(import ("math"))
(print (math.sqrt 16))  ; Imprime: 4.0
```

## 8. Depuración y Puntos de Interrupción
Simpyl incluye una funcionalidad de depuración para inspeccionar variables y establecer puntos de interrupción.

### 8.1 Inspeccionar una Variable
```simpyl
(inspect (variable_name))
```

Ejemplo:
```simpyl
(inspect (x))  ; Imprime el valor de x
```

### 8.2 Puntos de Interrupción
Puedes agregar un punto de interrupción en una línea específica para detener la ejecución del programa:

```simpyl
(add-breakpoint -line_number-)
```

Ejemplo:
```simpyl
(add-breakpoint -10-)
```

## 9. Funciones Adicionales

### 9.1 Habilitar/Deshabilitar el Modo de Depuración
Para habilitar el modo de depuración:
```simpyl
(enable-debug)
```

Para deshabilitar el modo de depuración:
```simpyl
(disable-debug)
```

### 9.2 Eliminar un Punto de Interrupción
Para eliminar un punto de interrupción:
```simpyl
(remove-breakpoint -line_number-)
```

Ejemplo:
```simpyl
(remove-breakpoint -10-)
```

### 9.3 Manejo de Memoria
El sistema de Simpyl incluye un gestor de memoria que monitorea el uso y ejecuta recolección de basura cuando es necesario. Esto es manejado automáticamente por el sistema.

## 10. Ejemplo Completo
Aquí hay un ejemplo completo que demuestra varias características de Simpyl:

```simpyl
(define (suma (a, b)):
    (a + b))

(define (factorial n)
    (if (n <= 1)
        1
        (* n (factorial (n - 1)))))

(x = 10)
(y = 20)
(result = (suma (x, y)))
(print (string-append "La suma de " x " y " y " es: " result))

(print (string-append "El factorial de 5 es: " (factorial 5)))
```

Este ejemplo define dos funciones (`suma` y `factorial`), asigna valores a variables, y utiliza la función `print` para mostrar resultados.
```
