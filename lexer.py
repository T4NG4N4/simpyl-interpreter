import re
import sys

# Definir las expresiones regulares para cada token
token_specification = [
    ('COMMENT', r'/\*[\s\S]*?\*/'),   # Comentarios multilínea
    ('LPAREN', r'\('),                # Paréntesis izquierdo
    ('RPAREN', r'\)'),                # Paréntesis derecho
    ('DEFINE', r'\bdefine\b'),        # Palabra clave 'define'
    ('PRINT', r'\bprint\b'),          # Palabra clave 'print'
    ('IF', r'\bif\b'),                # Palabra clave 'if'
    ('ELSE', r'\belse\b'),            # Palabra clave 'else'
    ('WHILE', r'\bwhile\b'),          # Palabra clave 'while'
    ('FUNCTION', r'\bfunction\b'),    # Palabra clave 'function'
    ('CLASS', r'\bclass\b'),          # Palabra clave 'class'
    ('RETURN', r'\breturn\b'),        # Palabra clave 'return'
    ('TRUE', r'\btrue\b'),            # Literal 'true'
    ('FALSE', r'\bfalse\b'),          # Literal 'false'
    ('NULL', r'\bnull\b'),            # Literal 'null'
    ('NUMBER', r'\b\d+(\.\d+)?([eE][+-]?\d+)?\b'),  # Números con decimales o exponentes
    ('INTEGER', r'\d+'),              # Números enteros
    ('STRING', r'"([^"\\]|\\.)*"'),   # Cadenas entre comillas dobles (con escapes)
    ('IDENTIFIER', r'[A-Za-z_áéíóúÁÉÍÓÚñÑ][A-Za-z0-9_áéíóúÁÉÍÓÚñÑ]*'),  # Identificadores
    ('COMPARISON_OP', r'==|!=|<=|>=|<|>'),  # Operadores de comparación
    ('ASSIGNMENT_OP', r'='),          # Operador de asignación
    ('ARITHMETIC_OP', r'[+\-*/%]'),   # Operadores aritméticos
    ('COLON', r':'),                  # Dos puntos
    ('SKIP', r'[ \t\n\r]+'),          # Espacios, tabulaciones, saltos de línea
    ('MISMATCH', r'.'),               # Cualquier otro carácter no esperado
]

# Compilar la expresión regular para cada token
master_pattern = '|'.join(f'(?P<{pair[0]}>{pair[1]})' for pair in token_specification)
compiled_re = re.compile(master_pattern)

def handle_error(mismatch, line_num):
    print(f'Error: Carácter no esperado "{mismatch.group()}" en la línea {line_num}')
    sys.exit(1)

def lexer(code):
    line_num = 1
    line_start = 0
    for mo in compiled_re.finditer(code):
        kind = mo.lastgroup
        value = mo.group()
        column = mo.start() - line_start + 1

        if kind == 'COMMENT':  # Ignorar comentarios completamente
            line_num += value.count('\n')
            continue
        elif kind == 'SKIP':  # Ignorar espacios y saltos de línea
            if '\n' in value:
                line_num += value.count('\n')
                line_start = mo.end()
            continue
        elif kind == 'MISMATCH':  # Detectar caracteres no esperados
            handle_error(mo, line_num)
        else:
            yield kind, value, line_num

def debug_tokens(token):
    print(f'Token: {token[0]}, Value: {token[1]}, Line: {token[2]}')

def test_lexer():
    code = '''
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
    
    for token in lexer(code):
        debug_tokens(token)

test_lexer()
