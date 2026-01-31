"""
==============================================================================
DASHBOARD - PROGRAMACIÓN ORIENTADA A OBJETOS (2525)
==============================================================================

Archivo: Dashboard.py
Descripción: Dashboard interactivo para gestionar los ejemplos y tareas
             del curso de Programación Orientada a Objetos.

Estudiante: YORMAN ALQUIMEDES HURTADO VILLEGAS
Carrera: TECNOLOGÍAS DE LA INFORMACIÓN
Paralelo: PARALELO A
Email: ya.hurtadov@uea.edu.ec
GitHub: jorman92

Fecha de Creación: Enero 2026

ADAPTACIONES REALIZADAS:
1. Banner personalizado con información del estudiante
2. Colores en la interfaz de consola
3. Fecha y hora en el menú principal
4. Opción para ver información del estudiante
5. Contador de scripts ejecutados
6. Historial de ejecuciones guardado en archivo
7. Sección "Acerca de" con descripción del proyecto
8. Documentación completa con comentarios descriptivos
==============================================================================
"""
import os
import subprocess
from datetime import datetime

# Habilitar colores en Windows
os.system('color')

# ===================== INFORMACIÓN DEL ESTUDIANTE =====================
ESTUDIANTE = {
    "nombre": "YORMAN ALQUIMEDES HURTADO VILLEGAS",
    "carrera": "TECNOLOGÍAS DE LA INFORMACIÓN",
    "paralelo": "PARALELO A",
    "email": "ya.hurtadov@uea.edu.ec",
    "github": "jorman92"
}

# ===================== COLORES PARA CONSOLA =====================
class Color:
    VERDE = '\033[92m'
    ROJO = '\033[91m'
    AMARILLO = '\033[93m'
    CYAN = '\033[96m'
    AZUL = '\033[94m'
    MAGENTA = '\033[95m'
    RESET = '\033[0m'
    NEGRITA = '\033[1m'

# ===================== VARIABLES GLOBALES =====================
contador_ejecuciones = 0

# ===================== FUNCIONES DE INTERFAZ =====================
def mostrar_banner():
    """
    Muestra el banner principal del dashboard con la información del estudiante.
    Incluye decoración visual y colores para mejor presentación.
    """
    print(f"""
{Color.CYAN}╔══════════════════════════════════════════════════════════════╗
║{Color.NEGRITA}        DASHBOARD - PROGRAMACIÓN ORIENTADA A OBJETOS          {Color.CYAN}║
╠══════════════════════════════════════════════════════════════╣
║{Color.RESET}{Color.AMARILLO}  Estudiante: {ESTUDIANTE['nombre']:<40}{Color.CYAN}  ║
║{Color.RESET}{Color.AMARILLO}  Email: {ESTUDIANTE['email']:<45}{Color.CYAN}  ║
║{Color.RESET}{Color.AMARILLO}  GitHub: {ESTUDIANTE['github']:<44}{Color.CYAN}  ║
╚══════════════════════════════════════════════════════════════╝{Color.RESET}
""")

def mostrar_fecha_hora():
    """Muestra la fecha y hora actual del sistema."""
    ahora = datetime.now()
    print(f"{Color.VERDE} Fecha: {ahora.strftime('%d/%m/%Y')}  Hora: {ahora.strftime('%H:%M:%S')}{Color.RESET}")

def mostrar_linea():
    """Muestra una línea separadora decorativa."""
    print(f"{Color.CYAN}{'─' * 62}{Color.RESET}")

