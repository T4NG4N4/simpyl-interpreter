import re  # Librería para manejar expresiones regulares
import gc  # Gestión de memoria y recolección de basura
import psutil  # Para obtener información sobre el uso de memoria y CPU
import traceback  # Para capturar y mostrar trazas de errores
import importlib  # Para importar módulos dinámicamente
import ast  # Para evaluar expresiones de forma segura
import json  # Para trabajar con estructuras de datos JSON (listas y diccionarios)
import logging  # Para registrar errores sin mostrarlos en pantalla
import pdb  # Depurador interactivo de Python
import pytest  # Librería para pruebas unitarias
import sys  # Para acceder a argumentos del sistema

# Configuración del sistema de logs
logging.basicConfig(level=logging.ERROR, filename="simpyl.log", filemode="w")


class MemoryManager:
    """Maneja la memoria y ejecuta la recolección de basura cuando el uso de memoria excede un umbral."""
    
    def __init__(self, threshold=100, check_interval=10):
        self.memory_threshold = threshold  # Umbral de memoria en MB
        self.check_interval = check_interval  # Frecuencia de chequeo en comandos ejecutados

    def monitor_memory(self, command_count):
        """Monitorea el uso de memoria y ejecuta la recolección de basura si es necesario."""
        if command_count % self.check_interval == 0:
            process = psutil.Process()
            memory_usage = process.memory_info().rss / (1024 * 1024)

            # Ajusta el umbral de recolección de basura dinámicamente
            if memory_usage > self.memory_threshold:
                print(f"Uso de memoria alto: {memory_usage:.2f} MB. Ejecutando recolección de basura.")
                gc.collect()
                gc.set_threshold(int(memory_usage * 0.8))  # Ajusta umbral dinámicamente


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
        """Inspecciona una variable y muestra su valor si existe."""
        if var_name in variables:
            print(f"{var_name} = {variables[var_name]}")
        else:
            print(f"Variable '{var_name}' no encontrada.")


class FunctionManager:
    """Maneja la definición y almacenamiento de funciones dentro del intérprete."""
    
    def __init__(self):
        self.functions = {}  # Diccionario de funciones definidas por el usuario

    def define_function(self, command):
        """Define una función en Simpyl y la almacena en el entorno global."""
        try:
            match = re.match(r'\(define \((\w+) \((.*?)\)\): \((.*?)\)\)', command)
            if not match:
                return "Error de sintaxis en la definición de la función. Asegúrese de que la sintaxis sea correcta."

            func_name, params, body = match.groups()
            param_list = [p.strip() for p in params.split(',')] if params else []
            function_code = f"def {func_name}({', '.join(param_list)}): return {body}"

            exec(function_code, globals())  # Ejecuta y almacena la función en el entorno global
            return f"Función '{func_name}' definida correctamente."
        except Exception as e:
            logging.error(f"Error al definir la función: {command}\n{e}", exc_info=True)
            return f"Error al definir la función: {traceback.format_exc()}"


class ModuleManager:
    """Maneja la importación dinámica de módulos externos."""
    
    def __init__(self):
        self.loaded_modules = {}

    def load_module(self, module_name):
        """Importa dinámicamente un módulo si está disponible."""
        try:
            module = importlib.import_module(module_name)
            self.loaded_modules[module_name] = module
            print(f"Módulo '{module_name}' cargado con éxito.")
        except ModuleNotFoundError:
            logging.error(f"Error: El módulo '{module_name}' no se encuentra.")
            return f"Error: El módulo '{module_name}' no se encuentra."
        except Exception as e:
            logging.error(f"Error al cargar el módulo '{module_name}': {e}", exc_info=True)
            return f"Error al cargar el módulo '{module_name}': {traceback.format_exc()}"


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
                module_name = command.split('("')[1].rstrip('")')
                return self.module_manager.load_module(module_name)
            elif re.match(r'\(define ', command):
                return self.function_manager.define_function(command)
            elif re.match(r'\(\w+ = ', command):
                return self.handle_variable_assignment(command)
            elif command.startswith("(print"):
                return self.handle_print(command)
            elif re.match(r'\(if ', command):
                return self.handle_conditional(command)
            else:
                return "Comando no reconocido. Por favor, revise la sintaxis."
        except Exception as e:
            logging.error(f"Error al ejecutar comando: {command}\n{e}", exc_info=True)
            return f"Error al ejecutar el comando: {traceback.format_exc()}"

    def handle_variable_assignment(self, command):
        """Maneja la asignación de variables."""
        try:
            var_name, expression = re.match(r'\((\w+) = (.*?)\)', command).groups()
            value = self.evaluate_expression(expression)
            self.variables[var_name] = value
            return f"{var_name} asignado con valor {value}"
        except Exception as e:
            logging.error(f"Error en asignación de variable: {command}\n{e}", exc_info=True)
            return f"Error al asignar variable: {traceback.format_exc()}"

    def evaluate_expression(self, expression):
        """Evalúa una expresión matemática o lógica de forma segura."""
        try:
            if expression.startswith("[") or expression.startswith("{"):
                return json.loads(expression)  # Soporte para listas y diccionarios
            return eval(expression, {"__builtins__": None}, self.variables)
        except Exception as e:
            logging.error(f"Error al evaluar expresión: {expression}\n{e}", exc_info=True)
            return f"Expresión inválida: {traceback.format_exc()}"

    def handle_print(self, command):
        """Maneja el comando print."""
        try:
            expression = re.match(r'\(print \((.*?)\)\)', command).groups()[0]
            value = self.evaluate_expression(expression)
            print(value)
        except Exception as e:
            logging.error(f"Error en comando print: {command}\n{e}", exc_info=True)
            return f"Error en comando print: {traceback.format_exc()}"

    def handle_conditional(self, command):
        """Maneja la estructura condicional if-else."""
        try:
            match = re.match(r'\(if \((.*?)\)\s*\((.*?)\)\s*\((.*?)\)\)', command)
            if not match:
                return "Error de sintaxis en la declaración if-else."

            condition, then_expr, else_expr = match.groups()
            if self.evaluate_expression(condition):
                return self.evaluate_expression(then_expr)
            else:
                return self.evaluate_expression(else_expr)
        except Exception as e:
            logging.error(f"Error en la declaración if-else: {command}\n{e}", exc_info=True)
            return f"Error en la declaración if-else: {traceback.format_exc()}"

    def run_interactive(self):
        """Ejecuta el intérprete en modo interactivo."""
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
            except KeyboardInterrupt:
                print("\nSaliendo de Simpyl...")
                break
            except Exception:
                logging.error("Error fatal en el intérprete.", exc_info=True)
                print("Error interno en Simpyl.")

    def run_file(self, filename):
        """Ejecuta un archivo de Simpyl."""
        try:
            with open(filename, "r", encoding="utf-8") as file:
                for line in file:
                    result = self.execute_command(line.strip())
                    if result:
                        print(result)
                    self.command_count += 1
                    self.memory_manager.monitor_memory(self.command_count)
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo '{filename}'.")
        except Exception as e:
            logging.error(f"Error al ejecutar archivo: {filename}\n{e}", exc_info=True)
            print(f"Error interno al ejecutar archivo: {traceback.format_exc()}")

if __name__ == "__main__":
    interpreter = SimpylInterpreter()

    if len(sys.argv) > 1:
        filename = sys.argv[1]
        interpreter.run_file(filename)
    else:
        interpreter.run_interactive()
