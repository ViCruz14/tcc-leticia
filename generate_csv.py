import csv
import re
from io import StringIO

from tqdm import tqdm

regex = r"_\d+"

def gerar_csv_no_drive(drive, folder_id):
    image_links = {}

    query_images = f"'{folder_id}' in parents and mimeType = 'image/jpeg' and trashed=false"
    query_txts = f"'{folder_id}' in parents and mimeType = 'text/plain' and trashed=false"

    images_list = drive.ListFile({'q': query_images}).GetList()
    txts_list = drive.ListFile({'q': query_txts}).GetList()

    for file in images_list:
        title = re.sub(regex, "", file['title']).split(".")[0]
        link = file['alternateLink']
        
        if title in image_links:
            image_links[title].append(link)
        else:
            image_links[title] = [link]


    csv_buffer = StringIO()
    csv_writer = csv.writer(csv_buffer, delimiter=";")

    for file in tqdm(txts_list, total=len(image_links)):
        title = file['title'].split(".")[0]

        file_content = drive.CreateFile({'id': file['id']}).GetContentString().replace("\n", "")

        csv_writer.writerow([",".join(image_links[title]),file_content])


    output_file = "final_list.csv"
    output_path = f"/{folder_id}/{output_file}"

    combined_file = drive.CreateFile({'title': output_file, 'parents': [{'id': folder_id}]})
    combined_file.SetContentString(csv_buffer.getvalue())
    combined_file.Upload()
