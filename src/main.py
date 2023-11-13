import tkinter as tk
from ventanas import ViewAgregarEmpleado, ViewGestionarEmpleado,ViewActualizarBonificacion
from ttkthemes import ThemedTk
def abrir_ventana(ventana):
    ventana()

root = tk.Tk()
root.title("Menú Principal")

root.configure(bg='#A1b0cb')
root.geometry('430x550')
frame = tk.Frame(root)
frame.pack()
frame.configure(bg='#A1b0cb')
img_crear = tk.PhotoImage(file="../Recursos/add.png")
img_gestionar = tk.PhotoImage(file="../Recursos/gestionarE.png")
img_gestionarB = tk.PhotoImage(file="../Recursos/bonificacion.png")



btn_AgregarEmpleado = tk.Button(frame, image=img_crear, command=lambda: abrir_ventana(ViewAgregarEmpleado.abrir_ventana1))
btn_AgregarEmpleado.image = img_crear
btn_AgregarEmpleado.config( fg='white', bg='grey', activebackground='green')
btn_AgregarEmpleado.grid(row=1, column=3, padx=10, pady=10)

btn_GestionarEmpleado = tk.Button(frame, image=img_gestionar, command=lambda: abrir_ventana(ViewGestionarEmpleado.abrir_ventana2))
btn_GestionarEmpleado.image = img_gestionar
btn_GestionarEmpleado.config( bg='grey', activebackground='green')
btn_GestionarEmpleado.grid(row=2, column=3, padx=10, pady=10)

btn_ActualizarBonificacion = tk.Button(frame, image=img_gestionarB,command=lambda: abrir_ventana(ViewActualizarBonificacion.abrir_ventana3))
btn_ActualizarBonificacion.image = img_gestionarB
btn_ActualizarBonificacion.config( fg='white', bg='grey', activebackground='green')
btn_ActualizarBonificacion.grid(row=3, column=3, padx=10, pady=10)

btn_Salir= tk.Button(frame, text='Salir',command=root.destroy)
btn_Salir.config(font=('Times New Roman', 10, 'bold'), fg='#D01818', bg='#Ce8d8d', activebackground='green')
btn_Salir.grid(row=4, column=3, padx=10, pady=(50, 10), sticky="ew")


root.mainloop()