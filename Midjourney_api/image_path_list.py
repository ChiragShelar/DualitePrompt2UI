import os

def image_path_list(directory_path, file_names):
    return [os.path.join(directory_path, file_name) for file_name in file_names]
