from customtkinter import *
from PIL import Image
from pytube import YouTube
import os

c_negro = "#010101"
c_verde = "#008000"

root = CTk()
root.geometry("700x600")
root.resizable(0, 0)
current_path = os.path.dirname(os.path.realpath(__file__))
root.title("Script")

set_appearance_mode("dark")

img = Image.open(current_path + "/logo.png")
img2 = Image.open(current_path + "/cambio.png")

def accion():
    # Obtener el enlace del video desde la entrada de texto
    enlace = entry1.get()
    
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

def accion2():
    # Obtener el enlace del video desde la entrada de texto
    enlace = entry2.get()
    
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
    else:
        ruta_temporal = f"{ruta_descarga}/{descarga.title}.mp4"
        ruta_destino = f"{ruta_descarga}/{descarga.title}.mp3"
        os.rename(ruta_temporal, ruta_destino)
    
def nombre():
    global nombre_archivo
    aux = entry3.get()
    nombre_archivo = aux

def mostrar(*arg):
    if check_var.get() == True:
        entry4 = CTkEntry(master=frame, placeholder_text="(OPCIONAL)", width=250, text_color="#FFFFFF")
        entry4.place(relx=0.55, rely=0.75, anchor="center")

        boton4 = CTkButton(frame, text="Cambiar", corner_radius=32, fg_color=c_negro, hover_color="#4158D0", border_color="#FFFFFF", border_width=2, image=CTkImage(dark_image=img2, light_image=img2), command=lambda: direccion(entry4))
        boton4.place(relx=0.55, rely=0.825, anchor="center")

        mostrar.entry4 = entry4
        mostrar.boton4 = boton4
        
        return entry4

    else:
        if hasattr(mostrar, 'entry4') and mostrar.entry4 is not None:
            mostrar.entry4.place_forget()
            mostrar.entry4 = None
        if hasattr(mostrar, 'boton4') and mostrar.boton4 is not None:
            mostrar.boton4.place_forget()
            mostrar.boton4 = None

def direccion(entry4):
    global ruta_descarga
    aux = entry4.get()
    aux = aux.replace("\\", "/")
    aux = aux.replace('"', '')
    ruta_descarga = aux
    print(ruta_descarga)


Text1 = CTkLabel(master=root, text="Script para descargar videos de Youtube en alta calidad:)", font=("Arial", 20), text_color = "#FFFFFF")
Text1.place(relx=0.5, rely=0.1, anchor="center")

ruta_descarga = current_path
nombre_archivo = ""

bg_image = CTkImage(Image.open(current_path + "/fondo.png"), size=(1280, 720))
bg_image_label = CTkLabel(root, image=bg_image)
bg_image_label.grid(row=0, column=0)

frame = CTkFrame(master=root, width=300, height=600, corner_radius=0, bg_color=c_negro)
frame.place(relx=0, rely=0)
# frame.attributes("-alpha", 0.7)

# CAMBIO DIRECCION
check_var = BooleanVar(value=False)
checkbox = CTkCheckBox(master=frame, text="Cambiar ruta de guardado", fg_color="#FF0000", checkbox_height=20, checkbox_width=20, corner_radius=10, variable=check_var, onvalue=True, offvalue=False)
checkbox.place(relx=0.55, rely=0.7, anchor="center")
check_var.trace_add("write", mostrar)

# CAMBIO NOMBRE
Text3 = CTkLabel(master=frame, text="Cambiar nombre archivo:", font=("Arial", 16), text_color = "#FFFFFF")
Text3.place(relx=0.55, rely=0.1, anchor="center")

entry3 = CTkEntry(master=frame, placeholder_text="(OPCIONAL)", width=250, text_color="#FFFFFF")
entry3.place(relx=0.55, rely=0.15, anchor="center")

boton3 = CTkButton(frame, text="Cambiar", corner_radius=32, fg_color=c_negro, hover_color="#4158D0", border_color="#FFFFFF", border_width=2, image=CTkImage(dark_image=img2, light_image=img2), command=nombre)
boton3.place(relx=0.55, rely=0.225, anchor="center")

# DESCARGA AUDIO
Text2 = CTkLabel(master=frame, text="Descargar en formato mp3: ", font=("Arial", 16), text_color = "#FFFFFF")
Text2.place(relx=0.55, rely=0.5, anchor="center")

entry2 = CTkEntry(master=frame, placeholder_text="Ingrese el link del video", width=250, text_color="#FFFFFF")
entry2.place(relx=0.55, rely=0.55, anchor="center")

boton2 = CTkButton(frame, text="Descargar", corner_radius=32, fg_color=c_negro, hover_color="#4158D0", border_color="#FFFFFF", border_width=2, image=CTkImage(dark_image=img, light_image=img), command=accion2)
boton2.place(relx=0.55, rely=0.625, anchor="center")

# DESCARGA VIDEO
TextFinal = CTkLabel(master=frame, text="Descargar video en alta calidad:", font=("Arial", 16), text_color = "#FFFFFF")
TextFinal.place(relx=0.55, rely=0.3, anchor="center")

entry1 = CTkEntry(master=frame, placeholder_text="Ingrese el link del video", width=250, text_color="#FFFFFF")
entry1.place(relx=0.55, rely=0.35, anchor="center")

boton1 = CTkButton(frame, text="Descargar", corner_radius=32, fg_color=c_negro, hover_color="#4158D0", border_color="#FFFFFF", border_width=2, image=CTkImage(dark_image=img, light_image=img), command=accion)
boton1.place(relx=0.55, rely=0.425, anchor="center")

root.mainloop()