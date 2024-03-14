#files Organizer,Made by Ayoub Oulaarbi
import os
from pathlib import Path

#parent directory
directory = "C:\\Users\\username\\downloads";

#directories to be created
doc_dir = "doc_files";
zip_dir = "zip_files";
img_dir = "img_files";
video_dir = "video_files";
pdf_dir = "pdf_files";

#the full paths of the directories
doc_path = os.path.join(directory,doc_dir)
zip_path = os.path.join(directory,zip_dir)
img_path = os.path.join(directory,img_dir);
vid_path = os.path.join(directory,video_dir)
pdf_path = os.path.join(directory,pdf_dir)

#list of directories
lis = [doc_path,zip_path,img_path,vid_path,pdf_path];

def move_file(destination,file):
    file_location = os.path.join(directory,file);
    file_destination = os.path.join(destination,file);
    Path(file_location).rename(file_destination);

try:
    for element in lis:
        os.mkdir(element)
except Exception as e:
    print(e);
# except FileExistsError:
#     print("The directories already exist ! you have to delete them");
finally:
    for file in os.listdir(directory):
        if os.path.isfile(file):
            if file.endswith(".mp4"):
                move_file(vid_path,file);
            elif file.endswith(".pdf"):
                move_file(pdf_path,file);
            elif file.endswith((".png",".jpg",".jpeg")):
                move_file(img_path,file);
            elif file.endswith((".pptx",".doc",".html",".htm",".php",".webp",".xlsx",".txt")):
                move_file(doc_path,file);
            elif file.endswith((".zip",".rar")):
                move_file(zip_path,file);
