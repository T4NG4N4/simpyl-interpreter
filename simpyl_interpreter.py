import re
import gc
import psutil
import traceback
import importlib

class MemoryManager:
    """
    Clase para manejar la memoria, monitoreando y ejecutando la recolección de basura si es necesario.
    """
    def __init__(self, threshold=100, check_interval=10):
        # Umbral de memoria en MB y intervalo de chequeo en número de comandos ejecutados
        self.memory_threshold = threshold
        self.check_interval = check_interval

    def monitor_memory(self, command_count):
        """
        Monitorea el uso de memoria y ejecuta la recolección de basura si el uso de memoria supera el umbral.
        """
        if command_count % self.check_interval == 0:
            process = psutil.Process()
            memory_usage = process.memory_info().rss / (1024 * 1024)  # Convertir a MB
            if memory_usage > self.memory_threshold:
                print(f"Uso de memoria alto: {memory_usage:.2f} MB. Ejecutando recolección de basura.")
                gc.collect()

class Debugger:
    """
    Clase para manejar la depuración, incluyendo puntos de interrupción e inspección de variables.
    """
    def __init__(self):
        self.debug_mode = False
        self.breakpoints = {}

    def enable_debug(self):
        """
        Habilita el modo de depuración.
        """
        self.debug_mode = True
        print("Modo de depuración habilitado. Usa '(inspect <variable>)' para ver el valor de las variables.")

    def disable_debug(self):
        """
        Deshabilita el modo de depuración.
        """
        self.debug_mode = False
        print("Modo de depuración deshabilitado.")

    def add_breakpoint(self, line, condition=None):
        """
        Añade un punto de interrupción en una línea específica con una condición opcional.
        """
        self.breakpoints[line] = condition
        print(f"Punto de interrupción añadido en la línea {line}. Condición: {condition or 'Ninguna'}.")

    def remove_breakpoint(self, line):
        """
        Elimina un punto de interrupción de una línea específica.
        """
        if line in self.breakpoints:
            del self.breakpoints[line]
            print(f"Punto de interrupción eliminado de la línea {line}.")
        else:
            print(f"No hay punto de interrupción en la línea {line}.")

    def inspect_variable(self, variables, var_name):
        """
        Inspecciona el valor de una variable específica.
        """
        if var_name in variables:
            print(f"{var_name} = {variables[var_name]['value']}")
        else:
            print(f"Variable '{var_name}' no encontrada.")

    def show_call_stack(self):
        """
        Muestra la pila de llamadas actual.
        """
        print("Pila de llamadas:")
        print("".join(traceback.format_stack()))

class FunctionManager:
    """
    Clase para manejar la definición y ejecución de funciones.
    """
    def __init__(self):
        self.functions = {}

    def handle_function_definition(self, command):
        """
        Maneja la definición de funciones.
        """
        try:
            # Usa una expresión regular para extraer el nombre, parámetros y cuerpo de la función.
            match = re.match(r'\(define\s+\((\w+)\s*(.*?)\)\s*\((.*?)\)\)', command)
            if not match:
                return "Error de sintaxis en la definición de la función."
            
            func_name, params, body = match.groups()
            param_list = [p.strip() for p in params.split()] if params else []

            self.functions[func_name] = {'params': param_list, 'body': body.strip()}
            return f"Función '{func_name}' definida con parámetros {param_list}."
        except Exception as e:
            return f"Error al definir la función: {traceback.format_exc()}"

class ModuleManager:
    """
    Clase para manejar la carga de módulos.
    """
    def __init__(self):
        self.loaded_modules = {}

    def load_module(self, module_name):
        """
        Carga un módulo especificado.
        """
        try:
            module = importlib.import_module(module_name)
            self.loaded_modules[module_name] = module
            print(f"Módulo '{module_name}' cargado con éxito.")
        except ModuleNotFoundError:
            print(f"Error: El módulo '{module_name}' no se encuentra. Verifica el nombre e inténtalo nuevamente.")
        except Exception as e:
            print(f"Error al cargar el módulo: {traceback.format_exc()}")

