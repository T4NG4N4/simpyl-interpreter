# Guía de Simpyl

## 1. Introducción a Simpyl
Simpyl es un lenguaje de programación diseñado para ser sencillo, flexible y fácil de entender. Está inspirado en lenguajes funcionales como Scheme, con una sintaxis minimalista que lo hace accesible tanto para programadores principiantes como avanzados.

Simpyl se ejecuta en un intérprete y tiene un enfoque basado en expresiones. Aquí veremos cómo escribir y ejecutar código en Simpyl.

## 2. Sintaxis Básica
Simpyl utiliza una sintaxis basada en paréntesis para definir y ejecutar expresiones. Algunos de los elementos más comunes son:

- Definición de funciones: `(define ...)`
- Asignación de variables: `(define var_name value)`
- Impresión de valores: `(print ...)`
- Llamadas a funciones: `(function_name ...)`
- Condicionales: `(if condition then-expression else-expression)`
- Módulos: `(import module_name)`

## 3. Comandos Básicos

### 3.1 Definir una Función
La sintaxis para definir una función es:

```scheme
(define (function-name param1 param2 ...)
  body-of-function)
Ejemplo:

scheme
Copiar
Editar
(define (suma a b)
  (+ a b))
Llamada:

scheme
Copiar
Editar
(suma 3 4)  ; Resultado: 7
3.2 Asignar una Variable
Para asignar un valor a una variable, utilizamos define:

scheme
Copiar
Editar
(define x 10)
3.3 Imprimir un Valor
El comando print se usa para mostrar información en la salida estándar:

scheme
Copiar
Editar
(print "Hola, mundo!")
3.4 Llamada a Funciones
Las funciones se llaman con el siguiente formato:

scheme
Copiar
Editar
(function-name param1 param2 ...)
Ejemplo:

scheme
Copiar
Editar
(suma 5 10)  ; Resultado: 15
4. Expresiones y Operadores
Simpyl permite realizar operaciones matemáticas con operadores básicos:

+ para sumar
- para restar
* para multiplicar
/ para dividir
mod para obtener el módulo
expt para exponenciación
Ejemplo:

scheme
Copiar
Editar
(define x (+ 5 10))  ; Asigna a x el valor de 5 + 10, es decir, 15
5. Condicionales (If-Else)
Las decisiones condicionales en Simpyl se manejan con if:

scheme
Copiar
Editar
(if (condition)
    then-expression
    else-expression)
Ejemplo:

scheme
Copiar
Editar
(if (> 10 5)
    (print "10 es mayor que 5")
    (print "10 no es mayor que 5"))
6. Manejo de Funciones Avanzadas
6.1 Funciones con Valores por Defecto
Puedes definir funciones con valores por defecto usando define:

scheme
Copiar
Editar
(define saludar
  (lambda (nombre)
    (print (string-append "Hola, " nombre))))

(saludar "Carlos")  ; Imprime: Hola, Carlos
6.2 Funciones Recursivas
Las funciones recursivas son aquellas que se llaman a sí mismas dentro de su cuerpo. Aquí tienes un ejemplo de cómo calcular el factorial de un número:

scheme
Copiar
Editar
(define (factorial n)
  (if (<= n 1)
      1
      (* n (factorial (- n 1)))))
Llamada:

scheme
Copiar
Editar
(factorial 5)  ; Resultado: 120
7. Manejo de Módulos
En Simpyl, puedes importar módulos externos para extender la funcionalidad de tu programa utilizando el comando (import "module_name"):

scheme
Copiar
Editar
(import "math")
(print (sqrt 16))  ; Imprime: 4.0
8. Depuración y Puntos de Interrupción
8.1 Inspeccionar una Variable
Puedes inspeccionar el valor de una variable en cualquier momento utilizando el comando inspect:

scheme
Copiar
Editar
(inspect x)  ; Imprime el valor de x
8.2 Puntos de Interrupción
Puedes agregar un punto de interrupción en una línea específica para detener la ejecución del programa con el comando add-breakpoint:

scheme
Copiar
Editar
(add-breakpoint 10)
8.3 Habilitar o Deshabilitar el Modo de Depuración
Simpyl permite habilitar o deshabilitar el modo de depuración para ver mensajes detallados de lo que está ocurriendo en el código:

scheme
Copiar
Editar
(enable-debug)  ; Habilita el modo de depuración
(disable-debug)  ; Deshabilita el modo de depuración
9. Manejo de Memoria
El sistema de Simpyl incluye un gestor de memoria que monitorea el uso y ejecuta recolección de basura cuando es necesario. Esto es manejado automáticamente por el sistema. Puedes configurar el umbral de memoria para activar la recolección de basura, pero generalmente no es necesario intervenir directamente.

10. Ejemplo Completo
Aquí hay un ejemplo completo que demuestra varias características de Simpyl:

scheme
Copiar
Editar
(define (suma a b)
  (+ a b))

(define (factorial n)
  (if (<= n 1)
      1
      (* n (factorial (- n 1)))))

(define x 10)
(define y 20)
(define result (suma x y))
(print (string-append "La suma de " (number->string x) " y " (number->string y) " es: " (number->string result)))

(print (string-append "El factorial de 5 es: " (number->string (factorial 5))))
Este ejemplo define dos funciones (suma y factorial), asigna valores a variables y usa print para mostrar resultados. Además, utiliza string-append y number->string para concatenar y mostrar los resultados de manera más legible.
