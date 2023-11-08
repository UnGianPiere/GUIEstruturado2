import tkinter as tk
from tkinter import ttk

def on_combobox_select(event):
    selected_value = combobox.get()
    print("Valor seleccionado:", selected_value)

root = tk.Tk()
root.title("Ejemplo de Combobox")

combobox = ttk.Combobox(root, values=["Opción 1", "Opción 2", "Opción 3"])
combobox.pack()

combobox.bind("<<ComboboxSelected>>", on_combobox_select)

root.mainloop()