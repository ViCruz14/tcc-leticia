import glob
import os

from tqdm import tqdm


def upload_arquivos_para_drive(drive, pasta_local, pasta_drive_id):
    arquivos_jpeg = glob.glob(os.path.join(pasta_local, '*.jpg'))
    arquivos_mp4 = glob.glob(os.path.join(pasta_local, '*.mp4'))
    arquivos_txts = glob.glob(os.path.join(pasta_local, '*.txt'))
    arquivos = arquivos_jpeg + arquivos_mp4 + arquivos_txts
    
    for arquivo in tqdm(arquivos, total=len(arquivos)):
        nome_arquivo = os.path.basename(arquivo)
        arquivo_drive = drive.CreateFile({
            'title': nome_arquivo,
            'parents': [{'id': pasta_drive_id}]
        })
        arquivo_drive.SetContentFile(arquivo)
        arquivo_drive.Upload()
