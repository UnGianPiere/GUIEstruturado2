import tkinter as tk
from ventanas import ViewAgregarEmpleado, ViewGestionarEmpleado, ventana3,ventana4
def abrir_ventana(ventana):
    ventana()

root = tk.Tk()
root.title("Menú Principal")
root.geometry("370x600")
root.configure(bg='#A1b0cb')


img_crear = tk.PhotoImage(file="../Recursos/add.png")
img_gestionar = tk.PhotoImage(file="../Recursos/gestionarE.png")
img_gestionarB = tk.PhotoImage(file="../Recursos/bonificacion.png")

btn_AgregarEmpleado = tk.Button(root, image=img_crear, command=lambda: abrir_ventana(ViewAgregarEmpleado.abrir_ventana1))
btn_AgregarEmpleado.image = img_crear
btn_AgregarEmpleado.config( fg='white', bg='grey', activebackground='green')
btn_AgregarEmpleado.grid(row=0, column=3, padx=10, pady=10, sticky="ew")

btn_GestionarEmpleado = tk.Button(root, image=img_gestionar, command=lambda: abrir_ventana(ViewGestionarEmpleado.abrir_ventana2))
btn_GestionarEmpleado.image = img_gestionar
btn_GestionarEmpleado.config( bg='grey', activebackground='green')
btn_GestionarEmpleado.grid(row=1, column=3, padx=10, pady=10, sticky="ew")

btn_ActualizarBonificacion = tk.Button(root, image=img_gestionarB,command=lambda: abrir_ventana(ventana3.abrir_ventana3))
btn_ActualizarBonificacion.image = img_gestionarB
btn_ActualizarBonificacion.config( fg='white', bg='grey', activebackground='green')
btn_ActualizarBonificacion.grid(row=2, column=3, padx=10, pady=10, sticky="ew")

btn_Justificar = tk.Button(root, text='Justificar',command=lambda: abrir_ventana(ventana4.abrir_ventana4))
btn_Justificar.config(font=('Times New Roman', 10, 'bold'), fg='#D01818', bg='#Ce8d8d', activebackground='green')
btn_Justificar.grid(row=3, column=3, padx=10, pady=(50, 10), sticky="ew")


root.mainloop()