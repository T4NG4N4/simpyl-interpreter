import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import pyperclip
from translate import Translator
import pygments
from pygments.lexers import PythonLexer
from pygments.styles import get_style_by_name
import re

# Clase para el resaltado de sintaxis en el widget Text
class SyntaxHighlightingText(tk.Text):
    def __init__(self, *args, **kwargs):
        tk.Text.__init__(self, *args, **kwargs)
        self.lexer = PythonLexer()  # Usar el lexer de Python de Pygments
        self.style = get_style_by_name('monokai')  # Usar el estilo 'monokai' de Pygments
        self.configure_tags()  # Configurar las etiquetas de estilo

    def configure_tags(self):
        # Configurar las etiquetas de estilo basadas en los tokens de Pygments
        for token, style in self.style:
            if style['color']:
                self.tag_configure(str(token), foreground='#' + style['color'])
            if style['bgcolor']:
                self.tag_configure(str(token), background='#' + style['bgcolor'])

    def highlight(self, event=None):
        # Resaltar el texto en el widget
        self.remove_tags()  # Eliminar etiquetas existentes
        code = self.get("1.0", tk.END)  # Obtener el contenido del widget
        for token, content in self.lexer.get_tokens(code):
            self.insert_tag(token, content)  # Insertar etiquetas para los tokens

    def insert_tag(self, token, content):
        # Insertar una etiqueta para un token específico
        start = self.index(tk.INSERT)
        self.insert(start, content)
        self.tag_add(str(token), start, self.index(tk.INSERT))

    def remove_tags(self):
        # Eliminar todas las etiquetas del texto
        for tag in self.tag_names():
            self.tag_remove(tag, "1.0", tk.END)

# Clase para el autocompletado en el widget Text
class AutoComplete:
    def __init__(self, text_widget):
        self.text_widget = text_widget
        self.words = set()  # Conjunto de palabras para autocompletar
        self.text_widget.bind("<KeyRelease>", self.on_key_release)  # Vincular evento de liberación de tecla

    def add_words(self, words):
        # Añadir palabras al conjunto de palabras para autocompletar
        self.words.update(words)

    def on_key_release(self, event):
        # Evento de liberación de tecla
        if event.keysym in {'Return', 'Tab', 'BackSpace'}:
            return
        current_text = self.text_widget.get("1.0", tk.END).split()
        if current_text:
            prefix = current_text[-1]  # Obtener el prefijo actual
            matches = [w for w in self.words if w.startswith(prefix)]  # Encontrar coincidencias
            if matches:
                self.show_popup(matches, prefix)

    def show_popup(self, matches, prefix):
        # Mostrar un popup con las coincidencias de autocompletado
        popup = tk.Toplevel(self.text_widget)
        popup.geometry("+%d+%d" % (self.text_widget.winfo_rootx(), self.text_widget.winfo_rooty()))
        popup.wm_overrideredirect(True)
        listbox = tk.Listbox(popup)
        listbox.pack()
        for match in matches:
            listbox.insert(tk.END, match)  # Insertar coincidencias en la lista

        def on_select(event):
            # Evento de selección de una coincidencia
            selected = listbox.get(tk.ACTIVE)
            current_text = self.text_widget.get("1.0", tk.END).split()
            current_text[-1] = selected
            self.text_widget.delete("1.0", tk.END)
            self.text_widget.insert(tk.END, ' '.join(current_text))
            popup.destroy()

        listbox.bind("<<ListboxSelect>>", on_select)  # Vincular evento de selección

