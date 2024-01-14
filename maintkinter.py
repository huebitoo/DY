from pytube import YouTube
from tkinter import *
from tkinter import messagebox as Messagebox
import os

def accion2():
    # Obtener el enlace del video desde la entrada de texto
    enlace = audio.get()
    
    global ruta_descarga
    global nombre_archivo
    # Crear un objeto YouTube con el enlace proporcionado
    videos = YouTube(enlace)
    
    # Obtener la mejor resolución disponible para el video
    descarga = videos.streams.filter(only_audio=True).first()

    descarga.download(output_path=ruta_descarga)

    if nombre_archivo != "":
        ruta_temporal = f"{ruta_descarga}/{descarga.title}.mp4"
        ruta_destino = f"{ruta_descarga}/{nombre_archivo}.mp3"
        os.rename(ruta_temporal, ruta_destino)
    
    
    # Descarga el video  
    

def accion():
    # Obtener el enlace del video desde la entrada de texto
    enlace = video.get()
    
    global ruta_descarga
    global nombre_archivo
    # Crear un objeto YouTube con el enlace proporcionado
    videos = YouTube(enlace)
    
    # Obtener la mejor resolución disponible para el video
    descarga = videos.streams.get_highest_resolution()
    
    # Descarga el video  
    descarga.download(output_path=ruta_descarga)

    if nombre_archivo != "":
        ruta_temporal = f"{ruta_descarga}/{descarga.title}.mp4"
        ruta_destino = f"{ruta_descarga}/{nombre_archivo}.mp4"
    os.rename(ruta_temporal, ruta_destino)

def direccion():
    global ruta_descarga
    aux = ruta.get()
    aux = aux.replace("\\", "/")
    aux = aux.replace('"', '')
    ruta_descarga = aux

def nombre():
    global nombre_archivo
    aux = name.get()
    nombre_archivo = aux

ruta_descarga = "C:/Users/campo/OneDrive/Escritorio/codigo"
nombre_archivo = ""
ventana = Tk()
ventana.title("Script descargar videos")
ventana.geometry("650x300")
ventana.resizable(0,0)

image = PhotoImage(file="C:/Users/campo/OneDrive/Escritorio/codigo/python/turtle/logo.png")
foto = Label(ventana, image=image, bd=0)
foto.grid(row=0, column=0)

milabel = Label(ventana, text="Script para la descarga de videos de Youtube en alta calidad\n Solo debe copiar el link del video que desea descargar y pegarlo en el bloque")
milabel.grid(row=0, column=1)

# CAMBIO DE RUTA DESCARGA

Text2 = Label(ventana, text="Ingrese la ruta de descarga (opcional):")
Text2.grid(row=1, column=0)

ruta = Entry(ventana)
ruta.grid(row=2, column=0)

boton1 = Button(ventana, text="Cambio", command=direccion)
boton1.grid(row=3, column=0)


# VIDEOS DESCARGA

Text1 = Label(ventana, text="Ingrese el link acá (VIDEO):")
Text1.grid(row=4, column=0)

video = Entry(ventana)
video.grid(row=5, column=0)

boton2 = Button(ventana, text="Descarga", command=accion)
boton2.grid(row=6, column=0)

# AUDIOS DESCARGA

Text3 = Label(ventana, text="Ingrese el link acá (AUDIO):")
Text3.grid(row=4, column=1)

audio = Entry(ventana)
audio.grid(row=5, column=1)

boton3 = Button(ventana, text="Descarga", command=accion2)
boton3.grid(row=6, column=1)

# NOMBRE AUDIO O VIDEO

Text4 = Label(ventana, text="Ingrese el nombre del archivo (opcional):")
Text4.grid(row=1, column=1)

name = Entry(ventana)
name.grid(row=2, column=1)

boton4 = Button(ventana, text="Cambio", command=nombre)
boton4.grid(row=3, column=1)

ventana.mainloop()