
import glob
from mutagen.mp3 import MP3
import eyed3
import music_tag
import shutil
import os


work_dir="/mnt/drive-b/my-music"
unzip_dir=work_dir+"/tmp"
output_dir=work_dir+"/output"


dir_path = unzip_dir+'/**/*.mp3'
for f in glob.glob(dir_path, recursive=True):
    print(f)
    audio=music_tag.load_file(f)
    print("Title:",audio["title"])
    print("Artist:",audio['artist'])
    print("Album:",audio['album'])
    print("Album artist:",audio['album_artist'])
    print("Year:",audio['year'])

    # artist,album=str(audio['artist']),str(audio['album'])
    # dest_dir=output_dir+"/"+artist+"/"+album 
    # if os.path.exists(dest_dir)!=True: os.makedirs(dest_dir)            
    # dest_file=dest_dir+"/"+os.path.basename(f)
    # shutil.move(f,dest_file)