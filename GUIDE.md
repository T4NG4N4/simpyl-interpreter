# Guía de Simpyl (Actualizada)

## 1. Introducción a Simpyl

Simpyl es un lenguaje de programación diseñado para ser sencillo, flexible y fácil de entender. Está inspirado en lenguajes funcionales como Scheme, pero con la flexibilidad y las estructuras de Python. La sintaxis de Simpyl está basada completamente en paréntesis, lo que permite una estructura clara y coherente.

Simpyl se ejecuta en un intérprete y tiene un enfoque basado en expresiones. Aquí veremos cómo escribir y ejecutar código en Simpyl.

---

## 2. Sintaxis Básica

Simpyl utiliza una sintaxis basada en paréntesis para definir y ejecutar expresiones. Algunos de los elementos más comunes son:

- **Definición de funciones:** `(define (nombre (param1 param2 ...)) ...)`
- **Asignación de variables:** `(define (var (nombre valor)))`
- **Impresión de valores:** `(print (valor))`
- **Llamadas a funciones:** `(nombre-de-funcion (param1 param2 ...))`
- **Condicionales:** `(if (condición) (entonces) (si-no))`
- **Bucles:** `(while (condición) (cuerpo))`
- **Listas:** `(list (elem1 elem2 elem3))`

---

## 3. Comandos Básicos

### 3.1 Definir una Función

La sintaxis para definir una función es:

```scheme
(define (nombre (param1 param2 ...))
    (cuerpo-de-la-funcion))
```

Ejemplo:

```scheme
(define (suma (a b))
    return (+ a b))
```

Llamada:

```scheme
(suma (3 4)) ; Resultado: 7
```

---

### 3.2 Asignar una Variable

Para asignar un valor a una variable, utilizamos `define`:

```scheme
(define (var (x 10)))
```

Ejemplo:

```scheme
(define (var (pi 3.1416)))
```

---

### 3.3 Imprimir un Valor

El comando `print` se usa para mostrar información en la salida estándar:

```scheme
(print ("Hola, mundo!"))
```

---

### 3.4 Llamada a Funciones

Las funciones se llaman con el siguiente formato:

```scheme
(nombre-de-funcion (param1 param2 ...))
```

Ejemplo:

```scheme
(suma (5 10)) ; Resultado: 15
```

---

## 4. Expresiones y Operadores

Simpyl permite realizar operaciones matemáticas con operadores básicos:

- `+` para sumar
- `-` para restar
- `*` para multiplicar
- `/` para dividir
- `mod` para obtener el módulo
- `expt` para exponenciación

Ejemplo:

```scheme
(define (var (x (+ 5 10)))) ; Asigna a x el valor de 5 + 10, es decir, 15
```

---

## 5. Condicionales (If-Elif-Else)

Las decisiones condicionales en Simpyl se manejan con `if`, `elif` y `else`:

```scheme
(if (> 10 5)
    (print ("10 es mayor que 5"))
    (elif (= 10 5)
        (print ("10 es igual a 5"))
        (else
            (print ("10 no es mayor que 5"))))
```

---

## 6. Bucles (While)

Puedes definir bucles `while` utilizando la siguiente sintaxis:

```scheme
(while (< x 5)
    (print (x))
    (define (var (x (+ x 1))))
```

Ejemplo:

```scheme
(define (var (x 0)))
(while (< x 3)
    (print (x))
    (define (var (x (+ x 1)))))
```

---

## 7. Listas y Tuplas

Puedes definir listas usando `list`:

```scheme
(define (var (mi-lista (list (1 2 3 4)))))
(print (mi-lista)) ; Resultado: (1 2 3 4)
```

Para definir tuplas:

```scheme
(define (var (mi-tupla (tuple (1 2 3)))))
(print (mi-tupla)) ; Resultado: (1 2 3)
```

Para acceder a elementos:

```scheme
(print (list-get (mi-lista 0))) ; Resultado: 1
(print (tuple-get (mi-tupla 1))) ; Resultado: 2
```

---

## 8. Entrada de Datos

Para leer entrada de datos desde el teclado:

```scheme
(define (var (nombre (input ("¿Cuál es tu nombre?")))))
(print (string-append ("Hola, " nombre)))
```

---

## 9. Operadores Lógicos

Simpy admite operadores lógicos:

- `and`, `or`, `not`, `xor`

Ejemplo:

```scheme
(if (and (> 5 3) (< 5 10))
    (print ("5 está entre 3 y 10")))

(if (or (> 5 10) (< 5 10))
    (print ("Al menos una condición es verdadera")))

(if (not (> 5 10))
    (print ("5 no es mayor que 10")))
```

---

## 10. Ejemplo Completo

```scheme
(define (suma (a b))
    return (+ a b))

(define (factorial (n))
    (if (<= n 1)
        1
        (* n (factorial (- n 1)))))

(define (var (x 10)))
(define (var (y 20)))
(define (var (result (suma (x y)))))

(print (string-append ("La suma de " (number->string (x)) " y " (number->string (y)) " es: " (number->string (result)))))
(print (string-append ("El factorial de 5 es: " (number->string (factorial (5))))))
```

---

