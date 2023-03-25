import requests
from bs4 import BeautifulSoup
import os

# URL de la página
url = 'http://www.mercadocentral.gob.ar/informaci%C3%B3n/precios-mayoristas-0'

# Carpeta de destino donde se guardarán los archivos descargados
folder_path = 'descargas'

# Crea la carpeta si no existe
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# Realiza la solicitud HTTP y obtiene el contenido HTML de la página
response = requests.get(url)
html_content = response.content

# Analiza el contenido HTML con BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Encuentra todos los enlaces que apuntan a archivos .zip
links = soup.find_all('a', href=lambda href: href and href.endswith('.zip'))

# Descarga cada archivo zip encontrado
for link in links:
    # Obtiene la URL del archivo zip
    file_url = link['href']
    
    # Descarga el archivo y guarda en la carpeta de destino
    file_path = os.path.join(folder_path, os.path.basename(file_url))
    with open(file_path, 'wb') as f:
        response = requests.get(file_url)
        f.write(response.content)
