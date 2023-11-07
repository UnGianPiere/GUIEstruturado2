import tkinter as tk
from tkinter import ttk
from src.Data.conexion_db import Conexion
from src.Clases.ClaseDetalleMensualTrabajador import SQLDetalleMensualTrabajador
from src.Clases.ClaseEmpleado import SQLEmpleado
def abrir_ventana2():
    ventanaGE=tk.Toplevel()
    ventanaGE.title('Buscar Empleado')
    ventanaGE.geometry("600x400")

    ventanaGE.label = tk.Label(ventanaGE, text="Nombre del Empleado:")
    ventanaGE.label.grid(row=0, column=0, padx=10, pady=10)
    ventanaGE.entry = tk.Entry(ventanaGE)
    ventanaGE.entry.grid(row=0, column=1, padx=10, pady=10, columnspan=2)
    ventanaGE.botonBuscar = tk.Button(ventanaGE, text='Buscar Empleado',command=lambda :BuscarEmpleado(ventanaGE))
    ventanaGE.botonBuscar.config(bg='Green', fg='White')
    ventanaGE.botonBuscar.grid(row=1, column=1, padx=10, pady=10)

    ventanaGE.tablaB = ttk.Treeview(ventanaGE, column=('Nombre', 'Cargo'))
    ventanaGE.tablaB.grid(row=2, column=0, columnspan=3)
    ventanaGE.tablaB.heading('#0', text='ID')
    ventanaGE.tablaB.heading('#1', text='Nombre')
    ventanaGE.tablaB.heading('#2', text='Cargo')

    ventanaGE.botonSeleccionar = tk.Button(ventanaGE, text='Mostrar Historial',command=lambda :Seleccion(ventanaGE))
    ventanaGE.botonSeleccionar.config(bg='grey', fg='White')
    ventanaGE.botonSeleccionar.grid(row=3, column=1, padx=10, pady=10)

    ventanaGE.botonSeleccionar2 = tk.Button(ventanaGE, text='Gestionar asistencia ')
    ventanaGE.botonSeleccionar2.config(bg='grey', fg='White')
    ventanaGE.botonSeleccionar2.grid(row=3, column=2, padx=10, pady=10)

def BuscarEmpleado(ventanaGE):
    ventanaGE.tablaB.delete(*ventanaGE.tablaB.get_children())
    nombre=ventanaGE.entry.get()
    empleado=SQLEmpleado(None,nombre)
    ventanaGE.lista=empleado.LeerEmpleado()
    for i in ventanaGE.lista:
        ventanaGE.tablaB.insert('', 0, text=i[0], values=(i[1], i[3]))

def Seleccion(ventanaGE):
    selected_item = ventanaGE.tablaB.selection()
    if selected_item:
        selected_row = ventanaGE.tablaB.item(selected_item)
        ventanaGE.id = selected_row['text']  # ID en la columna 0
        ventanaGE.nombre = selected_row['values'][0]  # Nombre en la columna 1
    conexion = Conexion()
    cursor = conexion.cursor()
    cursor.execute(f"select * from tblBoletaPago Where IDEmpleado LIKE {ventanaGE.id}")
    lista=cursor.fetchall()
    lista.reverse()
    FrameHistorial=tk.Toplevel()
    FrameHistorial.title('Historial de pagos')
    FrameHistorial.geometry("600x400")
    FrameHistorial.label = tk.Label(FrameHistorial, text=f"Nombre del Empleado: {ventanaGE.nombre}")
    FrameHistorial.label.grid(row=0, column=0, padx=10, pady=10)

    tablaBOL= ttk.Treeview(FrameHistorial, column=('Fecha', 'Monto'))
    tablaBOL.grid(row=2, column=0, columnspan=3)
    tablaBOL.heading('#0', text='ID de Boleta')
    tablaBOL.heading('#1', text='Fecha de pago')
    tablaBOL.heading('#2', text='Monto Total')
    for i in lista:
            tablaBOL.insert('', 0, text=i[0], values=(i[4], i[1]))

    cursor.close()
    conexion.close()
