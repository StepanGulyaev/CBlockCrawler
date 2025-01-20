import os
import shutil
import re
from CBlockCrawler.cblock_datafile import CBlock_datafile

def get_src_files( project_root : str ):
    src_files = []
    for root, dirs, files in os.walk(project_root):
        for file in files:
            if file.endswith('.c') or file.endswith('.h'):
                file_path = os.path.join(root, file)
                src_files.append(file_path)
    return src_files

def create_tmp_project_copy( project_dir : str ):
    dir_name = "project_dir_tmp"
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


def check_if_block_in_file( src_file : str, block_start_regex : re.Pattern, block_end_regex : re.Pattern ):

    inside_block = False
    level = 0

    with open(src_file, 'r') as file:
        for line_number, line in enumerate(file, start=1):
            if block_start_regex.search(line):
                if not level:
                    inside_block = True
                level += 1
            elif block_end_regex.search(line):
                if inside_block:
                    level -= 1
                    if level == 0:
                        inside_block = False
                    return True
    return False


def get_datafiles( src_files : list, tmp_project_root : str , args):
    datafiles = []
    for file in src_files:
        if check_if_block_in_file(file, args.block_start_regex, args.block_end_regex):
            datafile = CBlock_datafile(file, tmp_project_root, args.block_start_regex ,args.block_end_regex)
            datafiles.append(datafile)
    return datafiles

