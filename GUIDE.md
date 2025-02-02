Para iniciar el intérprete, ejecuta:

sh
python simpyl_interpreter.py
Escribe comandos en el prompt interactivo. Por ejemplo:

sh
Simpyl> (define (saludo) (print "¡Hola mundo!"))
Simpyl> (saludo)
Guía de Uso
Para una guía completa de la sintaxis y el uso de Simpyl, consulta el archivo GUIDE.md.

Contribución
¡Las contribuciones son bienvenidas! Si deseas colaborar, sigue estos pasos:

Haz un fork del repositorio.
Crea una nueva rama (git checkout -b feature/nueva-funcionalidad).
Realiza tus cambios y haz commit (git commit -am 'Añadir nueva funcionalidad').
Envía tus cambios a tu fork (git push origin feature/nueva-funcionalidad).
Abre un Pull Request.
Licencia
Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.

¡Esperamos verte entre los primeros miembros de la comunidad y contribuir al crecimiento de Simpyl!
Code
### `GUIDE.md`

```markdown
# Guía de Sintaxis de Simpyl

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

```scheme
(define (function_name param1 param2 ...) (body_of_function))
Ejemplo:

Scheme
(define (suma a b)
    (+ a b))
En este caso, la función suma recibe dos parámetros a y b, y devuelve su suma.

Ejemplo de llamada:

Scheme
(suma 3 4)  ; Resultado: 7
3.2 Asignar una Variable
Para asignar un valor a una variable, utilizamos la siguiente sintaxis:

Scheme
(var_name = expression)
Ejemplo:

Scheme
(x = 10)
Esto asigna el valor 10 a la variable x.

3.3 Imprimir un Valor
El comando print se usa para mostrar información en la salida estándar:

Scheme
(print expression)
Ejemplo:

Scheme
(print "Hola, mundo!")  ; Imprime: Hola, mundo!
3.4 Llamada a Función
Las funciones se llaman con el siguiente formato:

Scheme
(function_name param1 param2 ...)
Ejemplo:

Scheme
(suma 5 10)  ; Resultado: 15
4. Expresiones y Operadores
Simpyl permite realizar operaciones matemáticas con operadores básicos como:

+ para sumar
- para restar
* para multiplicar
/ para dividir
% para obtener el módulo
** para exponenciación
Ejemplo:

Scheme
(x = (+ 5 10))  ; Asigna a x el valor de 5 + 10, es decir, 15
5. Condicionales (If-Else)
Simpyl también permite realizar decisiones condicionales usando if, else y elif (no obligatorio, pero útil en casos complejos):

Scheme
(if condition
    (then_expression)
    (else_expression))
Ejemplo:

Scheme
(if (> 10 5)
    (print "10 es mayor que 5")
    (print "10 no es mayor que 5"))
6. Manejo de Funciones Avanzadas
6.1 Funciones con Parámetros Opcionales
Puedes definir funciones con parámetros opcionales y asignarles valores por defecto.

Ejemplo:

Scheme
(define (saludar nombre "Desconocido")
    (print (string-append "Hola, " nombre)))
    
(saludar "Carlos")    ; Imprime: Hola, Carlos
(saludar)             ; Imprime: Hola, Desconocido
6.2 Funciones Recursivas
Las funciones recursivas son aquellas que se llaman a sí mismas dentro de su cuerpo. Aquí tienes un ejemplo de cómo hacer una función recursiva para calcular el factorial de un número:

Scheme
(define (factorial n)
    (if (<= n 1)
        1
        (* n (factorial (- n 1)))))
Llamada:

Scheme
(factorial 5)  ; Resultado: 120
7. Manejo de Módulos
En Simpyl, puedes importar módulos externos para extender la funcionalidad de tu programa.

Scheme
(import "module_name")
Ejemplo:

Scheme
(import "math")
(print (math.sqrt 16))  ; Imprime: 4.0
8. Depuración y Puntos de Interrupción
Simpyl incluye una funcionalidad de depuración para inspeccionar variables y establecer puntos de interrupción.

8.1 Inspeccionar una Variable
Scheme
(inspect variable_name)
Ejemplo:

Scheme
(inspect x)  ; Imprime el valor de x
8.2 Puntos de Interrupción
Puedes agregar un punto de interrupción en una línea específica para detener la ejecución del programa:

Scheme
(add-breakpoint line_number)
Ejemplo:

Scheme
(add-breakpoint 10)
