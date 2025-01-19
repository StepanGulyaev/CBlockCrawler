import os
from CBlockCrawler.files_func import get_src_files
from CBlockCrawler.files_func import create_tmp_project_copy
from CBlockCrawler.files_func import rm_rf_dir
from CBlockCrawler.files_func import check_if_block_in_file
from CBlockCrawler.cblock_datafile import CBlock_datafile
from CBlockCrawler.cli import parse_main_args

def get_datafiles( src_files : list, args):
    datafiles = []
    for file in src_files:
        if check_if_block_in_file(file, args.block_start_regex, args.block_end_regex):
            datafile = CBlock_datafile(file, args.block_start_regex ,args.block_end_regex)
            datafiles.append(datafile)
    return datafiles


def execute_main():
    main_args = parse_main_args()
    tmp_project_dir = create_tmp_project_copy(main_args.project_root)
    src_files = get_src_files(tmp_project_dir)
    datafiles = get_datafiles(src_files, main_args)
    for datafile in datafiles: 
        datafile.touch_datafile()
    


    #rm_rf_dir(tmp_project_dir)

if __name__ == '__main__':
    execute_main()
