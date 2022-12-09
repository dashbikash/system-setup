import zipfile
work_dir="/mnt/drive-b/GoogleMusic"
zip_file="m666.zip"
with zipfile.ZipFile(work_dir+"/"+zip_file, 'r') as zip_ref:
    zip_ref.extractall(work_dir+"/unzipped/"+zip_file.split(".")[0])