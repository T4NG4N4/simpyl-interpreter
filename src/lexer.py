import re  # Importa el módulo 're' para trabajar con expresiones regulares
import sys  # Importa el módulo 'sys' para interactuar con el sistema (por ejemplo, para salir del programa)

# Especificación de los tokens utilizando expresiones regulares
token_specification = [ 
    ('COMMENT', r'/\*[\s\S]*?\*/'),   # Define el token 'COMMENT' para comentarios multilínea
    ('LPAREN', r'\('),                # Define el token 'LPAREN' para el paréntesis izquierdo
    ('RPAREN', r'\)'),                # Define el token 'RPAREN' para el paréntesis derecho
    ('DEFINE', r'\bdefine\b'),        # Define el token 'DEFINE' para la palabra clave 'define'
    ('PRINT', r'\bprint\b'),          # Define el token 'PRINT' para la palabra clave 'print'
    ('IF', r'\bif\b'),                # Define el token 'IF' para la palabra clave 'if'
    ('ELSE', r'\belse\b'),            # Define el token 'ELSE' para la palabra clave 'else'
    ('WHILE', r'\bwhile\b'),          # Define el token 'WHILE' para la palabra clave 'while'
    ('FUNCTION', r'\bfunction\b'),    # Define el token 'FUNCTION' para la palabra clave 'function'
    ('CLASS', r'\bclass\b'),          # Define el token 'CLASS' para la palabra clave 'class'
    ('RETURN', r'\breturn\b'),        # Define el token 'RETURN' para la palabra clave 'return'
    ('TRUE', r'\btrue\b'),            # Define el token 'TRUE' para el literal 'true'
    ('FALSE', r'\bfalse\b'),          # Define el token 'FALSE' para el literal 'false'
    ('NULL', r'\bnull\b'),            # Define el token 'NULL' para el literal 'null'
    ('NUMBER', r'\b\d+(\.\d+)?([eE][+-]?\d+)?\b'),  # Define el token 'NUMBER' para números con decimales o exponentes
    ('INTEGER', r'\d+'),              # Define el token 'INTEGER' para números enteros
    ('STRING', r'"([^"\\]|\\.)*"'),   # Define el token 'STRING' para cadenas entre comillas dobles
    ('IDENTIFIER', r'[A-Za-z_áéíóúÁÉÍÓÚñÑ][A-Za-z0-9_áéíóúÁÉÍÓÚñÑ]*'),  # Define el token 'IDENTIFIER' para identificadores
    ('COMPARISON_OP', r'==|!=|<=|>=|<|>'),  # Define el token 'COMPARISON_OP' para operadores de comparación
    ('ASSIGNMENT_OP', r'='),          # Define el token 'ASSIGNMENT_OP' para el operador de asignación '='
    ('ARITHMETIC_OP', r'[+\-*/%]'),   # Define el token 'ARITHMETIC_OP' para operadores aritméticos
    ('COLON', r':'),                  # Define el token 'COLON' para los dos puntos ':'
    ('SKIP', r'[ \t\n\r]+'),          # Define el token 'SKIP' para ignorar espacios, tabulaciones y saltos de línea
    ('MISMATCH', r'.'),               # Define el token 'MISMATCH' para cualquier carácter no esperado
]

# Compilación de las expresiones regulares para los tokens
master_pattern = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in token_specification)  # Crea una única expresión regular para todos los tokens
compiled_re = re.compile(master_pattern)  # Compila la expresión regular

def handle_error(mismatch, line_num):  
    """Maneja errores de tokens inesperados e imprime el mensaje de error."""
    print(f'Error: Carácter no esperado "{mismatch.group()}" en la línea {line_num}')
    sys.exit(1)  # Termina el programa si hay un error

def lexer(code):  
    """Función de análisis léxico que genera tokens a partir del código fuente."""
    line_num = 1  # Número de línea actual
    line_start = 0  # Posición de inicio de la línea actual

    # Itera a través de los resultados de la expresión regular
    for match in compiled_re.finditer(code):  # Encuentra todas las coincidencias de la expresión regular
        kind = match.lastgroup  # Tipo de token (basado en el nombre de grupo)
        value = match.group()   # Valor del token (el texto coincidente)
        column = match.start() - line_start + 1  # Columna del token en la línea

        if kind == 'COMMENT':  # Si el token es un comentario
            line_num += value.count('\n')  # Cuenta las líneas en el comentario
            continue  # Pasa al siguiente token sin hacer nada
        elif kind == 'SKIP':  # Si el token es un espacio, tabulación o salto de línea
            if '\n' in value:  # Si hay un salto de línea
                line_num += value.count('\n')  # Cuenta las líneas afectadas
                line_start = match.end()  # Ajusta el inicio de la siguiente línea
            continue  # Pasa al siguiente token
        elif kind == 'MISMATCH':  # Si el token no es reconocido
            handle_error(match, line_num)  # Llama a la función de manejo de errores
        else:
            yield kind, value, line_num  # Genera el token

def debug_tokens(token):  
    """Imprime información detallada sobre cada token."""
    print(f'Token: {token[0]}, Valor: {token[1]}, Línea: {token[2]}')  # Muestra el tipo, valor y línea del token

def test_lexer():  
    """Función para probar el lexer con un código de ejemplo."""
    code = '''  # Definición de un código fuente de prueba
    (define square (x) (* x x))
    (print (square 4))
    (if true
        (print "verdadero")
        (print "falso"))
    (while (x > 0)
        (print x)
        (x = (x - 1)))
    /* Esto es un comentario
       que se extiende a varias líneas */
    (x = (x * 2)) /* Fin de comentario */
    (function testFunc () (return 42))
    (class MyClass (x) (return x))
    '''
    
    # Ejecuta el lexer sobre el código de prueba
    for token in lexer(code):  # Itera sobre los tokens generados por el lexer
        debug_tokens(token)  # Imprime información sobre cada token

test_lexer()  # Llama a la función que prueba el lexer
