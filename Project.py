import os
import dropbox

path = 'C:/Users/HIBA PC/Desktop/Python/Dropbox Upload/files'

list = os.listdir(path)
print(list)

def upload_file(files_name):
    access_token = 'sl.A5L55jShlU-gqzlXAZgGRnZEHcZ4jSlI3bTWaUSe11sFgQSf172HAwCtnQEFY5m0DOc_-cyDuNbhUcMSQJE95jQr33_P-qd7g3mSonjQCZ12d9w1tBUgN8lux7MELW-wN1ee04tpksM'
    file = files_name
    file_from = 'C:/Users/HIBA PC/Desktop/Python/Dropbox Upload/files/' + file
    file_to="/First Class/"+(files_name)
    dbx = dropbox.Dropbox(access_token)

    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to,mode=dropbox.files.WriteMode.overwrite)
        print("file uploaded")


for v in list:
    upload_file(v)