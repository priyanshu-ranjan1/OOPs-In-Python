#i jjsut added a gui using ai in my code 

import math
import customtkinter as ctk

# Set appearance
ctk.set_appearance_mode("System")  # Options: "Dark", "Light", "System"
ctk.set_default_color_theme("blue")  # You can explore other themes

# Define Calculator
class Calculator:
    @staticmethod
    def square(n):
        return n**2

    @staticmethod
    def cube(n):
        return n**3

    @staticmethod
    def square_root(n):
        return math.sqrt(n)

# GUI App
class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Gradient Calculator 🌈")
        self.geometry("400x380")
        self.configure(fg_color="#1E1E2E")  # Deep background

        # Gradient-like label (imitated with font color and styling)
        self.header = ctk.CTkLabel(self, text="Gradient Calculator", text_color="#FFD700", font=("Helvetica", 24, "bold"))
        self.header.pack(pady=20)

        self.entry = ctk.CTkEntry(self, placeholder_text="Enter a number", width=250)
        self.entry.pack(pady=10)

        self.option = ctk.CTkOptionMenu(self, values=["Square", "Cube", "Square Root"])
        self.option.pack(pady=10)

        self.result_label = ctk.CTkLabel(self, text="Result: ", font=("Helvetica", 16))
        self.result_label.pack(pady=10)

        self.button = ctk.CTkButton(self, text="Calculate", command=self.calculate)
        self.button.pack(pady=20)

    def calculate(self):
        try:
            value = float(self.entry.get())
            choice = self.option.get().lower()

            if choice == "square":
                result = Calculator.square(value)
            elif choice == "cube":
                result = Calculator.cube(value)
            elif choice == "square root":
                result = Calculator.square_root(value)
            else:
                result = "Invalid"

            self.result_label.configure(text=f"Result: {result:.2f}")
        except ValueError:
            self.result_label.configure(text="Please enter a valid number.")

# Run App
if __name__ == "__main__":
    app = App()
    app.mainloop()
