import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import webbrowser  

# 📌 Comprobar e instalar matplotlib automáticamente
try:
    import matplotlib.pyplot as plt
except ModuleNotFoundError:
    import os
    os.system("pip install matplotlib")
    import matplotlib.pyplot as plt  

# Crear la ventana principal centrada
root = tk.Tk()
root.title("Sistema Académico")
root.geometry("800x600")

# Centrar la ventana en la pantalla
ancho_pantalla = root.winfo_screenwidth()
alto_pantalla = root.winfo_screenheight()
x = (ancho_pantalla - 800) // 2
y = (alto_pantalla - 600) // 2
root.geometry(f"800x600+{x}+{y}")

root.configure(bg="#3b5998")

# Crear contenedor de pestañas
notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill="both", padx=10, pady=10)

# Crear marcos para cada pestaña
frame_registro = tk.Frame(notebook, bg="white", padx=20, pady=20)
frame_mensajes = tk.Frame(notebook, bg="white", padx=20, pady=20)
frame_calendario = tk.Frame(notebook, bg="white", padx=20, pady=20)
frame_rendimiento = tk.Frame(notebook, bg="white", padx=20, pady=20)
frame_material = tk.Frame(notebook, bg="white", padx=20, pady=20)
frame_foro = tk.Frame(notebook, bg="white", padx=20, pady=20)

# Agregar pestañas
notebook.add(frame_registro, text="Registro de Estudiantes")
notebook.add(frame_mensajes, text="Mensajes")
notebook.add(frame_calendario, text="Calendario")
notebook.add(frame_rendimiento, text="Rendimiento Académico")
notebook.add(frame_material, text="Material de Apoyo")
notebook.add(frame_foro, text="Foro Académico")

# 📌 Pestaña Registro
tk.Label(frame_registro, text="Registro de Estudiantes", font=("Arial", 14, "bold"), bg="white").pack(pady=5)

nombre_estudiante = tk.StringVar()
apellido_estudiante = tk.StringVar()
nota_estudiante = tk.StringVar()
estudiantes = []

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

tk.Label(frame_registro, text="Nombre:", bg="white").pack()
tk.Entry(frame_registro, textvariable=nombre_estudiante).pack()
tk.Label(frame_registro, text="Apellido:", bg="white").pack()
tk.Entry(frame_registro, textvariable=apellido_estudiante).pack()
tk.Label(frame_registro, text="Nota:", bg="white").pack()
tk.Entry(frame_registro, textvariable=nota_estudiante).pack()
tk.Button(frame_registro, text="Registrar Estudiante", command=registrar_estudiante, bg="#3b5998", fg="white").pack(pady=5)

# 📌 Pestaña Material de Apoyo
tk.Label(frame_material, text="Material de Apoyo", font=("Arial", 14, "bold"), bg="white").pack(pady=5)

# Lista de archivos subidos
lista_archivos = tk.Listbox(frame_material, width=60, height=5)
lista_archivos.pack(pady=5)

# Lista de enlaces agregados
lista_enlaces = tk.Listbox(frame_material, width=60, height=5)
lista_enlaces.pack(pady=5)

# Función para subir archivos
def subir_archivo():
    archivo = filedialog.askopenfilename(title="Selecciona un archivo", filetypes=[("Todos los archivos", "*.*")])
    if archivo:
        lista_archivos.insert(tk.END, archivo)  # Agrega el archivo a la lista
        messagebox.showinfo("Material de Apoyo", f"Archivo agregado:\n{archivo}")

# Función para agregar enlaces
def agregar_enlace():
    enlace = entrada_enlace.get().strip()
    if enlace and enlace.startswith("http"):
        lista_enlaces.insert(tk.END, enlace)  # Agrega el enlace a la lista
        entrada_enlace.set("")  # Limpia el campo
    else:
        messagebox.showwarning("Error", "Debes ingresar un enlace válido que comience con 'http'.")

# Función para abrir enlaces al hacer doble clic
def abrir_enlace(event):
    seleccion = lista_enlaces.curselection()
    if seleccion:
        enlace = lista_enlaces.get(seleccion[0])
        webbrowser.open(enlace)  # Abre el enlace en el navegador

# Campo de entrada para enlaces
entrada_enlace = tk.StringVar()
tk.Entry(frame_material, textvariable=entrada_enlace, width=50).pack(pady=5)

# Botones de acción
tk.Button(frame_material, text="Subir Archivo", command=subir_archivo, bg="#4682B4", fg="white").pack(pady=5)
tk.Button(frame_material, text="Agregar Enlace", command=agregar_enlace, bg="#32CD32", fg="white").pack(pady=5)