# Clase principal de la interfaz de usuario del IDE
class SimpylIDE:
    def __init__(self, root):
        self.root = root
        self.root.title("Simpyl IDE")

        # Crear el widget de texto con resaltado de sintaxis
        self.editor = SyntaxHighlightingText(root, wrap=tk.WORD, undo=True)
        self.editor.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)
        
        # Configurar el autocompletado
        self.autocomplete = AutoComplete(self.editor)
        self.autocomplete.add_words(['import', 'from', 'def', 'class', 'try', 'except', 'finally', 'for', 'while', 'if', 'else', 'elif', 'return', 'print', 'self', 'True', 'False', 'None'])

        # Crear el botón de ejecutar
        self.run_button = ttk.Button(root, text="Ejecutar", command=self.run_code)
        self.run_button.pack(padx=10, pady=5)

        # Crear el widget de texto para la salida
        self.output = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=10, state='disabled')
        self.output.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)

    def run_code(self):
        # Ejecutar el código escrito en el editor
        code = self.editor.get("1.0", tk.END)
        self.output.config(state='normal')
        self.output.delete("1.0", tk.END)

        try:
            exec(code, globals())  # Ejecutar el código
        except Exception as e:
            # Mostrar errores en la salida
            self.output.insert(tk.END, f"Error: {str(e)}\n")
            self.output.insert(tk.END, traceback.format_exc())
        
        self.output.config(state='disabled')
        self.editor.highlight()  # Resaltar el código después de la ejecución

# Clase del intérprete Simpyl
class SimpylInterpreter:
    def __init__(self):
        self.variables = {}
        self.memory_manager = MemoryManager()
        self.debugger = Debugger()
        self.function_manager = FunctionManager()
        self.module_manager = ModuleManager()
        self.command_count = 0

    def execute_command(self, command):
        # Ejecutar un comando dado
        command = command.strip()
        try:
            if command.startswith("(import"):
                module_name = command.split()[1].strip(')')
                return self.module_manager.load_module(module_name)
            elif re.match(r'\(define ', command):
                return self.function_manager.handle_function_definition(command)
            elif re.match(r'\(\w+ = ', command):
                return self.handle_variable_assignment(command)
            elif command.startswith("(print"):
                return self.handle_print(command)
            elif re.match(r'\(\w+\s', command):
                return self.handle_function_call(command)
            else:
                return "Comando no reconocido."
        except Exception as e:
            error_message = f"Error al ejecutar el comando: {traceback.format_exc()}"
            print(error_message)
            return error_message

    def handle_variable_assignment(self, command):
        # Manejar la asignación de variables
        try:
            var_name, expression = re.match(r'\((\w+) = (.*?)\)', command).groups()
            var_name = var_name.strip()
            expression = expression.strip()

            value = self.evaluate_expression(expression)
            self.variables[var_name] = {'value': value}
            return f"{var_name} asignado con valor {value}"
        except Exception as e:
            error_message = f"Error al asignar variable: {traceback.format_exc()}"
            print(error_message)
            return error_message

    def handle_print(self, command):
        # Manejar el comando print
        try:
            expression = command[7:-1].strip()
            value = self.evaluate_expression(expression)
            print(value)
        except Exception as e:
            error_message = f"Error en print: {traceback.format_exc()}"
            print(error_message)

    def evaluate_expression(self, expression):
        # Evaluar una expresión de manera segura
        allowed_operators = {'+', '-', '*', '/', '%', '**'}
        for op in allowed_operators:
            if op in expression:
                return self.safe_eval(expression)
        return eval(expression, {"__builtins__": None}, self.variables)

    def safe_eval(self, expression):
        # Realizar una evaluación segura de una expresión
        tokens = re.findall(r'\d+|[-+*/%**()]', expression)
        result = eval(''.join(tokens))
        return result

    def handle_function_call(self, command):
        # Manejar la llamada a funciones
        try:
            func_call = re.match(r'\((\w+)\s*(.*?)\)', command)
            func_name, params = func_call.groups()
            params = [self.evaluate_expression(p.strip()) for p in params.split()]
            func = self.function_manager.functions[func_name]
            local_vars = dict(zip(func['params'], params))
            local_vars.update(self.variables)
            return eval(func['body'], {"__builtins__": None}, local_vars)
        except Exception as e:
            error_message = f"Error en la llamada a la función: {traceback.format_exc()}"
            print(error_message)
            return error_message

if __name__ == "__main__":
    # Crear la ventana principal y ejecutar el IDE
    root = tk.Tk()
    ide = SimpylIDE(root)
    root.mainloop()
