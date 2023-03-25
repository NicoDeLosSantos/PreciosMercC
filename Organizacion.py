import os
import zipfile
import pandas as pd

# Carpeta donde se guardaron los archivos zip descargados
folder_path = 'descargas'

# Carpeta donde se guardarán los archivos Excel descomprimidos
extract_folder_path = 'descomprimidos'

# Crea la carpeta si no existe
if not os.path.exists(extract_folder_path):
    os.makedirs(extract_folder_path)

# Recorre todos los archivos zip en la carpeta de descarga
for filename in os.listdir(folder_path):
    if filename.endswith('.zip'):
        # Ruta completa del archivo zip
        file_path = os.path.join(folder_path, filename)
        
        # Descomprime el archivo zip en la carpeta de extracción
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            zip_ref.extractall(extract_folder_path)
            
# Encuentra todos los archivos Excel descomprimidos en la carpeta de extracción
excel_files = [os.path.join(extract_folder_path, f) for f in os.listdir(extract_folder_path) if f.endswith('.xls')]

# Combina los datos de los archivos Excel en un solo DataFrame
dfs = []
for file in excel_files:
    # Lee el archivo Excel en un DataFrame
    df = pd.read_excel(file, sheet_name='Hoja1')
    
    # Agrega una columna con el nombre del archivo de origen
    df['Archivo'] = os.path.basename(file)
    
    # Agrega el DataFrame a la lista
    dfs.append(df)
    
# Concatena los DataFrames en uno solo
combined_df = pd.concat(dfs, ignore_index=True)

# Muestra los primeros 5 registros del DataFrame combinado
print(combined_df.head())