# Vincular la función para abrir enlaces
lista_enlaces.bind("<Double-Button-1>", abrir_enlace)


# 📌 Pestaña Mensajes Académicos
tk.Label(frame_mensajes, text="Mensajes", font=("Arial", 14, "bold"), bg="white").pack(pady=5)

mensajes_preexistentes = [
    "📢 Recordatorio: La entrega de proyectos finales es el 15 de junio.",
    "📝 Examen de Matemáticas programado para el 20 de junio.",
    "📅 Cierre de inscripciones el 30 de junio.",
]

lista_mensajes = tk.Listbox(frame_mensajes, width=60, height=10)
lista_mensajes.pack(pady=5)

for mensaje in mensajes_preexistentes:
    lista_mensajes.insert(tk.END, mensaje)

# 📌 Pestaña Calendario Académico
tk.Label(frame_calendario, text="Calendario Académico", font=("Arial", 14, "bold"), bg="white").pack(pady=5)

eventos_calendario = [
    "📅 10 de junio - Inicio de inscripciones.",
    "📅 15 de junio - Entrega de proyectos.",
    "📅 20 de junio - Examen de Matemáticas.",
]

lista_calendario = tk.Listbox(frame_calendario, width=60, height=10)
lista_calendario.pack(pady=5)

for evento in eventos_calendario:
    lista_calendario.insert(tk.END, evento)

# 📌 Pestaña Rendimiento Académico
tk.Label(frame_rendimiento, text="Rendimiento Académico", font=("Arial", 14, "bold"), bg="white").pack(pady=5)

tabla_estadisticas = tk.Label(frame_rendimiento, text="", bg="white", font=("Arial", 12))
tabla_estadisticas.pack(pady=5)

def calcular_estadisticas():
    if estudiantes:
        notas = [est["nota"] for est in estudiantes]
        promedio = sum(notas) / len(notas)
        nota_maxima = max(notas)
        nota_minima = min(notas)

        tabla_estadisticas.config(text=f"Promedio: {promedio:.2f}\nNota Máxima: {nota_maxima}\nNota Mínima: {nota_minima}")
    else:
        messagebox.showwarning("Vacío", "No hay estudiantes registrados.")

tk.Button(frame_rendimiento, text="Calcular Estadísticas", command=calcular_estadisticas, bg="#FF6347", fg="white").pack(pady=5)

# 📌 Pestaña Mensajes Académicos
tk.Label(frame_mensajes, text="Mensajes Académicos", font=("Arial", 14, "bold"), bg="white").pack(pady=5)

mensajes_preexistentes = [
    "📢 Recordatorio: La entrega de proyectos finales es el 15 de junio.",
    "📝 Examen de Matemáticas programado para el 20 de junio.",
    "📅 Cierre de inscripciones el 30 de junio.",
]

lista_mensajes = tk.Listbox(frame_mensajes, width=60, height=10)
lista_mensajes.pack(pady=5)

for mensaje in mensajes_preexistentes:
    lista_mensajes.insert(tk.END, mensaje)

# 📌 Pestaña Foro Académico
tk.Label(frame_foro, text="Foro Académico", font=("Arial", 14, "bold"), bg="white").pack(pady=5)

mensajes_preexistentes_foro = [
    "Carlos: ¿Cuál creen que sea el mejor lenguaje para backend?",
    "Ana: Yo uso Python, pero algunos prefieren Node.js.",
    "Luis: Depende del proyecto, ¿han probado Django?",
]

mensajes_foro = tk.Listbox(frame_foro, width=60, height=10)
mensajes_foro.pack(pady=5)

for mensaje in mensajes_preexistentes_foro:
    mensajes_foro.insert(tk.END, mensaje)

entrada_mensaje_foro = tk.StringVar()
tk.Entry(frame_foro, textvariable=entrada_mensaje_foro, width=50).pack(pady=5)

def publicar_mensaje():
    mensaje = entrada_mensaje_foro.get().strip()
    if mensaje:
        mensajes_foro.insert(tk.END, f"Ricardo: {mensaje}")
        entrada_mensaje_foro.set("")
    else:
        messagebox.showwarning("Error", "No puedes enviar un mensaje vacío.")

tk.Button(frame_foro, text="Publicar Mensaje", command=publicar_mensaje, bg="#32CD32", fg="white").pack(pady=5)


# Iniciar la interfaz gráfica
root.mainloop()
