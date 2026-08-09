# 🧮 Py-Calculator

A modern, highly aesthetic, and feature-rich Python desktop calculator built using Object-Oriented Programming (OOP) principles. It offers both a **minimalist CLI interface** and a **premium, interactive Desktop GUI** powered by CustomTkinter.

---

## 🎨 Preview

![Calculator GUI Screenshot](https://github.com/reezmahanan/Py-Calculator/blob/main/Screenshot.png)

---

## ✨ Features

### 🖥️ Desktop GUI (Recommended)
- **Aesthetic Dark & Light Themes**: Sleek, glassmorphic layout inspired by modern operating systems, with a toggle switch (☀️/🌙).
- **Dynamic Layouts**: Easily switch between **Basic** and **Scientific** modes from a segmented tab. The window and layout resize dynamically.
- **Interactive Micro-Animations**: Buttons briefly highlight/flash upon mouse clicks and physical keyboard presses.
- **Scrollable History Sidebar**: Slide-out panel that tracks your calculations. Clicking on a history card loads its expression back into the display.
- **Full Keyboard Integration**: Supports desktop execution via numeric keys, decimal points, standard operators, bracket keys, Backspace, Escape, and Enter.
- **Status Indicators**: Clean labels displaying active Angle Mode (`RAD`/`DEG`) and current memory values (`M = ...`).

### 📚 Scientific Capabilities
- **Trigonometric Functions**: `sin`, `cos`, and `tan` supporting both degrees and radians.
- **Memory Operations**: `MC` (Clear), `MR` (Recall), `MS` (Store), `M+` (Add), and `M-` (Subtract).
- **Brackets**: Supports parentheses `(` and `)` to evaluate complex algebraic expressions.
- **Constants & Operators**: Built-in inputs for Pi (`π`), Euler's number (`e`), squaring (`x²`), square root (`√`), sign toggle (`±`), and percentages (`%`).
- **Error Resilience**: Intercepts syntax errors and division by zero exceptions, presenting warning alerts without disrupting input flow.

---

## 📂 Project Structure

```text
Py-Calculator/
│
├── .venv/                  # Local Python Virtual Environment
├── Calculator.py           # Core logic (Calculator, ScientificCalculator & CLI UI)
├── CalculatorGUI.py        # Desktop GUI implementation (CustomTkinter App)
├── Screenshot.png          # Visual representation of the GUI
└── README.md               # Project documentation
```

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/reezmahanan/Py-Calculator.git
cd Py-Calculator
```

### 2. Set Up & Install Dependencies
It is highly recommended to install the dependencies inside your project's virtual environment (`.venv`):

```powershell
# Activate your virtual environment (Windows PowerShell)
.\.venv\Scripts\Activate.ps1

# Install CustomTkinter
pip install customtkinter
```

### 3. Running the Application

- **Run the Desktop GUI (Recommended)**:
  ```powershell
  python .\CalculatorGUI.py
  ```

- **Run the CLI Interface**:
  ```powershell
  python .\Calculator.py
  ```

---

## ⌨️ Keyboard Shortcuts

| Action | Physical Key |
| :--- | :--- |
| **Digits & Dot** | `0` - `9` , `.` |
| **Operators** | `+` , `-` , `*` , `/` |
| **Brackets** | `(` , `)` |
| **Calculate Result** | `Enter` / `Return` or `=` |
| **Delete Last Input** | `Backspace` |
| **Clear Display** | `Escape` |

---

## 🛡️ License & Disclaimers
This project uses Python's standard library `eval` safely caught inside robust OOP exception handlers for mathematical calculations. For production-level parsers, replace `eval` with a safe abstract syntax tree (AST) validator.
