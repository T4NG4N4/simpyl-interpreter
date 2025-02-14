# Simpyl Interpreter: Un Proyecto Innovador para Desarrolladores

Simpyl es un lenguaje de programación minimalista y versátil, inspirado en la sintaxis limpia y funcional de Scheme, pero con la flexibilidad de Python. Su diseño busca combinar lo mejor de ambos mundos: facilidad de uso para principiantes y poderosas herramientas para programadores avanzados. Este proyecto tiene como objetivo crear un lenguaje independiente de Python, con su propio intérprete, para que los desarrolladores puedan disfrutar de una experiencia de codificación ágil y eficiente.

## Misión del Proyecto

La misión de Simpyl es convertirse en un lenguaje popular y totalmente independiente de Python, ofreciendo una alternativa única con su propio intérprete. Buscamos crear una comunidad activa que impulse su crecimiento, haciendo de Simpyl una herramienta poderosa y accesible para todos.

## Características Principales

- **Sintaxis clara y fácil de aprender:** Ideal tanto para quienes inician como para quienes buscan optimizar su flujo de trabajo.
- **Gestión automática de memoria:** Permite concentrarse en la lógica del programa sin preocuparse por la administración de recursos.
- **Herramientas de depuración integradas:** Incluye puntos de interrupción y herramientas para inspeccionar variables, mejorando la experiencia de desarrollo.
- **Definición y llamada a funciones:** Permite una estructura de código más modular y organizada.
- **Importación de módulos:** Extiende la funcionalidad de Simpyl con una amplia variedad de módulos.

Este es el momento perfecto para unirte a la comunidad de Simpyl. Al hacerlo, podrás influir en la evolución del lenguaje y ayudar a construir una base sólida para el proyecto. ¡Juntos podemos hacerlo crecer y llevarlo lejos!

---

## Estructura del Proyecto

El repositorio de Simpyl está requiere tu alluda para lograr tener un estructurado de la siguiente manera y un dia ser un lenguaje completo:

```
Simpyl/
├── src/
│   ├── lexer.py  # Analizador léxico
│   ├── parser.py  # Analizador sintáctico
│   ├── interpreter.py  # Intérprete de Simpyl
│   └── utils.py  # Utilidades y funciones auxiliares
├── examples/
│   ├── hello_world.spyl  # Ejemplo básico en Simpyl
│   ├── factorial.spyl  # Cálculo de factorial con recursión
│   └── conditionals.spyl  # Uso de estructuras condicionales
├── tests/
│   ├── test_lexer.py  # Pruebas del analizador léxico
│   ├── test_parser.py  # Pruebas del analizador sintáctico
│   ├── test_interpreter.py  # Pruebas del intérprete
│   └── test_examples.py  # Pruebas de ejemplos
├── README.md  # Documentación principal del proyecto
├── GUIDE.md  # Guía detallada sobre la sintaxis de Simpyl
└── LICENSE  # Licencia del proyecto
```

## Repositorio en GitHub

Puedes encontrar el código fuente y contribuir al desarrollo de Simpyl en el siguiente repositorio:

[Repositorio en GitHub](https://github.com/T4NG4N4/simpyl-interpreter)

## Analizador Léxico (Lexer)

El lexer de Simpyl transforma el código fuente en una secuencia de tokens que pueden ser interpretados por el analizador sintáctico. Su implementación en Python está basada en expresiones regulares para reconocer diferentes componentes del lenguaje.

### Implementación del Lexer

```python
import re
import sys

token_specification = [
    ('COMMENT', r'/\*[\s\S]*?\*/'),   # Comentarios multilínea
    ('LPAREN', r'\('),                # Paréntesis izquierdo
    ('RPAREN', r'\)'),                # Paréntesis derecho
    ('DEFINE', r'\bdefine\b'),        # Palabra clave 'define'
    ('PRINT', r'\bprint\b'),          # Palabra clave 'print'
    ('IF', r'\bif\b'),                # Palabra clave 'if'
    ('ELSE', r'\belse\b'),            # Palabra clave 'else'
    ('NUMBER', r'\b\d+(\.\d+)?([eE][+-]?\d+)?\b'),  # Números con decimales o exponentes
    ('STRING', r'"([^"\\]|\\.)*"'),   # Cadenas entre comillas dobles
    ('IDENTIFIER', r'[A-Za-z_][A-Za-z0-9_]*'),  # Identificadores
    ('COMPARISON_OP', r'==|!=|<=|>=|<|>'),  # Operadores de comparación
    ('ARITHMETIC_OP', r'[+\-*/%]'),   # Operadores aritméticos
    ('SKIP', r'[ \t\n\r]+'),          # Espacios, tabulaciones, saltos de línea
    ('MISMATCH', r'.'),               # Cualquier otro carácter no esperado
]

master_pattern = '|'.join(f'(?P<{pair[0]}>{pair[1]})' for pair in token_specification)
compiled_re = re.compile(master_pattern)

def lexer(code):
    for mo in compiled_re.finditer(code):
        kind = mo.lastgroup
        value = mo.group()
        if kind == 'SKIP':
            continue
        elif kind == 'MISMATCH':
            print(f'Error: Carácter inesperado "{value}"')
            sys.exit(1)
        else:
            yield kind, value
```

### Uso del Lexer

Ejemplo de ejecución:
```python
code = """
(define square (x) (* x x))
(print (square 4))
"""

for token in lexer(code):
    print(token)
```

## Contribuir al Proyecto

Si deseas contribuir a Simpyl, sigue estos pasos:

1. **Clona el repositorio:**
   ```sh
   git clone https://github.com/T4NG4N4/simpyl-interpreter.git
   cd simpyl-interpreter
   ```
2. **Crea una rama para tu contribución:**
   ```sh
   git checkout -b mi-nueva-funcionalidad
   ```
3. **Realiza tus cambios y prébalos.**
4. **Envía un Pull Request.**

Apreciamos cualquier tipo de contribución, ya sea mejorando el código, corrigiendo errores, agregando documentación o sugiriendo nuevas características.

## Contacto y Comunidad

Próximamente agregaremos redes sociales y canales de comunicación para interactuar con la comunidad de Simpyl.

¡Esperamos tu participación para hacer crecer Simpyl y mejorar juntos!

