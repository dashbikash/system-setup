import os
import glob
import music_tag
import shutil

work_dir="/mnt/drive-b/my-music"


dest_dirs={}

def organize_files():   
    mp3_format = work_dir+'/**/*.mp3'
    for file in glob.glob(mp3_format, recursive=True):
        print(file)
        audio=music_tag.load_file(file)
        artist,album_artist,album=str(audio['artist']).strip(),str(audio['album_artist']).strip(),str(audio['album']).strip()
        # print("Title:",audio["title"])
        # print("Artist:",audio['artist'])
        # print("Album:",audio['album'])
        # print("Album artist:",audio['album_artist'])
        # print("Year:",audio['year'])

        artist_dir= album_artist if len(album_artist)>1 else artist
        dest_dir="%s/%s/%s"% (work_dir,artist_dir,album)  if len(artist_dir)>1 else "%s/%s"% (work_dir,album)
        dest_dirs.append(dest_dirs)
        if os.path.exists(dest_dir)!=True: os.makedirs(dest_dir)            
        dest_file=dest_dir+"/"+os.path.basename(file)
        
        if file.strip()!=dest_file.strip(): 
            print("%s --> %s"%(file,dest_file))
            shutil.move(file,dest_file)



organize_files()

# dir_path = unzip_dir+'/**/*.mp3'
# for file in glob.glob(dir_path, recursive=True):
#     print(file)