# ===================== FUNCIONES DE INFORMACIÓN =====================
def mostrar_info_estudiante():
    """
    Muestra la información completa del estudiante.
    Lee los datos del diccionario ESTUDIANTE y los presenta de forma organizada.
    """
    print(f"\n{Color.CYAN}╔══════════════════════════════════════════════════════════════╗")
    print(f"║{Color.NEGRITA}              INFORMACIÓN DEL ESTUDIANTE                   {Color.CYAN}║")
    print(f"╚══════════════════════════════════════════════════════════════╝{Color.RESET}\n")
    
    for clave, valor in ESTUDIANTE.items():
        print(f"  {Color.AMARILLO}{clave.upper():12}{Color.RESET}: {valor}")
    
    print(f"\n  {Color.VERDE}Scripts ejecutados en esta sesión: {contador_ejecuciones}{Color.RESET}")
    mostrar_linea()
    input(f"\n{Color.CYAN}Presiona Enter para continuar...{Color.RESET}")

def mostrar_acerca_de():
    """
    Muestra información sobre el proyecto y el curso.
    Incluye descripción del dashboard y sus funcionalidades.
    """
    print(f"""
{Color.MAGENTA}╔══════════════════════════════════════════════════════════════╗
║                      ACERCA DE ESTE PROYECTO                 ║
╚══════════════════════════════════════════════════════════════╝{Color.RESET}

  {Color.NEGRITA}Curso:{Color.RESET} Programación Orientada a Objetos (2525)
  {Color.NEGRITA}Universidad:{Color.RESET} Universidad Estatal Amazónica
  
  {Color.NEGRITA}Descripción:{Color.RESET}
  Este dashboard permite navegar por los ejemplos de código
  del curso de POO, visualizar el código fuente y ejecutar
  los scripts de manera interactiva.
  
  {Color.NEGRITA}Funcionalidades:{Color.RESET}
  ✓ Navegación por unidades y temas
  ✓ Visualización de código con formato
  ✓ Ejecución de scripts Python
  ✓ Historial de ejecuciones
  ✓ Interfaz con colores
""")
    mostrar_linea()
    input(f"\n{Color.CYAN}Presiona Enter para continuar...{Color.RESET}")

# ===================== FUNCIONES DE CÓDIGO =====================
def mostrar_codigo(ruta_script):
    """
    Muestra el contenido de un archivo Python con formato.
    
    Args:
        ruta_script: Ruta al archivo Python a mostrar
        
    Returns:
        str: Contenido del archivo o None si hay error
    """
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r', encoding='utf-8') as archivo:
            codigo = archivo.read()
            print(f"\n{Color.VERDE}{'─' * 62}{Color.RESET}")
            print(f"{Color.NEGRITA}{Color.AMARILLO}📄 Archivo: {os.path.basename(ruta_script)}{Color.RESET}")
            print(f"{Color.VERDE}{'─' * 62}{Color.RESET}\n")
            
            # Mostrar código con números de línea
            lineas = codigo.split('\n')
            for i, linea in enumerate(lineas, 1):
                print(f"{Color.AZUL}{i:4d}{Color.RESET} │ {linea}")
            
            print(f"\n{Color.VERDE}{'─' * 62}{Color.RESET}")
            return codigo
    except FileNotFoundError:
        print(f"{Color.ROJO} Error: El archivo no se encontró.{Color.RESET}")
        return None
    except Exception as e:
        print(f"{Color.ROJO} Error al leer el archivo: {e}{Color.RESET}")
        return None

def ejecutar_codigo(ruta_script):
    """
    Ejecuta un script Python en una nueva ventana de terminal.
    Registra la ejecución en el historial y actualiza el contador.
    
    Args:
        ruta_script: Ruta al script Python a ejecutar
    """
    global contador_ejecuciones
    contador_ejecuciones += 1
    
    # Guardar en historial
    guardar_historial(ruta_script)
    
    print(f"\n{Color.VERDE}▶ Ejecutando script... [Ejecución #{contador_ejecuciones}]{Color.RESET}\n")
    
    try:
        if os.name == 'nt':  # Windows
            subprocess.Popen(['cmd', '/k', 'python', ruta_script])
        else:  # Linux/Mac
            subprocess.Popen(['xterm', '-hold', '-e', 'python3', ruta_script])
    except Exception as e:
        print(f"{Color.ROJO} Error al ejecutar: {e}{Color.RESET}")

