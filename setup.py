from cx_Freeze import setup, Executable  

setup(
    name="Sistema Académico",
    version="1.0",
    description="Aplicación de gestión académica",
    executables=[Executable("Tarea 3.py", base="Win32GUI")]
)
