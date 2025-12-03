# 📥 Descargador Multimedia

Una aplicación de escritorio con interfaz gráfica (GUI) que permite descargar videos, audio y archivos multimedia de manera simple y eficiente.

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-orange.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## 🌟 Características

- **🎥 Descarga de Videos de YouTube**: Descarga videos en la mejor calidad disponible (MP4)
- **🎵 Descarga de Audio de YouTube**: Extrae y descarga solo el audio en formato MP3
- **🖼️ Descarga de Archivos Genéricos**: Descarga imágenes y otros archivos desde URLs directas
- **📁 Selección de Carpeta de Destino**: Elige dónde guardar tus descargas
- **⚡ Descarga en Segundo Plano**: Interfaz no se congela durante las descargas
- **📊 Indicadores de Estado**: Feedback visual del proceso de descarga

## 📋 Requisitos

- Python 3.x
- Dependencias de Python:
  - `tkinter` (incluido por defecto en la mayoría de instalaciones de Python)
  - `pytube`
  - `requests`

## 🚀 Instalación

### 1. Clonar o descargar el proyecto

```bash
git clone <url-del-repositorio>
cd descargador_multimedia
```

### 2. Crear un entorno virtual (recomendado)

```bash
# En Linux/Mac
python3 -m venv venv
source venv/bin/activate

# En Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Instalar dependencias

```bash
pip install pytube requests
```

## 💻 Uso

### Ejecutar la aplicación

```bash
python descargador.py
```

### Pasos para descargar

1. **Pega la URL** del video, audio o archivo que deseas descargar
2. **Selecciona el tipo de descarga**:
   - `Video (YouTube)`: Descarga el video completo en MP4
   - `Audio/Música (YouTube)`: Descarga solo el audio en MP3
   - `Imagen/Genérico`: Descarga archivos directos (imágenes, PDFs, etc.)
3. **Elige la carpeta de destino** (opcional, por defecto usa la carpeta "Descargas")
4. **Haz clic en "▶️ Iniciar Descarga"**
5. **Espera** a que el proceso complete y verás una notificación de éxito

## 📝 Ejemplos de URLs Soportadas

### Videos de YouTube

```
https://www.youtube.com/watch?v=dQw4w9WgXcQ
https://youtu.be/dQw4w9WgXcQ
```

### Archivos Genéricos (imágenes, etc.)

```
https://example.com/imagen.jpg
https://example.com/documento.pdf
```

## 🛠️ Estructura del Proyecto

```
descargador_multimedia/
│
├── descargador.py       # Archivo principal de la aplicación
├── .gitignore          # Archivos ignorados por Git
├── README.md           # Este archivo
└── venv/               # Entorno virtual (no incluido en el repositorio)
```

## ⚙️ Funcionalidades Técnicas

### Arquitectura

- **Interfaz Gráfica**: Construida con Tkinter
- **Threading**: Descargas ejecutadas en hilos separados para mantener la UI responsiva
- **Manejo de Errores**: Captura y muestra errores de manera amigable
- **API de YouTube**: Utiliza pytube para interactuar con YouTube
- **HTTP Requests**: Usa la biblioteca requests para descargas genéricas

### Componentes Principales

```python
class DescargadorApp:
    - __init__()                    # Inicializa la interfaz
    - select_download_path()        # Selector de carpeta
    - start_download_thread()       # Inicia descarga en segundo plano
    - process_download()            # Determina tipo de descarga
    - _download_youtube_video()     # Descarga videos de YouTube
    - _download_youtube_audio()     # Descarga audio de YouTube
    - _download_generic()           # Descarga archivos genéricos
```

## 🐛 Solución de Problemas

### Error: "ModuleNotFoundError: No module named 'pytube'"

```bash
pip install pytube
```

### Error: "No video streams available"

Puede deberse a restricciones de YouTube. Intenta:

- Verificar que la URL sea correcta y el video esté disponible
- Actualizar pytube: `pip install --upgrade pytube`

### Error de permisos al guardar archivos

Asegúrate de tener permisos de escritura en la carpeta de destino seleccionada.

## 🔮 Mejoras Futuras

- [ ] Barra de progreso de descarga
- [ ] Soporte para listas de reproducción de YouTube
- [ ] Selección de calidad de video
- [ ] Historial de descargas
- [ ] Tema oscuro/claro
- [ ] Descargas por lotes (múltiples URLs)
- [ ] Conversión de formatos de video/audio

## 📄 Licencia

Este proyecto es de código abierto y está disponible para uso personal y educativo.

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Si deseas mejorar este proyecto:

1. Haz un Fork del repositorio
2. Crea una rama para tu feature (`git checkout -b feature/nueva-caracteristica`)
3. Commit tus cambios (`git commit -am 'Agrega nueva característica'`)
4. Push a la rama (`git push origin feature/nueva-caracteristica`)
5. Abre un Pull Request

## 👨‍💻 Autor

Desarrollado con ❤️ por alexgrt5

---

⭐ Si este proyecto te fue útil, no olvides darle una estrella!
