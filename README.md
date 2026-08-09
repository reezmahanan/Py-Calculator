# Python Calculator 

A feature-rich calculator implementation in Python using Object-Oriented Programming (OOP) concepts. Includes both basic and scientific calculator functionalities with a clean, interactive interface.

![Calculator GUI Screenshot](screenshot.png)

## Features 

### Basic Calculator
- **Arithmetic Operations**: Addition, Subtraction, Multiplication, Division
- **Advanced Functions**: 
  - Percentage calculations
  - Sign toggle ()
  - Square and Square root
  - Backspace and Clear functions
- **Calculation History**: Keeps track of all calculations
- **Error Handling**: Graceful handling of division by zero and invalid expressions

### Scientific Calculator
- **Trigonometric Functions**: sin, cos, tan (with radians/degrees toggle)
- **Memory Operations**: Store, recall, add to, subtract from memory
- **Angle Mode**: Switch between radians and degrees

## Installation & Setup 🚀

1. **Clone the repository**:
   ```bash
   git clone https://github.com/reezmahanan/Py-Calculator.git
   cd Py-Calculator
   ```

2. **Install the modern GUI dependency**:
   ```powershell
   pip install customtkinter
   ```

3. **Run the calculator**:
   - **GUI Desktop Version (Recommended)**:
     ```powershell
     python .\CalculatorGUI.py
     ```
   - **CLI Text-based Version**:
     ```powershell
     python .\Calculator.py
     ```

## Usage

Run the application of your choice from the repository folder:

- **For the Desktop GUI App**:
  ```powershell
  python .\CalculatorGUI.py
  ```
- **For the CLI Version**:
  ```powershell
  python .\Calculator.py
  ```

### Interactive Mode
- **Operations**: `+`, `-`, `*`, `/`
- **Special Keys**:
  - `C`: Clear all
  - `CE`: Clear entry
  - `BS`: Backspace
  - `%`: Percentage
  - ``: Toggle sign
  - `=`: Calculate current expression
- Type `quit` to exit

## Examples
- Basic calculation: `5 + 3 * 2`  `11`
- Scientific: Square root of 16  `4.0`

## Files
- `Calculator.py`: Main code containing `Calculator`, `ScientificCalculator`, and a simple text UI.

## Notes
- The calculator uses Python's `eval` for expression evaluation in the demo. Do not pass untrusted input to `eval` in production contexts.
- The interactive mode expects simple token-like inputs (numbers or operators). For more complex usage, extend the `CalculatorUI` parsing logic.

## Future Improvements
- Safer expression evaluator (no `eval`)
- Improved interactive input parsing
- GUI front-end
