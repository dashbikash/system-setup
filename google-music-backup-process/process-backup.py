import zipfile
import os
import glob
import music_tag
import shutil
import threading

work_dir="/mnt/drive-b/GoogleMusic"
tmp_dir="/mnt/drive-b/my-music"+"/tmp"
output_dir="/mnt/drive-b/my-music"+"/output"

# Create Working Dirs
if os.path.exists(tmp_dir)!=True: os.makedirs(tmp_dir)
if os.path.exists(output_dir)!=True: os.makedirs(output_dir)


def unzip(zip_file):
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(tmp_dir+'/'+zip_file.split(".")[0].split("/")[-1])



def process_zip(zip_file):
    unzip(zip_file)
   
    mp3_format = tmp_dir+'/'+os.path.basename(zip_file).split('.')[0]+'/**/*.mp3'
    for file in glob.glob(mp3_format, recursive=True):
        print(file)
        audio=music_tag.load_file(file)
        artist,album=str(audio['artist']),str(audio['album'])
        print("Title:",audio["title"])
        print("Artist:",audio['artist'])
        print("Album:",audio['album'])
        print("Album artist:",audio['album_artist'])
        print("Year:",audio['year'])
        dest_dir=output_dir+"/"+artist+"/"+album 
        if os.path.exists(dest_dir)!=True: os.makedirs(dest_dir)            
        dest_file=dest_dir+"/"+os.path.basename(file)
        shutil.move(file,dest_file)



def main():
    zip_format = work_dir+'/*.zip'
    ths=[]
    for file in glob.glob(zip_format, recursive=True):
        print(file)
        ths.append(threading.Thread(target=process_zip,args=(file,)))
    for th in ths:
        th.start()
        
        


main()

# dir_path = unzip_dir+'/**/*.mp3'
# for file in glob.glob(dir_path, recursive=True):
#     print(file)
