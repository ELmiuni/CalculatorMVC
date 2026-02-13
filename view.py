# view.py
import tkinter as tk
from tkinter import messagebox

class CalculatorView(tk.Tk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller or None
        self.title("Calculator MVC")
        self.geometry("320x420")
        self.resizable(False, False)

        # Pantalla
        self.display = tk.Entry(
            self,
            font=("Consolas", 28),
            justify="right",
            bd=10,
            relief="sunken"
        )
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

        # Botones
        buttons_layout = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3),
        ]

        for (text, row, col) in buttons_layout:
            cmd = lambda t=text: self.controller.on_button_press(t) if self.controller else None
            btn = tk.Button(
                self,
                text=text,
                font=("Arial", 18),
                command=cmd,
                width=5,
                height=2
            )
            btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

        # Configurar expansión
        for i in range(5):
            self.grid_rowconfigure(i, weight=1)
        for j in range(4):
            self.grid_columnconfigure(j, weight=1)

    def update(self):
        """Método llamado por el modelo cuando hay cambios"""
        if self.controller is None or self.controller.model is None:
            self.display.delete(0, tk.END)
            self.display.insert(0, "0")
            return
        self.display.delete(0, tk.END)
        self.display.insert(0, self.controller.model.get_display_value())

    def show_error(self, message: str):
        messagebox.showerror("Error", message)