# MVC Calculator with Python and Tkinter

A simple desktop calculator application that strictly follows the **Model-View-Controller (MVC)** pattern.

## How the Application Works

The calculator supports basic arithmetic operations with integers:

- Pressing a digit (0–9) appends it to the current number on the display.
- Pressing an operator (+, -, ×, ÷) stores the pending operation and prepares for the next number.
- Pressing "=" performs the stored operation and shows the result.
- Pressing "C" resets everything to zero.
- If you try to divide by zero, an error message appears and the calculator is cleared.

The display updates automatically after every action thanks to the **Observer** pattern.

## How the MVC Pattern Was Applied

| Component       | File            | Main Responsibility                                        | Knows about...                  |
|-----------------|-----------------|------------------------------------------------------------|---------------------------------|
| **Model**       | `model.py`      | Manages state (numbers and pending operation) and performs all math calculations. Notifies observers of changes. | Nobody (completely independent) |
| **View**        | `view.py`       | Builds and displays the graphical interface (window, display, buttons). Updates the screen when notified by the Model. Forwards button events to the Controller. | Controller                      |
| **Controller**  | `controller.py` | Receives button events, interprets them, calls appropriate Model methods, handles errors, and coordinates between Model and View. | Model and View                  |
| **Orchestrator** | `main.py`      | Creates instances of Model, View, and Controller in the correct order and resolves circular dependencies. | All components                  |

- **Data flow**: Model → View (via Observer notifications)
- **Event flow**: View → Controller → Model
- No direct communication between Model and View (only through Controller and Observer registration)

## How to Run the Application

1. Make sure you have **Python 3.8 or higher** installed  
   (Tkinter is included by default in most installations. On Windows, ensure "tcl/tk and IDLE" was selected during Python setup if it's missing.)

2. Clone the repository:

   ```bash
   git clone https://github.com/ELmiuni/CalculatorMVC.git
   cd CalculatorMVC

3. 
    python main.py

## Project organzation
CalculatorMVC/
├── main.py           # Entry point – creates and connects Model, View, and Controller
├── model.py          # Pure math logic and state (no UI knowledge)
├── view.py           # Graphical interface and visual updates
├── controller.py     # User event handling and coordination
└── README.md         # This documentation

