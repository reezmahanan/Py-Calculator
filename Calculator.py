import math


class Calculator:
    def __init__(self):
        """Initialize calculator with default values"""
        self.current_input = ""
        self.result_displayed = False
        self.history = []
    
    def input_number(self, number):
        """Add a number or decimal point to current input"""
        if self.result_displayed:
            self.clear()
        
        if number == '.' and '.' in self.current_input:
            return self  # Return self for method chaining
        
        self.current_input += str(number)
        self.result_displayed = False
        return self
    
    def input_operator(self, operator):
        """Add an operator to current input"""
        if self.current_input and not self.current_input[-1] in ['+', '-', '*', '/']:
            self.current_input += operator
            self.result_displayed = False
        return self
    
    def calculate(self):
        """Perform calculation and return result"""
        try:
            if not self.current_input:
                return self
            
            # Evaluate the expression
            result = eval(self.current_input)
            
            # Add to history
            self.history.append(f"{self.current_input} = {result}")
            
            self.current_input = str(result)
            self.result_displayed = True
            return self
            
        except ZeroDivisionError:
            self.current_input = "Error: Division by zero"
            self.result_displayed = True
            return self
        except:
            self.current_input = "Error: Invalid expression"
            self.result_displayed = True
            return self
    
    def clear(self):
        """Clear the current input"""
        self.current_input = ""
        self.result_displayed = False
        return self
    
    def clear_entry(self):
        """Clear the last entry"""
        self.current_input = ""
        return self
    
    def backspace(self):
        """Remove the last character from current input"""
        if self.current_input:
            self.current_input = self.current_input[:-1]
        return self
    
    def percentage(self):
        """Convert current input to percentage"""
        try:
            value = float(self.current_input)
            self.current_input = str(value / 100)
            return self
        except:
            return self
    
    def toggle_sign(self):
        """Toggle between positive and negative"""
        if self.current_input and self.current_input not in ['+', '-', '*', '/']:
            if self.current_input.startswith('-'):
                self.current_input = self.current_input[1:]
            else:
                self.current_input = '-' + self.current_input
        return self
    
    def square(self):
        """Square the current number"""
        try:
            value = float(self.current_input)
            self.current_input = str(value ** 2)
            return self
        except:
            return self
    
    def square_root(self):
        """Calculate square root of current number"""
        try:
            value = float(self.current_input)
            if value < 0:
                self.current_input = "Error: Negative root"
            else:
                self.current_input = str(value ** 0.5)
            return self
        except:
            return self
    
    def get_display(self):
        """Get the current display value"""
        return self.current_input if self.current_input else "0"
    
    def get_history(self):
        """Get calculation history"""
        return self.history
    
    def clear_history(self):
        """Clear calculation history"""
        self.history = []
        return self


class ScientificCalculator(Calculator):
    def __init__(self):
        """Initialize scientific calculator"""
        super().__init__()
        self.memory = 0
        self.is_radians = True
    
    def memory_store(self, value):
        """Store value in memory"""
        try:
            self.memory = float(value)
            return self
        except:
            return self
    
    def memory_recall(self):
        """Recall value from memory"""
        self.current_input = str(self.memory)
        return self
    
    def memory_clear(self):
        """Clear memory"""
        self.memory = 0
        return self
    
    def memory_add(self, value):
        """Add value to memory"""
        try:
            self.memory += float(value)
            return self
        except:
            return self
    
    def memory_subtract(self, value):
        """Subtract value from memory"""
        try:
            self.memory -= float(value)
            return self
        except:
            return self
    
    def sin(self):
        """Calculate sine"""
        try:
            value = float(self.current_input)
            if not self.is_radians:
                value = math.radians(value)
            self.current_input = str(math.sin(value))
            return self
        except:
            return self
    
    def cos(self):
        """Calculate cosine"""
        try:
            value = float(self.current_input)
            if not self.is_radians:
                value = math.radians(value)
            self.current_input = str(math.cos(value))
            return self
        except:
            return self
    
    def tan(self):
        """Calculate tangent"""
        try:
            value = float(self.current_input)
            if not self.is_radians:
                value = math.radians(value)
            self.current_input = str(math.tan(value))
            return self
        except:
            return self
    
    def toggle_angle_mode(self):
        """Toggle between radians and degrees"""
        self.is_radians = not self.is_radians
        return self
    
    def get_angle_mode(self):
        """Get current angle mode"""
        return "RAD" if self.is_radians else "DEG"


class CalculatorUI:
    def __init__(self):
        """Initialize calculator UI"""
        self.calculator = Calculator()
        self.setup_ui()
    
    def setup_ui(self):
        """Setup text-based user interface"""
        print("=== PYTHON CALCULATOR ===")
        print("Operations: +, -, *, /")
        print("Special: C (Clear), CE (Clear Entry), BS (Backspace)")
        print("Functions: % (Percentage), ± (Toggle Sign), = (Calculate)")
        print("Type 'quit' to exit\n")
    
    def display(self):
        """Display current calculator state"""
        print(f"Display: {self.calculator.get_display()}")
    
    def run(self):
        """Run the calculator interface"""
        import math
        
        while True:
            self.display()
            user_input = input("Enter input: ").strip()
            
            if user_input.lower() == 'quit':
                break
            elif user_input == 'C':
                self.calculator.clear()
            elif user_input == 'CE':
                self.calculator.clear_entry()
            elif user_input == 'BS':
                self.calculator.backspace()
            elif user_input == '%':
                self.calculator.percentage()
            elif user_input == '±':
                self.calculator.toggle_sign()
            elif user_input == '=':
                self.calculator.calculate()
            elif user_input in ['+', '-', '*', '/']:
                self.calculator.input_operator(user_input)
            elif user_input.replace('.', '').isdigit():
                self.calculator.input_number(user_input)
            else:
                print("Invalid input! Please try again.")
            
            print()


# Example usage and demonstration
if __name__ == "__main__":
    # Basic Calculator Demo
    print("=== BASIC CALCULATOR DEMO ===")
    calc = Calculator()
    
    # Method chaining example
    (calc.input_number(5)
        .input_operator('+')
        .input_number(3)
        .input_operator('*')
        .input_number(2)
        .calculate())
    
    print(f"Result: {calc.get_display()}")  # Should show 11
    
    # Clear and try another calculation
    (calc.clear()
        .input_number(10)
        .input_operator('/')
        .input_number(3)
        .calculate())
    
    print(f"Result: {calc.get_display()}")
    print(f"History: {calc.get_history()}")
    
    # Scientific Calculator Demo
    print("\n=== SCIENTIFIC CALCULATOR DEMO ===")
    sci_calc = ScientificCalculator()
    
    # Square root calculation
    (sci_calc.input_number(16)
        .square_root())
    
    print(f"Square root of 16: {sci_calc.get_display()}")
    
    # Interactive UI
    print("\n=== INTERACTIVE MODE ===")
    ui = CalculatorUI()
    ui.run()