class SimpylInterpreter:
    """
    Intérprete principal para ejecutar comandos.
    """
    def __init__(self):
        self.variables = {}
        self.memory_manager = MemoryManager()
        self.debugger = Debugger()
        self.function_manager = FunctionManager()
        self.module_manager = ModuleManager()
        self.command_count = 0

    def execute_command(self, command):
        """
        Ejecuta un comando dado.
        """
        command = command.strip()
        try:
            if command.startswith("(import"):
                # Maneja la importación de módulos
                module_name = command.split()[1].strip(')')
                return self.module_manager.load_module(module_name)
            elif re.match(r'\(define ', command):
                # Maneja la definición de funciones
                return self.function_manager.handle_function_definition(command)
            elif re.match(r'\(\w+ = ', command):
                # Maneja la asignación de variables
                return self.handle_variable_assignment(command)
            elif command.startswith("(print"):
                # Maneja el comando print
                return self.handle_print(command)
            elif re.match(r'\(\w+\s', command):
                # Maneja la llamada a funciones
                return self.handle_function_call(command)
            else:
                return "Comando no reconocido. Asegúrate de que la sintaxis sea correcta."
        except Exception as e:
            return f"Error al ejecutar el comando: {traceback.format_exc()}"

    def handle_variable_assignment(self, command):
        """
        Maneja la asignación de variables.
        """
        try:
            var_name, expression = re.match(r'\((\w+) = (.*?)\)', command).groups()
            var_name = var_name.strip()
            expression = expression.strip()

            value = self.evaluate_expression(expression)
            self.variables[var_name] = {'value': value}
            return f"{var_name} asignado con valor {value}"
        except Exception as e:
            return f"Error al asignar variable: {traceback.format_exc()}"

    def handle_print(self, command):
        """
        Maneja el comando print.
        """
        try:
            expression = command[7:-1].strip()
            value = self.evaluate_expression(expression)
            print(value)
        except Exception as e:
            print(f"Error en print: {traceback.format_exc()}")

    def evaluate_expression(self, expression):
        """
        Evalúa una expresión de manera segura.
        """
        allowed_operators = {'+', '-', '*', '/', '%', '**'}
        for op in allowed_operators:
            if op in expression:
                return self.safe_eval(expression)
        return eval(expression, {"__builtins__": None}, self.variables)

    def safe_eval(self, expression):
        """
        Realiza una evaluación segura de una expresión.
        """
        tokens = re.findall(r'\d+|[-+*/%**()]', expression)
        result = eval(''.join(tokens))
        return result

    def handle_function_call(self, command):
        """
        Maneja la llamada a funciones.
        """
        try:
            func_call = re.match(r'\((\w+)\s*(.*?)\)', command)
            func_name, params = func_call.groups()
            params = [self.evaluate_expression(p.strip()) for p in params.split()]
            func = self.function_manager.functions[func_name]
            local_vars = dict(zip(func['params'], params))
            local_vars.update(self.variables)
            return eval(func['body'], {"__builtins__": None}, local_vars)
        except Exception as e:
            return f"Error en la llamada a la función: {traceback.format_exc()}"

    def run(self):
        """
        Inicia el bucle principal del intérprete.
        """
        print("Bienvenido a Simpyl. Escriba 'exit' para salir.")
        while True:
            try:
                command = input(f"Simpyl> ")
                if command.lower() == "exit":
                    print("Saliendo de Simpyl...")
                    break
                result = self.execute_command(command)
                if result:
                    print(result)
                self.command_count += 1
                self.memory_manager.monitor_memory(self.command_count)
            except Exception as e:
                print(f"Error: {traceback.format_exc()}. Verifica la sintaxis o el comando.")

if __name__ == "__main__":
    interpreter = SimpylInterpreter()
    interpreter.run()
