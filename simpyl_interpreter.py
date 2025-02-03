import re  # Librería para manejar expresiones regulares
import gc  # Gestión de memoria y recolección de basura
import psutil  # Para obtener información sobre el uso de memoria y CPU
import traceback  # Para capturar y mostrar trazas de errores
import importlib  # Para importar módulos dinámicamente

class MemoryManager:
    """Maneja la memoria y ejecuta la recolección de basura cuando el uso de memoria excede un umbral."""
    def __init__(self, threshold=100, check_interval=10):
        self.memory_threshold = threshold  # Umbral de memoria en MB
        self.check_interval = check_interval  # Frecuencia de chequeo en comandos ejecutados

    def monitor_memory(self, command_count):
        if command_count % self.check_interval == 0:
            process = psutil.Process()
            memory_usage = process.memory_info().rss / (1024 * 1024)
            if memory_usage > self.memory_threshold:
                print(f"Uso de memoria alto: {memory_usage:.2f} MB. Ejecutando recolección de basura.")
                gc.collect()

class Debugger:
    """Proporciona herramientas de depuración, como puntos de interrupción e inspección de variables."""
    def __init__(self):
        self.debug_mode = False  # Estado del modo de depuración
        self.breakpoints = {}  # Diccionario de puntos de interrupción

    def enable_debug(self):
        self.debug_mode = True
        print("Modo de depuración habilitado.")

    def disable_debug(self):
        self.debug_mode = False
        print("Modo de depuración deshabilitado.")

    def add_breakpoint(self, line):
        self.breakpoints[line] = True
        print(f"Punto de interrupción añadido en la línea {line}.")

    def remove_breakpoint(self, line):
        if line in self.breakpoints:
            del self.breakpoints[line]
            print(f"Punto de interrupción eliminado de la línea {line}.")

    def inspect_variable(self, variables, var_name):
        if var_name in variables:
            print(f"{var_name} = {variables[var_name]}")
        else:
            print(f"Variable '{var_name}' no encontrada.")

class FunctionManager:
    """Maneja la definición y almacenamiento de funciones dentro del intérprete."""
    def __init__(self):
        self.functions = {}  # Diccionario de funciones definidas por el usuario

    def define_function(self, command):
        try:
            match = re.match(r'\(define \((\w+) \((.*?)\)\): \((.*?)\)\)', command)
            if not match:
                return "Error de sintaxis en la definición de la función."
            
            func_name, params, body = match.groups()
            param_list = [p.strip() for p in params.split(',')] if params else []
            self.functions[func_name] = {'params': param_list, 'body': body.strip()}
            return f"Función '{func_name}' definida."
        except Exception:
            return f"Error al definir la función: {traceback.format_exc()}"

class ModuleManager:
    """Maneja la importación dinámica de módulos externos."""
    def __init__(self):
        self.loaded_modules = {}

    def load_module(self, module_name):
        try:
            module = importlib.import_module(module_name)
            self.loaded_modules[module_name] = module
            print(f"Módulo '{module_name}' cargado con éxito.")
        except ModuleNotFoundError:
            print(f"Error: El módulo '{module_name}' no se encuentra.")

class SimpylInterpreter:
    """Interpreta y ejecuta comandos del lenguaje Simpyl."""
    def __init__(self):
        self.variables = {}  # Diccionario de variables
        self.memory_manager = MemoryManager()
        self.debugger = Debugger()
        self.function_manager = FunctionManager()
        self.module_manager = ModuleManager()
        self.command_count = 0  # Contador de comandos ejecutados

    def execute_command(self, command):
        """Ejecuta un comando ingresado por el usuario."""
        command = command.strip()
        try:
            if command.startswith("(import"):
                module_name = command.split('(")')[1].rstrip('"))')
                return self.module_manager.load_module(module_name)
            elif re.match(r'\(define ', command):
                return self.function_manager.define_function(command)
            elif re.match(r'\(\w+ = ', command):
                return self.handle_variable_assignment(command)
            elif command.startswith("(print"):
                return self.handle_print(command)
            elif re.match(r'\(\w+\s', command):
                return self.handle_function_call(command)
            elif re.match(r'\(if ', command):
                return self.handle_conditional(command)
            else:
                return "Comando no reconocido."
        except Exception:
            return f"Error al ejecutar el comando: {traceback.format_exc()}"

    def handle_variable_assignment(self, command):
        """Maneja la asignación de variables."""
        try:
            var_name, expression = re.match(r'\((\w+) = (.*?)\)', command).groups()
            value = self.evaluate_expression(expression)
            self.variables[var_name] = value
            return f"{var_name} asignado con valor {value}"
        except Exception:
            return f"Error al asignar variable: {traceback.format_exc()}"

    def handle_print(self, command):
        """Maneja el comando print para mostrar valores en pantalla."""
        try:
            expression = command[7:-1].strip()
            value = self.evaluate_expression(expression)
            print(value)
        except Exception:
            print(f"Error en print: {traceback.format_exc()}")

    def evaluate_expression(self, expression):
        """Evalúa una expresión matemática o lógica."""
        allowed_operators = {'+', '-', '*', '/', '%', '**'}
        for op in allowed_operators:
            if op in expression:
                return self.safe_eval(expression)
        return eval(expression, {"__builtins__": None}, self.variables)

    def handle_conditional(self, command):
        """Maneja la evaluación de estructuras condicionales (if-else)."""
        try:
            match = re.match(r'\(if \((.*?)\)\s*\((.*?)\)\s*\((.*?)\)\)', command)
            if not match:
                return "Error de sintaxis en la estructura condicional."
            condition, then_expression, else_expression = match.groups()
            result = self.evaluate_expression(condition)
            return self.evaluate_expression(then_expression) if result else self.evaluate_expression(else_expression)
        except Exception:
            return f"Error en la evaluación condicional: {traceback.format_exc()}"

    def run(self):
        """Ejecuta el intérprete en un bucle de lectura de comandos."""
        print("Bienvenido a Simpyl. Escriba 'exit' para salir.")
        while True:
            try:
                command = input("Simpyl> ")
                if command.lower() == "exit":
                    print("Saliendo de Simpyl...")
                    break
                result = self.execute_command(command)
                if result:
                    print(result)
                self.command_count += 1
                self.memory_manager.monitor_memory(self.command_count)
            except Exception:
                print(f"Error: {traceback.format_exc()}.")

if __name__ == "__main__":
    interpreter = SimpylInterpreter()
    interpreter.run()
