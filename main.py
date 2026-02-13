# main.py
from model import CalculatorModel
from view import CalculatorView
from controller import CalculatorController

if __name__ == "__main__":
    # 1. Crear el modelo (datos + lógica pura)
    model = CalculatorModel()

    # 2. Crear la vista (aún sin controlador asignado)
    view = CalculatorView(None)           # temporalmente None

    # 3. Crear el controlador (conecta model ↔ view)
    controller = CalculatorController(model, view)

    # 4. Ahora sí: conectar la vista al controlador
    view.controller = controller

    # 5. Refrescar la vista una sola vez al inicio (muestra "0")
    view.update()

    # 6. Iniciar el loop de eventos
    view.mainloop()