## 1. Introducción a Simpyl
Simpyl es un lenguaje de programación diseñado para ser sencillo, flexible y fácil de entender. Está inspirado en lenguajes funcionales como Scheme, con una sintaxis minimalista que lo hace accesible tanto para programadores principiantes como avanzados.

Simpyl se ejecuta en un intérprete y tiene un enfoque basado en expresiones. Aquí veremos cómo escribir y ejecutar código en Simpyl.

## 2. Sintaxis Básica
Simpyl utiliza una sintaxis basada en paréntesis para definir y ejecutar expresiones. Algunos de los elementos más comunes son:

- Definición de funciones: `(define ...)`
- Asignación de variables: `(define var_name value)`
- Impresión de valores: `(display ...)`
- Llamadas a funciones: `(function_name ...)`

## 3. Comandos Básicos

### 3.1 Definir una Función
La sintaxis para definir una función es:

```scheme
(define (function-name param1 param2 ...)
  body-of-function)
```

Ejemplo:
```scheme
(define (suma a b)
  (+ a b))
```

Llamada:
```scheme
(suma 3 4)  ; Resultado: 7
```

### 3.2 Asignar una Variable
Para asignar un valor a una variable, utilizamos `define`:

```scheme
(define x 10)
```

### 3.3 Imprimir un Valor
El comando `display` se usa para mostrar información en la salida estándar:

```scheme
(display "Hola, mundo!")
```

### 3.4 Llamada a Funciones
Las funciones se llaman con el siguiente formato:

```scheme
(function-name param1 param2 ...)
```

Ejemplo:
```scheme
(suma 5 10)  ; Resultado: 15
```

## 4. Expresiones y Operadores
Simpyl permite realizar operaciones matemáticas con operadores básicos:

- `+` para sumar
- `-` para restar
- `*` para multiplicar
- `/` para dividir
- `modulo` para obtener el módulo
- `expt` para exponenciación

Ejemplo:
```scheme
(define x (+ 5 10))  ; Asigna a x el valor de 5 + 10, es decir, 15
```

## 5. Condicionales (If-Else)
Las decisiones condicionales en Simpyl se manejan con `if`:

```scheme
(if (condition)
    then-expression
    else-expression)
```

Ejemplo:
```scheme
(if (> 10 5)
    (display "10 es mayor que 5")
    (display "10 no es mayor que 5"))
```

## 6. Manejo de Funciones Avanzadas

### 6.1 Funciones con Valores por Defecto
Puedes definir funciones con valores por defecto usando `lambda` y `define`:

```scheme
(define saludar
  (lambda (nombre)
    (display (string-append "Hola, " nombre))))

(saludar "Carlos")  ; Imprime: Hola, Carlos
```

### 6.2 Funciones Recursivas
Las funciones recursivas son aquellas que se llaman a sí mismas dentro de su cuerpo. Aquí tienes un ejemplo de cómo calcular el factorial de un número:

```scheme
(define (factorial n)
  (if (<= n 1)
      1
      (* n (factorial (- n 1)))))
```

Llamada:
```scheme
(factorial 5)  ; Resultado: 120
```

## 7. Manejo de Módulos
En Simpyl, puedes importar módulos externos para extender la funcionalidad de tu programa:

```scheme
(import "module_name")
```

Ejemplo:
```scheme
(import "math")
(display (sqrt 16))  ; Imprime: 4.0
```

## 8. Depuración y Puntos de Interrupción
Simpyl incluye una funcionalidad de depuración para inspeccionar variables y establecer puntos de interrupción.

### 8.1 Inspeccionar una Variable
```scheme
(inspect variable-name)
```

Ejemplo:
```scheme
(inspect x)  ; Imprime el valor de x
```

### 8.2 Puntos de Interrupción
Puedes agregar un punto de interrupción en una línea específica para detener la ejecución del programa:

```scheme
(add-breakpoint line-number)
```

Ejemplo:
```scheme
(add-breakpoint 10)
```

## 9. Manejo de Memoria
El sistema de Simpyl incluye un gestor de memoria que monitorea el uso y ejecuta recolección de basura cuando es necesario. Esto es manejado automáticamente por el sistema.

## 10. Ejemplo Completo
Aquí hay un ejemplo completo que demuestra varias características de Simpyl:

```scheme
(define (suma a b)
  (+ a b))

(define (factorial n)
  (if (<= n 1)
      1
      (* n (factorial (- n 1)))))

(define x 10)
(define y 20)
(define result (suma x y))
(display (string-append "La suma de " (number->string x) " y " (number->string y) " es: " (number->string result)))

(display (string-append "El factorial de 5 es: " (number->string (factorial 5))))
```

Este ejemplo define dos funciones (`suma` y `factorial`), asigna valores a variables y usa `display` para mostrar resultados.

