from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive

gauth = GoogleAuth()
gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)

file_list = drive.ListFile({'q': "'1D_exe9t6d5g2RoVik1Xp30lzauWrM3A4' in parents and trashed=false"}).GetList()
for file1 in file_list:
  print('title: %s, id: %s' % (file1['title'], file1['id']))

# title: Eduardo Bolsonaro, id: 1Nh53gtPS29O7uH3tgn3_o_Kcq8uhY8w3
# title: Eli Borges, id: 17rvp7YI29_AVTWziBcjazvSSTS0g1jK6
# title: Clarissa Tércio, id: 1OAEn7Lz0RsqBKerWTUTnaZUZhYXhGSVu
# title: André Ferreira, id: 13XpqaK8QO7rYnm7NVNsc__Oj9xRmIZp3
# title: Nikolas Ferreira, id: 1-aukQr4Gyg_8iVgWoiZDtQvJ_elfOZIk
