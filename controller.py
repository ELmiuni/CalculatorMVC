# controller.py
class CalculatorController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        # Conectar la vista como observadora del modelo
        self.model.attach_observer(self.view)

    def on_button_press(self, button: str):
        try:
            if button.isdigit():
                self.model.add_digit(button)

            elif button in ['+', '-', '*', '/']:
                self.model.set_operation(button)

            elif button == '=':
                self.model.calculate()

            elif button == 'C':
                self.model.clear()

        except ZeroDivisionError:
            self.view.show_error("You cannot divide by 0")
            self.model.clear()
        except Exception as e:
            self.view.show_error(f"Unexpected error: {str(e)}")
            self.model.clear()