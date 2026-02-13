# model.py
class CalculatorModel:
    def __init__(self):
        self._observers = []
        self.current_value = 0
        self.operation = None
        self.previous_value = None

    def attach_observer(self, observer):
        """Registra una vista (u otro observador) para notificar cambios"""
        self._observers.append(observer)

    def _notify_observers(self):
        for observer in self._observers:
            observer.update()

    # ── Operaciones ────────────────────────────────────────────────
    def add_digit(self, digit: str):
        self.current_value = self.current_value * 10 + int(digit)
        self._notify_observers()

    def set_operation(self, op: str):
        if self.operation is not None:
            self.calculate()  # resuelve operación pendiente si la hay
        self.previous_value = self.current_value
        self.current_value = 0
        self.operation = op
        self._notify_observers()

    def calculate(self):
        if self.operation is None or self.previous_value is None:
            return

        try:
            if self.operation == '+':
                self.current_value = self.previous_value + self.current_value
            elif self.operation == '-':
                self.current_value = self.previous_value - self.current_value
            elif self.operation == '*':
                self.current_value = self.previous_value * self.current_value
            elif self.operation == '/':
                if self.current_value == 0:
                    raise ZeroDivisionError("You cannot divide by 0")
                self.current_value = self.previous_value / self.current_value
        except ZeroDivisionError as e:
            self.current_value = 0
            raise e
        finally:
            self.operation = None
            self.previous_value = None
            self._notify_observers()

    def clear(self):
        self.current_value = 0
        self.operation = None
        self.previous_value = None
        self._notify_observers()

    # ── Getters para la vista ──────────────────────────────────────
    def get_display_value(self) -> str:
        return str(self.current_value)

    def get_has_operation_pending(self) -> bool:
        return self.operation is not None