def guardar_historial(ruta_script):
    """
    Guarda un registro de la ejecución en el archivo historial.txt
    
    Args:
        ruta_script: Ruta del script que se ejecutó
    """
    try:
        ruta_historial = os.path.join(os.path.dirname(__file__), 'historial.txt')
        with open(ruta_historial, 'a', encoding='utf-8') as f:
            fecha = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            nombre_script = os.path.basename(ruta_script)
            f.write(f"{fecha} - {nombre_script}\n")
    except Exception as e:
        print(f"{Color.AMARILLO}⚠ No se pudo guardar historial: {e}{Color.RESET}")

# ===================== MENÚS DE NAVEGACIÓN =====================
def mostrar_menu():
    """
    Menú principal del dashboard.
    Permite acceder a las unidades del curso y otras funcionalidades.
    """
    ruta_base = os.path.dirname(__file__)
    
    # Unidades disponibles en el curso
    unidades = {
        '1': 'UNIDAD 1',
        '2': 'UNIDAD 2'
    }
    
    while True:
        # Limpiar pantalla (opcional)
        # os.system('cls' if os.name == 'nt' else 'clear')
        
        mostrar_banner()
        mostrar_fecha_hora()
        mostrar_linea()
        
        print(f"\n{Color.NEGRITA}MENÚ PRINCIPAL{Color.RESET}\n")
        
        # Mostrar unidades
        print(f"{Color.AMARILLO}Unidades del Curso:{Color.RESET}")
        for key in unidades:
            print(f"  {Color.CYAN}{key}{Color.RESET} - {unidades[key]}")
        
        # Mostrar opciones adicionales
        print(f"\n{Color.AMARILLO}Otras Opciones:{Color.RESET}")
        print(f"  {Color.VERDE}I{Color.RESET} - Mi Información")
        print(f"  {Color.VERDE}A{Color.RESET} - Acerca de")
        print(f"  {Color.ROJO}0{Color.RESET} - Salir")
        
        mostrar_linea()
        
        eleccion = input(f"\n{Color.CYAN}Elige una opción: {Color.RESET}").upper()
        
        if eleccion == '0':
            print(f"\n{Color.VERDE}¡Hasta luego, {ESTUDIANTE['nombre'].split()[0]}! 👋{Color.RESET}")
            print(f"{Color.AMARILLO}Scripts ejecutados en esta sesión: {contador_ejecuciones}{Color.RESET}\n")
            break
        elif eleccion == 'I':
            mostrar_info_estudiante()
        elif eleccion == 'A':
            mostrar_acerca_de()
        elif eleccion in unidades:
            mostrar_sub_menu(os.path.join(ruta_base, unidades[eleccion]))
        else:
            print(f"\n{Color.ROJO}Opción no válida. Intenta de nuevo.{Color.RESET}")
            input(f"{Color.CYAN}Presiona Enter para continuar...{Color.RESET}")

