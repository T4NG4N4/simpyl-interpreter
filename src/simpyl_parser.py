import re  # Importa la librería re para expresiones regulares (aunque no se utiliza explícitamente aquí).

class SimpylParser:
    def __init__(self, lexer):
        # Inicializa el parser con un lexer (analizador léxico) y establece el estado inicial.
        self.lexer = lexer
        self.tokens = []  # Lista para almacenar los tokens generados por el lexer.
        self.current_token = None  # El token actual en el análisis.
        self.token_index = -1  # Índice que rastrea el token actual en la lista de tokens.

    def parse(self, code):
        """Función principal para analizar el código y construir el AST (Abstract Syntax Tree)"""
        self.tokens = list(self.lexer(code))  # Convierte el código en una lista de tokens.
        self.token_index = -1  # Reinicia el índice de tokens.
        self.next_token()  # Avanza al primer token.
        return self.program()  # Inicia el análisis del programa.

    def next_token(self):
        """Avanza al siguiente token en la lista."""
        self.token_index += 1  # Incrementa el índice.
        if self.token_index < len(self.tokens):  # Si hay más tokens por procesar.
            self.current_token = self.tokens[self.token_index]  # Establece el siguiente token.
        else:
            self.current_token = None  # Si no hay más tokens, establece como None.

    def expect(self, kind):
        """Verifica si el siguiente token es del tipo esperado. Si no lo es, lanza un error de sintaxis."""
        if self.current_token and self.current_token[0] == kind:  # Si el tipo del token actual coincide con el esperado.
            value = self.current_token[1]  # Obtiene el valor del token.
            self.next_token()  # Avanza al siguiente token.
            return value  # Devuelve el valor del token.
        else:
            raise SyntaxError(f"Se esperaba un token de tipo '{kind}', pero se encontró '{self.current_token}'")

    def program(self):
        """Analiza un programa, que puede ser una lista de expresiones."""
        statements = []  # Lista para almacenar las declaraciones analizadas.
        while self.current_token:  # Mientras haya un token por procesar.
            statements.append(self.statement())  # Procesa una declaración y la agrega a la lista.
        return statements  # Devuelve todas las declaraciones analizadas.

    def statement(self):
        """Parsea una declaración general, que puede ser una asignación, definición de función o condicional."""
        if self.current_token[0] == "DEFINE":  # Si el token actual es una definición de función.
            return self.parse_function_definition()  # Analiza la definición de función.
        elif self.current_token[0] == "IF":  # Si el token actual es una sentencia if.
            return self.parse_if_statement()  # Analiza la sentencia if.
        elif self.current_token[0] == "IDENTIFIER":  # Si el token actual es un identificador (asignación).
            return self.parse_assignment()  # Analiza la asignación.
        else:
            raise SyntaxError(f"Declaración inesperada: {self.current_token}")  # Si el token no es válido.

    def parse_function_definition(self):
        """Parsea una definición de función: (define func_name (params) (body))"""
        self.expect("DEFINE")  # Espera y consume el token 'DEFINE'.
        self.expect("LPAREN")  # Espera y consume el paréntesis izquierdo de la función.
        func_name = self.expect("IDENTIFIER")  # Obtiene el nombre de la función.
        self.expect("LPAREN")  # Espera el paréntesis izquierdo de los parámetros.
        params = self.parse_parameters()  # Analiza los parámetros de la función.
        self.expect("RPAREN")  # Espera y consume el paréntesis derecho de los parámetros.
        self.expect("LPAREN")  # Espera el paréntesis izquierdo del cuerpo de la función.
        body = self.parse_expression()  # Analiza el cuerpo de la función.
        self.expect("RPAREN")  # Espera y consume el paréntesis derecho del cuerpo.
        return {"type": "function_definition", "name": func_name, "params": params, "body": body}  # Devuelve la representación de la función.

    def parse_parameters(self):
        """Parsea los parámetros de la función."""
        params = []  # Lista para almacenar los parámetros.
        while self.current_token and self.current_token[0] == "IDENTIFIER":  # Mientras haya un identificador.
            params.append(self.expect("IDENTIFIER"))  # Agrega el identificador como parámetro.
        return params  # Devuelve los parámetros de la función.

    def parse_assignment(self):
        """Parsea una asignación de variable: (variable = value)"""
        var_name = self.expect("IDENTIFIER")  # Obtiene el nombre de la variable.
        self.expect("ASSIGNMENT_OP")  # Espera y consume el operador de asignación ('=').
        expression = self.parse_expression()  # Analiza la expresión que se va a asignar.
        return {"type": "assignment", "name": var_name, "value": expression}  # Devuelve la representación de la asignación.

    def parse_expression(self):
        """Parsea una expresión, que puede ser un valor, operación o llamada a función."""
        if self.current_token[0] == "NUMBER":  # Si el token actual es un número.
            return {"type": "number", "value": self.expect("NUMBER")}  # Devuelve el número como una expresión.
        elif self.current_token[0] == "STRING":  # Si el token actual es una cadena.
            return {"type": "string", "value": self.expect("STRING")}  # Devuelve la cadena como una expresión.
        elif self.current_token[0] == "IDENTIFIER":  # Si el token actual es un identificador.
            return {"type": "identifier", "value": self.expect("IDENTIFIER")}  # Devuelve el identificador como una expresión.
        elif self.current_token[0] == "LPAREN":  # Si el token actual es un paréntesis izquierdo (comienza una expresión compleja).
            self.expect("LPAREN")  # Consume el paréntesis izquierdo.
            expr = self.statement()  # Analiza la expresión dentro de los paréntesis.
            self.expect("RPAREN")  # Consume el paréntesis derecho.
            return expr  # Devuelve la expresión analizada.
        elif self.current_token[0] == "OPERATOR":  # Si el token es un operador (por ejemplo, '+', '-', '*').
            operator = self.expect("OPERATOR")  # Obtiene el operador.
            left = self.parse_expression()  # Analiza la expresión de la izquierda.
            right = self.parse_expression()  # Analiza la expresión de la derecha.
            return {"type": "operation", "operator": operator, "left": left, "right": right}  # Devuelve la operación.
        else:
            raise SyntaxError(f"Expresión inesperada: {self.current_token}")  # Si el token no es una expresión válida.

    def parse_if_statement(self):
        """Parsea una sentencia condicional if: (if (condition) (then) (else))"""
        self.expect("IF")  # Espera y consume el token 'IF'.
        self.expect("LPAREN")  # Consume el paréntesis izquierdo de la condición.
        condition = self.parse_expression()  # Analiza la condición.
        self.expect("RPAREN")  # Consume el paréntesis derecho de la condición.
        then_expr = self.parse_expression()  # Analiza la expresión a ejecutar si la condición es verdadera.
        self.expect("RPAREN")  # Consume el paréntesis derecho del bloque 'then'.
        else_expr = self.parse_expression()  # Analiza la expresión a ejecutar si la condición es falsa.
        return {"type": "if", "condition": condition, "then": then_expr, "else": else_expr}  # Devuelve la sentencia 'if'.

# Ejemplo de uso con el lexer y parser

def test_parser():
    code = '''
    (define square (x) (* x x))
    (define add (a b) (+ a b))
    (if (> x 10) (print "Mayor que 10") (print "Menor o igual a 10"))
    (x = (add 5 3))
    '''
    parser = SimpylParser(lexer)  # Asumimos que 'lexer' es el lexer previamente definido.
    ast = parser.parse(code)  # Analiza el código y genera el AST.
    print(ast)  # Imprime el AST resultante.

test_parser()  # Ejecuta la función de prueba.
