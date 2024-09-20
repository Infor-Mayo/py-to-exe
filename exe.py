import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import subprocess
import threading
from PIL import Image

def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("Python files", "*.py")])
    entry_file.delete(0, tk.END)
    entry_file.insert(0, file_path)

def select_icon():
    icon_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif;*.ico")])
    entry_icon.delete(0, tk.END)
    entry_icon.insert(0, icon_path)

def create_executable():
    py_file = entry_file.get()
    icon_file = entry_icon.get()
    no_console = var_no_console.get()
    
    if not py_file:
        messagebox.showerror("Error", "Por favor selecciona un archivo .py")
        return
    
    if icon_file and not icon_file.endswith(".ico"):
        try:
            img = Image.open(icon_file)
            icon_file = icon_file.rsplit(".", 1)[0] + ".ico"
            img.save(icon_file, format="ICO")
        except Exception as e:
            messagebox.showerror("Error", f"Error al convertir la imagen a .ico: {e}")
            return
    
    command = f'pyinstaller --onefile "{py_file}"'
    if icon_file:
        command += f' --icon="{icon_file}"'
    if no_console:
        command += ' --noconsole'
    
    progress_bar.start()
    threading.Thread(target=run_command, args=(command,)).start()

def run_command(command):
    try:
        subprocess.run(command, check=True, shell=True)
        progress_bar.stop()
        messagebox.showinfo("Éxito", "El ejecutable .exe ha sido creado exitosamente")
    except subprocess.CalledProcessError as e:
        progress_bar.stop()
        messagebox.showerror("Error", f"Error al crear el ejecutable: {e}")

app = tk.Tk()
app.title("Creador de Ejecutables .exe")
app.configure(bg="#2e3f4f")

style = ttk.Style()
style.theme_use("clam")

style.configure("TButton", padding=6, relief="flat", background="#4CAF50", foreground="white", font=("Helvetica", 10, "bold"))
style.map("TButton", background=[("active", "#45a049")])

style.configure("TLabel", padding=6, background="#2e3f4f", foreground="white", font=("Helvetica", 10))
style.configure("TEntry", padding=6, font=("Helvetica", 10))
style.configure("TFrame", background="#2e3f4f")
style.configure("TCheckbutton", background="#2e3f4f", foreground="white", font=("Helvetica", 10))

frame = ttk.Frame(app, padding="10 10 10 10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

label_file = ttk.Label(frame, text="Archivo .py:")
label_file.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

entry_file = ttk.Entry(frame, width=50)
entry_file.grid(row=0, column=1, padx=5, pady=5, sticky=(tk.W, tk.E))

button_file = ttk.Button(frame, text="Seleccionar", command=select_file)
button_file.grid(row=0, column=2, padx=5, pady=5)

label_icon = ttk.Label(frame, text="Icono (cualquier imagen):")
label_icon.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)

entry_icon = ttk.Entry(frame, width=50)
entry_icon.grid(row=1, column=1, padx=5, pady=5, sticky=(tk.W, tk.E))

button_icon = ttk.Button(frame, text="Seleccionar", command=select_icon)
button_icon.grid(row=1, column=2, padx=5, pady=5)

var_no_console = tk.BooleanVar()
check_no_console = ttk.Checkbutton(frame, text="No abrir consola", variable=var_no_console)
check_no_console.grid(row=2, column=0, columnspan=3, pady=5, sticky=tk.W)

button_create = ttk.Button(frame, text="Crear .exe", command=create_executable)
button_create.grid(row=3, column=0, columnspan=3, pady=10)

progress_bar = ttk.Progressbar(frame, mode='indeterminate')
progress_bar.grid(row=4, column=0, columnspan=3, pady=10, sticky=(tk.W, tk.E))

frame.columnconfigure(1, weight=1)

app.mainloop()
