import os
import shutil
import re

def get_src_files( project_root : str ):
    src_files = []
    for root, dirs, files in os.walk(project_root):
        for file in files:
            if file.endswith('.c') or file.endswith('.h'):
                file_path = os.path.join(root, file)
                src_files.append(file_path)
    return src_files

def create_tmp_project_copy( project_dir : str ):
    dir_name = "project_tmp_dir"
    dst = os.path.abspath(dir_name)
    try:
        shutil.copytree(project_dir, dst)
    except Exception as e:
        print (f"An error occurred: {e}")
    return dst

def rm_rf_dir ( removed_dir : str):
    try:
        shutil.rmtree(removed_dir)
    except Exception as e:
        print(f"Failed to remove directory '{removed_dir}': {e}")
