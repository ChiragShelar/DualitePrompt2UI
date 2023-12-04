import os
import time
import glob

def watch_folder(folder_path, target_file_count):
    while True:
        # List files in the folder
        files = glob.glob(os.path.join(folder_path, '*'))
        
        # Check if the file count reaches the target
        if len(files) >= target_file_count:
            # Return a list of file names
            return [os.path.basename(file) for file in files]

        # Add a delay before the next check
        time.sleep(1)

