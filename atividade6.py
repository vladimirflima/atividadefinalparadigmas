import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tarefas")
        
        # Elementos da interface gráfica
        self.label = tk.Label(root, text="Digite a tarefa:")
        self.label.pack(pady=5)
        
        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack(pady=5)
        
        self.add_button = tk.Button(root, text="Adicionar Tarefa", command=self.add_task)
        self.add_button.pack(pady=5)
        
        self.tasks_listbox = tk.Listbox(root, width=50, height=10)
        self.tasks_listbox.pack(pady=5)
        
        self.remove_button = tk.Button(root, text="Remover Tarefa Selecionada", command=self.remove_task)
        self.remove_button.pack(pady=5)
        
        # Lista de tarefas
        self.tasks = []
        
    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_tasks_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Aviso", "Digite uma tarefa para adicionar.")
    
    def remove_task(self):
        try:
            selected_index = self.tasks_listbox.curselection()[0]
            del self.tasks[selected_index]
            self.update_tasks_listbox()
        except IndexError:
            messagebox.showwarning("Aviso", "Selecione uma tarefa para remover.")
    
    def update_tasks_listbox(self):
        self.tasks_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.tasks_listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
