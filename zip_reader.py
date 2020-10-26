from zipfile import ZipFile
from pathlib import Path


def pdf_names():
    
    unzipped_file =  ZipFile(list(Path.cwd().rglob('*.zip'))[0])
    files = list(unzipped_file.namelist())

    pdf_files = sorted(list(filter(lambda file: file.endswith('.pdf'), files)))

    for pdf in pdf_files:
        unzipped_file.extract(pdf)
        

    unzipped_file.close()
    return [pdf_files[0].split('/')[0], pdf_files]
