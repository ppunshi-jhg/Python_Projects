import customtkinter as ctk

class TaxCalculator:
    def __init__(self):
        # Initialize the main window, we have used ctk module and call CTK() class to create a window. and assign to self.window which is a object of CTK class. and then call title and all other methods on it.
        
        #We havent passed any arguments to the intializer, so we can use default values for the window title and size.
        self.window = ctk.CTk()
        self.window.title("Tax Calculator")
        self.window.geometry("400x300")
        self.window.resizable(False, False)
        
        #Widgets Padding
        
        self.padding: dict = {
            "padx": 20,
            "pady": 10
        }
        
        # Create input fields for income and tax rate
        
        self.income_label = ctk.CTkLabel(self.window, text = "Income:")
        self.income_label.grid(row = 0, column =0 , **self.padding)
        self.income_entry = ctk.CTkEntry(self.window)
        self.income_entry.grid(row = 0, column =1, **self.padding)
        
        #Tax rate input
        self.tax_rate_label = ctk.CTkLabel(self.window, text = "Percentage Tax Rate:")
        self.tax_rate_label.grid(row = 1, column = 0, **self.padding)
        self.tax_rate_entry = ctk.CTkEntry(self.window)
        self.tax_rate_entry.grid(row = 1, column = 1, **self.padding)
        
        #Result Label
        
        self.result_label = ctk.CTkLabel(self.window, text = "Tax Amount:")
        self.result_label.grid(row = 2, column = 0, **self.padding)
        self.result_entry = ctk.CTkEntry(self.window)
        self.result_entry.insert(0, "0")  # Initialize with 0, the first zero represents the index where the text will be inserted, and the second argument the text to be inserted.
        self.result_entry.grid(row = 2, column = 1, **self.padding)
        
        # Create a button to calculate tax
        self.calculate_button = ctk.CTkButton(self.window, text= "Calculate Tax", command = self.calculate_tax)
        self.calculate_button.grid(row = 3, column= 1, **self.padding)
        
    def update_result(self, text: str):
        # Update the result entry with the calculated tax amount
        self.result_entry.delete(0, ctk.END)
        self.result_entry.insert(0, text)
    
    def calculate_tax(self):
        # Calculate the tax based on income and tax rate
        try:
            income = float(self.income_entry.get())
            tax_rate = float(self.tax_rate_entry.get())
            tax_amount = income * (tax_rate / 100)
            self.update_result(f"{tax_amount:.2f}")
        except ValueError:
            self.update_result("Invalid input")
        
    def run(self):
        # Start the main loop of the application
        self.window.mainloop()
        
if __name__ == "__main__":
    tax_calculator = TaxCalculator()
    tax_calculator.run()