def mostrar_sub_menu(ruta_unidad):
    """
    Submenú que muestra las subcarpetas de una unidad.
    
    Args:
        ruta_unidad: Ruta a la carpeta de la unidad seleccionada
    """
    try:
        sub_carpetas = sorted([f.name for f in os.scandir(ruta_unidad) if f.is_dir()])
    except FileNotFoundError:
        print(f"{Color.ROJO} No se encontró la carpeta de la unidad.{Color.RESET}")
        input(f"{Color.CYAN}Presiona Enter para continuar...{Color.RESET}")
        return
    
    while True:
        nombre_unidad = os.path.basename(ruta_unidad)
        print(f"\n{Color.CYAN}{'═' * 62}{Color.RESET}")
        print(f"{Color.NEGRITA} {nombre_unidad}{Color.RESET}")
        print(f"{Color.CYAN}{'═' * 62}{Color.RESET}")
        
        print(f"\n{Color.AMARILLO}Temas disponibles:{Color.RESET}")
        for i, carpeta in enumerate(sub_carpetas, start=1):
            print(f"  {Color.CYAN}{i}{Color.RESET} - {carpeta}")
        
        print(f"\n  {Color.ROJO}0{Color.RESET} - Volver al menú principal")
        mostrar_linea()
        
        eleccion = input(f"\n{Color.CYAN}Elige un tema: {Color.RESET}")
        
        if eleccion == '0':
            break
        else:
            try:
                eleccion_idx = int(eleccion) - 1
                if 0 <= eleccion_idx < len(sub_carpetas):
                    mostrar_scripts(os.path.join(ruta_unidad, sub_carpetas[eleccion_idx]))
                else:
                    print(f"\n{Color.ROJO} Opción no válida.{Color.RESET}")
            except ValueError:
                print(f"\n{Color.ROJO} Por favor ingresa un número.{Color.RESET}")

def mostrar_scripts(ruta_sub_carpeta):
    """
    Muestra los scripts Python disponibles en una subcarpeta.
    
    Args:
        ruta_sub_carpeta: Ruta a la subcarpeta con los scripts
    """
    try:
        scripts = sorted([f.name for f in os.scandir(ruta_sub_carpeta) 
                         if f.is_file() and f.name.endswith('.py')])
    except FileNotFoundError:
        print(f"{Color.ROJO} No se encontró la carpeta.{Color.RESET}")
        return
    
    while True:
        nombre_tema = os.path.basename(ruta_sub_carpeta)
        print(f"\n{Color.VERDE}{'═' * 62}{Color.RESET}")
        print(f"{Color.NEGRITA} {nombre_tema}{Color.RESET}")
        print(f"{Color.VERDE}{'═' * 62}{Color.RESET}")
        
        print(f"\n{Color.AMARILLO}Scripts disponibles:{Color.RESET}")
        for i, script in enumerate(scripts, start=1):
            print(f"  {Color.CYAN}{i}{Color.RESET} - {script}")
        
        print(f"\n  {Color.ROJO}0{Color.RESET} - Volver")
        print(f"  {Color.ROJO}9{Color.RESET} - Menú principal")
        mostrar_linea()
        
        eleccion = input(f"\n{Color.CYAN}Elige un script: {Color.RESET}")
        
        if eleccion == '0':
            break
        elif eleccion == '9':
            return
        else:
            try:
                eleccion_idx = int(eleccion) - 1
                if 0 <= eleccion_idx < len(scripts):
                    ruta_script = os.path.join(ruta_sub_carpeta, scripts[eleccion_idx])
                    codigo = mostrar_codigo(ruta_script)
                    
                    if codigo:
                        print(f"\n{Color.AMARILLO}¿Qué deseas hacer?{Color.RESET}")
                        print(f"  {Color.VERDE}1{Color.RESET} - Ejecutar script")
                        print(f"  {Color.ROJO}0{Color.RESET} - Volver")
                        
                        ejecutar = input(f"\n{Color.CYAN}Opción: {Color.RESET}")
                        
                        if ejecutar == '1':
                            ejecutar_codigo(ruta_script)
                    
                    input(f"\n{Color.CYAN}Presiona Enter para continuar...{Color.RESET}")
                else:
                    print(f"\n{Color.ROJO} Opción no válida.{Color.RESET}")
            except ValueError:
                print(f"\n{Color.ROJO} Por favor ingresa un número.{Color.RESET}")

# ===================== PUNTO DE ENTRADA =====================
if __name__ == "__main__":
    try:
        mostrar_menu()
    except KeyboardInterrupt:
        print(f"\n\n{Color.AMARILLO}Programa interrumpido.{Color.RESET}")
        print(f"{Color.VERDE}¡Hasta pronto! {Color.RESET}\n")

