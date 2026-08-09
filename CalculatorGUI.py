import math
import customtkinter as ctk
from Calculator import ScientificCalculator

# Set initial appearance
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class CalculatorApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Initialize Backend
        self.calculator = ScientificCalculator()
        
        # Window Configuration
        self.title("Py-Calculator")
        self.configure(fg_color=("#F3F4F6", "#121212"))
        
        # Layout State
        self.current_mode = "Basic"  # "Basic" or "Scientific"
        self.history_visible = False
        
        # Button Mapping for Keyboard Visual Feedback
        self.btn_map = {}
        
        # Setup UI
        self.setup_ui()
        self.render_layout()
        self.bind_keyboard()
        
    def setup_ui(self):
        # Configure Grid Rows for main window
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        
        # Main Container
        self.main_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.main_frame.grid(row=0, column=0, sticky="nsew", padx=15, pady=15)
        
        self.main_frame.rowconfigure(0, weight=0)  # Top Menu/Toggle Bar
        self.main_frame.rowconfigure(1, weight=0)  # Display Block
        self.main_frame.rowconfigure(2, weight=1)  # Grid Buttons and History Panel
        self.main_frame.columnconfigure(0, weight=1)
        
        # ----------------------------------------------------
        # 1. Top Menu/Toggle Bar
        # ----------------------------------------------------
        self.top_bar = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.top_bar.grid(row=0, column=0, sticky="ew", pady=(0, 10))
        
        # Mode Selector (Basic / Scientific)
        self.mode_toggle = ctk.CTkSegmentedButton(
            self.top_bar,
            values=["Basic", "Scientific"],
            command=self.toggle_mode,
            font=("Segoe UI", 12, "bold"),
            selected_color=("#6366F1", "#7C3AED")
        )
        self.mode_toggle.set("Basic")
        self.mode_toggle.pack(side="left")
        
        # Theme Button
        self.theme_btn = ctk.CTkButton(
            self.top_bar,
            text="🌙",
            width=40,
            fg_color=("#E5E7EB", "#2D2D2D"),
            text_color=("#1F2937", "#FFFFFF"),
            hover_color=("#D1D5DB", "#3D3D3D"),
            font=("Segoe UI", 14),
            command=self.toggle_theme
        )
        self.theme_btn.pack(side="right", padx=(5, 0))
        
        # History Toggle Button
        self.history_toggle_btn = ctk.CTkButton(
            self.top_bar,
            text="📜 History",
            width=90,
            fg_color=("#E5E7EB", "#2D2D2D"),
            text_color=("#1F2937", "#FFFFFF"),
            hover_color=("#D1D5DB", "#3D3D3D"),
            font=("Segoe UI", 12, "bold"),
            command=self.toggle_history_panel
        )
        self.history_toggle_btn.pack(side="right")
        
        # ----------------------------------------------------
        # 2. Display Block
        # ----------------------------------------------------
        self.display_frame = ctk.CTkFrame(
            self.main_frame,
            fg_color=("#FFFFFF", "#1E1E1E"),
            border_color=("#E5E7EB", "#2D2D2D"),
            border_width=1,
            corner_radius=12
        )
        self.display_frame.grid(row=1, column=0, sticky="ew", pady=(0, 15))
        
        # Inner padding and layout
        self.display_frame.columnconfigure(0, weight=1)
        
        # Info bar (Memory and Angle mode indicator)
        self.info_frame = ctk.CTkFrame(self.display_frame, fg_color="transparent", height=20)
        self.info_frame.grid(row=0, column=0, sticky="ew", padx=15, pady=(8, 0))
        
        self.memory_label = ctk.CTkLabel(
            self.info_frame,
            text="",
            font=("Segoe UI", 11, "bold"),
            text_color=("#4F46E5", "#A78BFA")
        )
        self.memory_label.pack(side="left")
        
        self.angle_label = ctk.CTkLabel(
            self.info_frame,
            text="RAD",
            font=("Segoe UI", 11, "bold"),
            text_color=("#6B7280", "#9CA3AF")
        )
        self.angle_label.pack(side="right")
        
        # Running expression label (small, top)
        self.running_expr_label = ctk.CTkLabel(
            self.display_frame,
            text="",
            font=("Segoe UI", 14),
            text_color=("#6B7280", "#9CA3AF"),
            anchor="e"
        )
        self.running_expr_label.grid(row=1, column=0, sticky="ew", padx=15, pady=(2, 2))
        
        # Main screen display (large, bold)
        self.display_label = ctk.CTkLabel(
            self.display_frame,
            text="0",
            font=("Segoe UI", 36, "bold"),
            text_color=("#1F2937", "#FFFFFF"),
            anchor="e"
        )
        self.display_label.grid(row=2, column=0, sticky="ew", padx=15, pady=(0, 10))
        
        # ----------------------------------------------------
        # 3. Content Area (Scientific, Basic Grid, History)
        # ----------------------------------------------------
        self.content_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.content_frame.grid(row=2, column=0, sticky="nsew")
        self.content_frame.rowconfigure(0, weight=1)
        
        # Create Subframes
        self.setup_sci_frame()
        self.setup_basic_frame()
        self.setup_history_frame()

    # ----------------------------------------------------
    # Frame Setups
    # ----------------------------------------------------
    def setup_basic_frame(self):
        self.basic_frame = ctk.CTkFrame(self.content_frame, fg_color="transparent")
        
        # Grid layout: 5 rows, 4 columns
        for i in range(5):
            self.basic_frame.rowconfigure(i, weight=1)
        for j in range(4):
            self.basic_frame.columnconfigure(j, weight=1)
            
        # Button styles (tuples: light_theme, dark_theme)
        num_color = (("#E5E7EB", "#2D2D2D"), ("#D1D5DB", "#3D3D3D")) # fg, hover
        num_text = ("#1F2937", "#FFFFFF")
        
        op_color = (("#F3F4F6", "#252525"), ("#E5E7EB", "#333333"))
        op_text = ("#4F46E5", "#A78BFA")
        
        eq_color = ("#6366F1", "#7C3AED")
        eq_hover = ("#4F46E5", "#6D28D9")
        
        sp_color = (("#F3F4F6", "#252525"), ("#E5E7EB", "#333333"))
        sp_text = ("#EF4444", "#F87171")  # Red accent for Clear / delete
        
        # Basic buttons definition
        buttons = [
            ("CE", 0, 0, sp_color[0], sp_color[1], sp_text, lambda: self.press_clear_entry()),
            ("C",  0, 1, sp_color[0], sp_color[1], sp_text, lambda: self.press_clear()),
            ("⌫", 0, 2, sp_color[0], sp_color[1], sp_text, lambda: self.press_backspace()),
            ("/",  0, 3, op_color[0], op_color[1], op_text, lambda: self.press_operator("/")),
            
            ("7",  1, 0, num_color[0], num_color[1], num_text, lambda: self.press_number("7")),
            ("8",  1, 1, num_color[0], num_color[1], num_text, lambda: self.press_number("8")),
            ("9",  1, 2, num_color[0], num_color[1], num_text, lambda: self.press_number("9")),
            ("*",  1, 3, op_color[0], op_color[1], op_text, lambda: self.press_operator("*")),
            
            ("4",  2, 0, num_color[0], num_color[1], num_text, lambda: self.press_number("4")),
            ("5",  2, 1, num_color[0], num_color[1], num_text, lambda: self.press_number("5")),
            ("6",  2, 2, num_color[0], num_color[1], num_text, lambda: self.press_number("6")),
            ("-",  2, 3, op_color[0], op_color[1], op_text, lambda: self.press_operator("-")),
            
            ("1",  3, 0, num_color[0], num_color[1], num_text, lambda: self.press_number("1")),
            ("2",  3, 1, num_color[0], num_color[1], num_text, lambda: self.press_number("2")),
            ("3",  3, 2, num_color[0], num_color[1], num_text, lambda: self.press_number("3")),
            ("+",  3, 3, op_color[0], op_color[1], op_text, lambda: self.press_operator("+")),
            
            ("±",  4, 0, num_color[0], num_color[1], num_text, lambda: self.press_unary("toggle_sign")),
            ("0",  4, 1, num_color[0], num_color[1], num_text, lambda: self.press_number("0")),
            (".",  4, 2, num_color[0], num_color[1], num_text, lambda: self.press_number(".")),
            ("=",  4, 3, eq_color, eq_hover, "#FFFFFF", lambda: self.press_equal())
        ]
        
        for text, row, col, fg, hover, text_col, cmd in buttons:
            btn = ctk.CTkButton(
                self.basic_frame,
                text=text,
                fg_color=fg,
                hover_color=hover,
                text_color=text_col,
                font=("Segoe UI", 18, "bold"),
                corner_radius=8,
                command=cmd
            )
            btn.grid(row=row, column=col, sticky="nsew", padx=3, pady=3)
            self.btn_map[text] = btn
            
    def setup_sci_frame(self):
        self.sci_frame = ctk.CTkFrame(self.content_frame, fg_color="transparent")
        
        # Grid layout: 4 rows, 4 columns
        for i in range(4):
            self.sci_frame.rowconfigure(i, weight=1)
        for j in range(4):
            self.sci_frame.columnconfigure(j, weight=1)
            
        # Button Styles
        fn_color = (("#E5E7EB", "#202020"), ("#D1D5DB", "#2E2E2E"))
        fn_text = ("#374151", "#E5E7EB")
        
        mem_color = (("#F3F4F6", "#252525"), ("#E5E7EB", "#333333"))
        mem_text = ("#4F46E5", "#A78BFA")
        
        sci_buttons = [
            ("MC",      0, 0, mem_color[0], mem_color[1], mem_text, lambda: self.press_memory("MC")),
            ("MR",      0, 1, mem_color[0], mem_color[1], mem_text, lambda: self.press_memory("MR")),
            ("M+",      0, 2, mem_color[0], mem_color[1], mem_text, lambda: self.press_memory("M+")),
            ("M-",      0, 3, mem_color[0], mem_color[1], mem_text, lambda: self.press_memory("M-")),
            
            ("MS",      1, 0, mem_color[0], mem_color[1], mem_text, lambda: self.press_memory("MS")),
            ("DEG/RAD", 1, 1, fn_color[0], fn_color[1], fn_text, lambda: self.press_angle_mode()),
            ("(",       1, 2, fn_color[0], fn_color[1], fn_text, lambda: self.press_number("(")),
            (")",       1, 3, fn_color[0], fn_color[1], fn_text, lambda: self.press_number(")")),
            
            ("sin",     2, 0, fn_color[0], fn_color[1], fn_text, lambda: self.press_unary("sin")),
            ("cos",     2, 1, fn_color[0], fn_color[1], fn_text, lambda: self.press_unary("cos")),
            ("tan",     2, 2, fn_color[0], fn_color[1], fn_text, lambda: self.press_unary("tan")),
            ("π",       2, 3, fn_color[0], fn_color[1], fn_text, lambda: self.press_number(str(math.pi))),
            
            ("x²",      3, 0, fn_color[0], fn_color[1], fn_text, lambda: self.press_unary("square")),
            ("√",       3, 1, fn_color[0], fn_color[1], fn_text, lambda: self.press_unary("sqrt")),
            ("e",       3, 2, fn_color[0], fn_color[1], fn_text, lambda: self.press_number(str(math.e))),
            ("%",       3, 3, fn_color[0], fn_color[1], fn_text, lambda: self.press_unary("percentage"))
        ]
        
        for text, row, col, fg, hover, text_col, cmd in sci_buttons:
            btn = ctk.CTkButton(
                self.sci_frame,
                text=text,
                fg_color=fg,
                hover_color=hover,
                text_color=text_col,
                font=("Segoe UI", 15, "bold"),
                corner_radius=8,
                command=cmd
            )
            btn.grid(row=row, column=col, sticky="nsew", padx=3, pady=3)
            self.btn_map[text] = btn
            
    def setup_history_frame(self):
        self.history_frame = ctk.CTkFrame(
            self.content_frame,
            fg_color=("#FFFFFF", "#1E1E1E"),
            border_color=("#E5E7EB", "#2D2D2D"),
            border_width=1,
            corner_radius=12,
            width=240
        )
        self.history_frame.grid_propagate(False)
        self.history_frame.rowconfigure(0, weight=0) # Header
        self.history_frame.rowconfigure(1, weight=1) # Scroll list
        self.history_frame.rowconfigure(2, weight=0) # Clear button
        self.history_frame.columnconfigure(0, weight=1)
        
        # Header
        self.history_header = ctk.CTkLabel(
            self.history_frame,
            text="History",
            font=("Segoe UI", 16, "bold"),
            text_color=("#1F2937", "#FFFFFF")
        )
        self.history_header.grid(row=0, column=0, sticky="w", padx=15, pady=10)
        
        # Scrollable container for calculations
        self.history_list_frame = ctk.CTkScrollableFrame(self.history_frame, fg_color="transparent")
        self.history_list_frame.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
        
        # Clear Button
        self.clear_history_btn = ctk.CTkButton(
            self.history_frame,
            text="Clear History 🗑️",
            fg_color="transparent",
            text_color=("#EF4444", "#F87171"),
            hover_color=("#FEE2E2", "#3F1E1E"),
            font=("Segoe UI", 13, "bold"),
            command=self.clear_history
        )
        self.clear_history_btn.grid(row=2, column=0, sticky="ew", padx=15, pady=10)

    # ----------------------------------------------------
    # Interactive Actions
    # ----------------------------------------------------
    def toggle_mode(self, mode):
        self.current_mode = mode
        self.render_layout()
        
    def toggle_theme(self):
        if ctk.get_appearance_mode() == "Dark":
            ctk.set_appearance_mode("Light")
            self.theme_btn.configure(text="☀️")
        else:
            ctk.set_appearance_mode("Dark")
            self.theme_btn.configure(text="🌙")
            
    def toggle_history_panel(self):
        self.history_visible = not self.history_visible
        self.render_layout()
        if self.history_visible:
            self.update_history_ui()
            
    def render_layout(self):
        # Forget layouts
        self.sci_frame.grid_forget()
        self.basic_frame.grid_forget()
        self.history_frame.grid_forget()
        
        # Configure columns
        self.content_frame.columnconfigure(0, weight=1)
        self.content_frame.columnconfigure(1, weight=1)
        self.content_frame.columnconfigure(2, weight=0)
        
        if self.current_mode == "Scientific":
            # Column 0: Scientific, Column 1: Basic
            self.sci_frame.grid(row=0, column=0, sticky="nsew", padx=(0, 5))
            self.basic_frame.grid(row=0, column=1, sticky="nsew", padx=(5, 0))
            if self.history_visible:
                self.history_frame.grid(row=0, column=2, sticky="nsew", padx=(15, 0))
        else:
            # Column 0: Basic
            self.basic_frame.grid(row=0, column=0, sticky="nsew")
            if self.history_visible:
                self.history_frame.grid(row=0, column=1, sticky="nsew", padx=(15, 0))
                
        self.update_window_size()
        
    def update_window_size(self):
        # Standard sizes
        base_width = 360
        if self.current_mode == "Scientific":
            base_width += 340
        if self.history_visible:
            base_width += 250
            
        self.geometry(f"{base_width}x560")
        self.minsize(base_width, 560)
        
    # ----------------------------------------------------
    # Calculator Operations & Event Handlers
    # ----------------------------------------------------
    def update_display(self):
        display_val = self.calculator.get_display()
        
        # Formatting decimal numbers nicely if they are floats
        if display_val not in ["Error: Division by zero", "Error: Invalid expression", "Error: Negative root"]:
            try:
                # If it's a clean float ending in .0, display as int
                val_float = float(display_val)
                if val_float.is_integer():
                    display_val = str(int(val_float))
                else:
                    # Truncate very long float displays to keep it clean
                    display_val = f"{val_float:.10g}"
            except ValueError:
                pass
                
        self.display_label.configure(text=display_val)
        
        # Display running expression
        if self.calculator.result_displayed and self.calculator.history:
            # Get the expression before the '='
            last_hist = self.calculator.history[-1]
            if "=" in last_hist:
                expr = last_hist.split("=")[0].strip()
                self.running_expr_label.configure(text=f"{expr} =")
        else:
            self.running_expr_label.configure(text=self.calculator.current_input)
            
    def update_memory_indicator(self):
        if self.calculator.memory != 0:
            mem_val = self.calculator.memory
            if mem_val.is_integer():
                mem_val = int(mem_val)
            self.memory_label.configure(text=f"M = {mem_val}")
        else:
            self.memory_label.configure(text="")
            
    def update_history_ui(self):
        # Clear history scroll list
        for widget in self.history_list_frame.winfo_children():
            widget.destroy()
            
        history = self.calculator.get_history()
        if not history:
            no_hist_label = ctk.CTkLabel(
                self.history_list_frame,
                text="No history yet",
                font=("Segoe UI", 12, "italic"),
                text_color=("#9CA3AF", "#6B7280")
            )
            no_hist_label.pack(pady=20)
            return
            
        # Reverse history to show latest first
        for item in reversed(history):
            if "=" not in item:
                continue
            expr, res = item.split("=", 1)
            expr = expr.strip()
            res = res.strip()
            
            # Format numbers in res if possible
            try:
                res_float = float(res)
                if res_float.is_integer():
                    res = str(int(res_float))
                else:
                    res = f"{res_float:.10g}"
            except ValueError:
                pass
                
            # Calculation Box button
            btn_frame = ctk.CTkFrame(self.history_list_frame, fg_color="transparent")
            btn_frame.pack(fill="x", pady=4)
            
            hist_btn = ctk.CTkButton(
                btn_frame,
                text=f"{expr} =\n{res}",
                font=("Segoe UI", 13),
                anchor="e",
                fg_color=("#F3F4F6", "#252525"),
                hover_color=("#E5E7EB", "#2E2E2E"),
                text_color=("#374151", "#FFFFFF"),
                justify="right",
                corner_radius=6,
                command=lambda e=expr: self.load_history_item(e)
            )
            hist_btn.pack(fill="x", padx=2, pady=1)

    def load_history_item(self, expression):
        # Intercept errors
        if "Error" in expression:
            return
        self.calculator.current_input = expression
        self.calculator.result_displayed = False
        self.update_display()
        
    def clear_history(self):
        self.calculator.clear_history()
        self.update_history_ui()
        
    def press_number(self, num):
        # If showing error, clear first
        if "Error" in self.calculator.get_display():
            self.calculator.clear()
            
        self.calculator.input_number(num)
        self.update_display()
        
    def press_operator(self, op):
        if "Error" in self.calculator.get_display():
            self.calculator.clear()
            
        self.calculator.input_operator(op)
        self.update_display()
        
    def press_clear(self):
        self.calculator.clear()
        self.update_display()
        
    def press_clear_entry(self):
        self.calculator.clear_entry()
        self.update_display()
        
    def press_backspace(self):
        self.calculator.backspace()
        self.update_display()
        
    def press_equal(self):
        if not self.calculator.current_input:
            return
            
        # Prevent equal when error is shown
        if "Error" in self.calculator.get_display():
            self.calculator.clear()
            self.update_display()
            return
            
        self.calculator.calculate()
        self.update_display()
        
        # Update history sidebar if visible
        if self.history_visible:
            self.update_history_ui()
            
    def press_unary(self, operation):
        if "Error" in self.calculator.get_display():
            self.calculator.clear()
            self.update_display()
            return
            
        if not self.calculator.current_input:
            # Assume 0 as default if empty input
            self.calculator.current_input = "0"
            
        if operation == "toggle_sign":
            self.calculator.toggle_sign()
        elif operation == "percentage":
            self.calculator.percentage()
        elif operation == "square":
            self.calculator.square()
        elif operation == "sqrt":
            self.calculator.square_root()
        elif operation == "sin":
            self.calculator.sin()
        elif operation == "cos":
            self.calculator.cos()
        elif operation == "tan":
            self.calculator.tan()
            
        self.update_display()
        
    def press_memory(self, op):
        if "Error" in self.calculator.get_display():
            return
            
        # Evaluate first if we have a pending formula
        if self.calculator.current_input and not self.calculator.result_displayed:
            try:
                # If there's an operator at the end, strip it or ignore
                if not self.calculator.current_input[-1] in ['+', '-', '*', '/']:
                    self.calculator.calculate()
                    self.update_display()
            except:
                pass
                
        val = self.calculator.get_display()
        
        if op == "MC":
            self.calculator.memory_clear()
        elif op == "MR":
            self.calculator.memory_recall()
            self.calculator.result_displayed = False
        elif op == "MS":
            self.calculator.memory_store(val)
        elif op == "M+":
            self.calculator.memory_add(val)
        elif op == "M-":
            self.calculator.memory_subtract(val)
            
        self.update_memory_indicator()
        self.update_display()
        
    def press_angle_mode(self):
        self.calculator.toggle_angle_mode()
        self.angle_label.configure(text=self.calculator.get_angle_mode())

    # ----------------------------------------------------
    # Keyboard Bindings
    # ----------------------------------------------------
    def bind_keyboard(self):
        self.bind("<Key>", self.handle_keypress)
        
    def handle_keypress(self, event):
        char = event.char
        keysym = event.keysym
        
        # Mapping numeric & decimal point
        if char in "0123456789.":
            self.trigger_button_feedback(char, lambda: self.press_number(char))
        # Operators
        elif char in "+-*/":
            self.trigger_button_feedback(char, lambda: self.press_operator(char))
        # Parentheses
        elif char in "()":
            self.trigger_button_feedback(char, lambda: self.press_number(char))
        # Percentage
        elif char == "%":
            self.trigger_button_feedback("%", lambda: self.press_unary("percentage"))
        # Equal (Return or Equal key)
        elif keysym in ["Return", "KP_Enter"] or char == "=":
            self.trigger_button_feedback("=", self.press_equal)
        # Backspace
        elif keysym == "BackSpace":
            self.trigger_button_feedback("⌫", self.press_backspace)
        # Clear (Escape)
        elif keysym == "Escape":
            self.trigger_button_feedback("C", self.press_clear)

    def trigger_button_feedback(self, key_char, action):
        action()
        if key_char in self.btn_map:
            btn = self.btn_map[key_char]
            original_color = btn.cget("fg_color")
            # Create a flash feedback
            flash_color = ("#C7D2FE", "#4338CA") # indigo accent shade
            btn.configure(fg_color=flash_color)
            self.after(80, lambda b=btn, col=original_color: b.configure(fg_color=col))

if __name__ == "__main__":
    app = CalculatorApp()
    app.mainloop()
