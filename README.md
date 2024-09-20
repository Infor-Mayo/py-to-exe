# Creador de Ejecutables .exe 🚀

Este script de Python utiliza `tkinter` para crear una interfaz gráfica que permite a los usuarios convertir archivos `.py` en ejecutables `.exe` utilizando `PyInstaller`. También permite seleccionar un icono para el ejecutable y la opción de no abrir una consola al ejecutar el `.exe`. 🖥️💻

## Requisitos 📋

- Python 3.x 🐍
- `tkinter` (generalmente incluido con Python)
- `Pillow` (para manejar la conversión de imágenes a iconos `.ico`) 🖼️
- `PyInstaller` 📦

Puedes instalar las dependencias necesarias con el siguiente comando:

sh
pip install pillow pyinstaller


## Uso 🛠️

1. **Seleccionar el archivo `.py`**: Haz clic en el botón "Seleccionar" junto a "Archivo .py" y elige el archivo Python que deseas convertir en un ejecutable. 📄

2. **Seleccionar el icono**: Haz clic en el botón "Seleccionar" junto a "Icono (cualquier imagen)" y elige una imagen para usar como icono del ejecutable. La imagen será convertida automáticamente a formato `.ico`. 🖼️

3. **No abrir consola**: Marca la casilla "No abrir consola" si no deseas que se abra una consola al ejecutar el archivo `.exe`. 🚫

4. **Crear el ejecutable**: Haz clic en el botón "Crear .exe". El progreso se mostrará en la barra de progreso y recibirás un mensaje de éxito o error al finalizar. ✅❌


## Notas 📝

- Asegúrate de tener `PyInstaller` instalado y accesible desde tu línea de comandos. 🖥️
- La conversión de imágenes a iconos `.ico` se realiza automáticamente si seleccionas una imagen que no esté en formato `.ico`. 🔄
- La opción "No abrir consola" es útil para aplicaciones con interfaz gráfica que no necesitan una ventana de consola. 🪟

¡Disfruta creando tus ejecutables! 🎉🎊