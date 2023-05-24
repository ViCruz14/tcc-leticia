import os

from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive

from generate_csv import gerar_csv_no_drive
from upload_drive import upload_arquivos_para_drive

gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

ids = {
        "nikolasferreiradm": "1-aukQr4Gyg_8iVgWoiZDtQvJ_elfOZIk-",
        "andreferreira.pe":"13XpqaK8QO7rYnm7NVNsc__Oj9xRmIZp3",
        "clarissatercio": "1OAEn7Lz0RsqBKerWTUTnaZUZhYXhGSVu",
        "dep.eliborges":"17rvp7YI29_AVTWziBcjazvSSTS0g1jK6",
        "bolsonarosp": "1Nh53gtPS29O7uH3tgn3_o_Kcq8uhY8w3"
    }

folder_path = os.getcwd()

for pessoa in ids.items():
    upload_arquivos_para_drive(drive, f'{folder_path}/{pessoa[0]}', pessoa[1])
    gerar_csv_no_drive(drive, pessoa[1])
