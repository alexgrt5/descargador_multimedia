import tkinter as tk
from tkinter import messagebox, filedialog
from pytube import YouTube
import requests
import os
import threading

# --- Configuración principal de la interfaz ---

class DescargadorApp:
    def __init__(self, master):
        self.master = master
        master.title("Descargador Multimedia JPG, MP4 Y MP3")
        master.geometry("500x300")
        
        # Variable para almacenar la ruta de guardado seleccionada
        self.download_path = os.path.expanduser("~/Downloads") 

        # Título
        tk.Label(master, text="Ingresa la URL del Archivo/Video:", font=("Arial", 12)).pack(pady=10)

        # Campo de entrada para la URL
        self.url_entry = tk.Entry(master, width=60)
        self.url_entry.pack(pady=5)

        # Opciones de descarga (Video, Audio/Música, Imagen/Genérico)
        tk.Label(master, text="Tipo de Descarga:", font=("Arial", 10)).pack()
        
        self.download_type = tk.StringVar(master)
        self.download_type.set("Video (YouTube)") # Valor por defecto
        
        opciones = ["Video (YouTube)", "Audio/Música (YouTube)", "Imagen/Genérico"]
        
        self.type_menu = tk.OptionMenu(master, self.download_type, *opciones)
        self.type_menu.pack(pady=5)

        # Botón para seleccionar la carpeta de guardado
        self.path_button = tk.Button(master, text=f"Carpeta de Guardado: {os.path.basename(self.download_path)}", command=self.select_download_path)
        self.path_button.pack(pady=5)

        # Botón de Descarga
        self.download_button = tk.Button(master, text="▶️ Iniciar Descarga", command=self.start_download_thread, bg="green", fg="white", font=("Arial", 10, "bold"))
        self.download_button.pack(pady=20)
        
        # Etiqueta de estado
        self.status_label = tk.Label(master, text="Esperando URL...", fg="blue")
        self.status_label.pack(pady=5)

    # --- Métodos de la interfaz ---
    
    def select_download_path(self):
        """Abre un diálogo para que el usuario seleccione la carpeta de destino."""
        new_path = filedialog.askdirectory(initialdir=self.download_path)
        if new_path:
            self.download_path = new_path
            self.path_button.config(text=f"Carpeta de Guardado: {os.path.basename(self.download_path)}")
            self.status_label.config(text=f"Ruta cambiada a: {self.download_path}")

    def start_download_thread(self):
        """Inicia la descarga en un hilo separado para no congelar la GUI."""
        url = self.url_entry.get()
        if not url:
            messagebox.showerror("Error", "Por favor, ingresa una URL.")
            return

        # Deshabilita el botón y actualiza el estado mientras descarga
        self.download_button.config(state=tk.DISABLED, text="⌛ Descargando...")
        self.status_label.config(text="Descargando, por favor espera...", fg="orange")
        
        # Crea y arranca el hilo de descarga
        thread = threading.Thread(target=self.process_download, args=(url,))
        thread.start()

    # --- Lógica de Descarga (Ejecutada en el hilo) ---

    def process_download(self, url):
        """Determina el tipo de descarga y llama a la función correspondiente."""
        download_type = self.download_type.get()
        
        try:
            if "youtube" in url.lower() or "youtu.be" in url.lower():
                if "Video" in download_type:
                    self._download_youtube_video(url)
                elif "Audio/Música" in download_type:
                    self._download_youtube_audio(url)
                else:
                    messagebox.showerror("Error", "Tipo de descarga de YouTube no reconocido.")
            else:
                self._download_generic(url)
                
        except Exception as e:
            messagebox.showerror("Error de Descarga", f"Ocurrió un error: {e}")
            self.master.after(0, lambda: self.status_label.config(text="⚠️ Error en la descarga.", fg="red"))
            
        finally:
            # Habilita el botón y actualiza el estado al terminar
            self.master.after(0, lambda: self.download_button.config(state=tk.NORMAL, text="▶️ Iniciar Descarga"))
            
    def _download_youtube_video(self, url):
        """Descarga el video de YouTube en la mejor calidad disponible."""
        yt = YouTube(url)
        # Selecciona el stream de video con la mejor resolución
        video_stream = yt.streams.get_highest_resolution() 
        self.master.after(0, lambda: self.status_label.config(text=f"Descargando video: {yt.title}...", fg="orange"))
        video_stream.download(self.download_path)
        self.master.after(0, lambda: messagebox.showinfo("Éxito", f"'{yt.title}' descargado con éxito en {self.download_path}"))
        self.master.after(0, lambda: self.status_label.config(text="✅ Descarga completa.", fg="green"))


    def _download_youtube_audio(self, url):
        """Descarga solo el audio (música) del video de YouTube."""
        yt = YouTube(url)
        # Filtra por solo audio (mp4) y selecciona el primero (generalmente el de mayor bitrate)
        audio_stream = yt.streams.filter(only_audio=True).first()
        self.master.after(0, lambda: self.status_label.config(text=f"Descargando audio: {yt.title}...", fg="orange"))
        
        # Descarga el archivo (será .mp4)
        out_file = audio_stream.download(output_path=self.download_path)
        
        # Cambia la extensión de .mp4 a .mp3
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
        
        self.master.after(0, lambda: messagebox.showinfo("Éxito", f"'{yt.title}' descargado con éxito como MP3 en {self.download_path}"))
        self.master.after(0, lambda: self.status_label.config(text="✅ Descarga completa.", fg="green"))
        
        
    def _download_generic(self, url):
        """Descarga un archivo genérico (como una imagen) usando requests."""
        # Intenta obtener el nombre del archivo de la URL
        filename = url.split('/')[-1]
        
        if not filename or '.' not in filename:
            # Si la URL no tiene un nombre de archivo claro, usa un nombre por defecto
            filename = "descarga_generica_" + url.split('//')[-1].replace('/', '_').replace('.', '_')[:10]
            
        filepath = os.path.join(self.download_path, filename)

        self.master.after(0, lambda: self.status_label.config(text=f"Descargando archivo: {filename}...", fg="orange"))
        
        # Hace la petición GET al archivo
        response = requests.get(url, stream=True)
        response.raise_for_status() # Lanza una excepción para códigos de estado erróneos (4xx o 5xx)

        # Escribe el contenido en el archivo por bloques
        with open(filepath, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
                
        self.master.after(0, lambda: messagebox.showinfo("Éxito", f"'{filename}' descargado con éxito en {self.download_path}"))
        self.master.after(0, lambda: self.status_label.config(text="✅ Descarga completa.", fg="green"))

# --- Punto de entrada principal ---
if __name__ == "__main__":
    root = tk.Tk()
    app = DescargadorApp(root)
    root.mainloop()