import tkinter as tk
from tkinter import messagebox

class BMICalculator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Calculadora de IMC")

        self.setup_ui()
        
        self.root.mainloop()
    
    def setup_ui(self):
        tk.Label(self.root, text="Altura (m):").grid(row=0, column=0, padx=10, pady=10)
        self.height_entry = tk.Entry(self.root)
        self.height_entry.grid(row=0, column=1, padx=10, pady=10)
        
        tk.Label(self.root, text="Peso (kg):").grid(row=1, column=0, padx=10, pady=10)
        self.weight_entry = tk.Entry(self.root)
        self.weight_entry.grid(row=1, column=1, padx=10, pady=10)
        
        calculate_button = tk.Button(self.root, text="Calcular IMC", command=self.calculate_bmi)
        calculate_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
        
        self.result_label = tk.Label(self.root, text="IMC: ", font=("Arial", 14))
        self.result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
    
    def calculate_bmi(self):
        try:
            height = float(self.height_entry.get())
            weight = float(self.weight_entry.get())
        
            bmi = weight / (height ** 2)
            
            self.result_label.config(text=f"IMC: {bmi:.2f}")
            
            self.show_bmi_category(bmi)
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores válidos para altura e peso.")
    
    def show_bmi_category(self, bmi):
        if bmi < 18.5:
            category = "Abaixo do peso"
        elif 18.5 <= bmi < 24.9:
            category = "Peso normal"
        elif 25 <= bmi < 29.9:
            category = "Sobrepeso"
        else:
            category = "Obesidade"
        
        messagebox.showinfo("Categoria do IMC", f"Seu IMC é {bmi:.2f}. Categoria: {category}")

if __name__ == "__main__":
    BMICalculator()
