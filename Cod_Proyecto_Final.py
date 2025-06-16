import tkinter as tk
from tkinter import messagebox, ttk

# Crear la ventana principal con fondo tipo Facebook
root = tk.Tk()
root.title("Sistema Académico")
root.geometry("600x550")
root.configure(bg="#3b5998")

# Logo con la "G"
logo = tk.Label(root, text="G", font=("Arial", 50, "bold"), fg="white", bg="#3b5998")
logo.pack(pady=10)

# Marco para organizar los elementos principales
frame = tk.Frame(root, bg="white", padx=20, pady=20)
frame.pack()

# Variables de estudiante
nombre_estudiante = tk.StringVar()
apellido_estudiante = tk.StringVar()
nota_estudiante = tk.StringVar()

# Lista de estudiantes
estudiantes = []

# Función para registrar estudiante con nombre, apellido y nota
def registrar_estudiante():
    nombre = nombre_estudiante.get().strip()
    apellido = apellido_estudiante.get().strip()
    nota = nota_estudiante.get().strip()
    
    if nombre and apellido and nota.isdigit():
        estudiantes.append({"nombre": nombre, "apellido": apellido, "nota": int(nota)})
        messagebox.showinfo("Registro", f"{nombre} {apellido} registrado con nota {nota}.")
        nombre_estudiante.set("")
        apellido_estudiante.set("")
        nota_estudiante.set("")
    else:
        messagebox.showwarning("Error", "Ingresa datos válidos.")

# Función para mostrar estudiantes en tabla
def ver_registro():
    if estudiantes:
        ventana_registro = tk.Toplevel(root)
        ventana_registro.title("Registro de Notas de la Institución ------")
        ventana_registro.geometry("500x300")

        tk.Label(ventana_registro, text="Registro de Notas de la Institución ------", font=("Arial", 14, "bold")).pack(pady=10)

        tabla = ttk.Treeview(ventana_registro, columns=("Nombre", "Apellido", "Nota"), show="headings")
        tabla.heading("Nombre", text="Nombre")
        tabla.heading("Apellido", text="Apellido")
        tabla.heading("Nota", text="Nota")

        for estudiante in estudiantes:
            tabla.insert("", tk.END, values=(estudiante["nombre"], estudiante["apellido"], estudiante["nota"]))

        tabla.pack(expand=True, fill="both")
    else:
        messagebox.showwarning("Vacío", "No hay estudiantes registrados.")

# Función para mensajes y comunicaciones
def enviar_mensaje():
    messagebox.showinfo("Mensajes", "Aquí se pueden enviar avisos académicos.")

# Función para calendario académico
def ver_calendario():
    messagebox.showinfo("Calendario", "Visualización de eventos académicos.")

# Función para rendimiento académico (gráficos)
def ver_rendimiento():
    messagebox.showinfo("Rendimiento", "Aquí se mostrarán estadísticas de notas.")

# Función para material de apoyo
def subir_material():
    messagebox.showinfo("Material de Apoyo", "Aquí se pueden subir documentos y recursos.")

# Función para foro de discusión
def abrir_foro():
    messagebox.showinfo("Foro de Discusión", "Aquí se pueden intercambiar ideas y dudas.")

# Interfaz gráfica mejorada
tk.Label(frame, text="Registro de Estudiantes", font=("Arial", 14, "bold"), bg="white").pack(pady=5)

tk.Label(frame, text="Nombre:", bg="white").pack()
tk.Entry(frame, textvariable=nombre_estudiante).pack()

tk.Label(frame, text="Apellido:", bg="white").pack()
tk.Entry(frame, textvariable=apellido_estudiante).pack()

tk.Label(frame, text="Nota:", bg="white").pack()
tk.Entry(frame, textvariable=nota_estudiante).pack()

tk.Button(frame, text="Registrar Estudiante", command=registrar_estudiante, bg="#3b5998", fg="white").pack(pady=5)
tk.Button(frame, text="Ver Registro de Notas", command=ver_registro, bg="#008CBA", fg="white").pack(pady=5)

tk.Button(frame, text="Mensajes y Comunicaciones", command=enviar_mensaje, bg="#FFA500").pack(pady=5)
tk.Button(frame, text="Calendario Académico", command=ver_calendario, bg="#FF6347").pack(pady=5)
tk.Button(frame, text="Gráficos de Rendimiento", command=ver_rendimiento, bg="#9370DB").pack(pady=5)
tk.Button(frame, text="Material de Apoyo", command=subir_material, bg="#4682B4").pack(pady=5)
tk.Button(frame, text="Foro de Discusión", command=abrir_foro, bg="#32CD32").pack(pady=5)

# Iniciar la interfaz gráfica
root.mainloop()
