import os
import shutil
import time
import random

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

source = "C:/Users/owoad/Downloads"
dest = 'C:/Users/owoad/Desktop/downloaded files'

dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}
class FileMovementHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(event)
        print(event.src_path)
        name,extention = os.path.splitext(event.src_path) 
        time.sleep(1)
        for key,value in dir_tree.items():
            time.sleep(1)
            if extention in value:
                file_name = os.path.basename(event.src_path)
                path_1 = source + "/" + file_name
                path_2 = dest + "/" + key
                path_3 = dest + "/" + key + "/" + file_name
                if (os.path.exists(path_2)):
                    time.sleep(1)
                    if (os.path.exists(path_3)):
                        print("File already exists in " + key )
                        new_file_name = os.path.splitext(file_name)[0] + str(random.randint(1,20)) + os.path.splitext(file_name)[1]
                        path_4 = dest + "/" + key + "/" + new_file_name
                        print("Renamed file to ",new_file_name )
                        print("Moving... " + new_file_name )
                        shutil.move(path_1,path_4)
                        time.sleep(1)
                    else:
                        print("Moving..." + file_name)
                        shutil.move(path_1,path_3)
                        time.sleep(1)
                else:
                    print("Folder does not exist")
                    print("Making the folder...")
                    os.makedirs(path_2)
                    print("Moving..." + file_name)
                    shutil.move(path_1,path_3)
                    time.sleep(1)

event_handler = FileMovementHandler()

observer = Observer()

observer.schedule(event_handler, source, recursive=True)

observer.start()

try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    observer.stop()
    print("Observar Stoped")