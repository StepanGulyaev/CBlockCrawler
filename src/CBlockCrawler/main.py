import os
import clang.cindex
from CBlockCrawler.files_func import get_src_files
from CBlockCrawler.files_func import create_tmp_project_copy
from CBlockCrawler.files_func import rm_rf_dir
from CBlockCrawler.files_func import check_if_block_in_file
from CBlockCrawler.files_func import get_datafiles
from CBlockCrawler.cblock_datafile import CBlock_datafile
from CBlockCrawler.cblock.cblock_handler import CBlock_handler
from CBlockCrawler.funcs.src_functions_handler import Src_functions_handler
from CBlockCrawler.cli import parse_main_args

def execute_main():
    main_args = parse_main_args()
    tmp_project_root = create_tmp_project_copy(main_args.project_root)
    src_files = get_src_files(tmp_project_root)
    datafiles = get_datafiles(src_files, tmp_project_root, main_args)
    for datafile in datafiles: 
        datafile.touch_datafile()
        src_func_handler = Src_functions_handler(datafile.src_file)
        cblock_handler = CBlock_handler(datafile, src_func_handler)


    



    if not main_args.save_tmp_files: rm_rf_dir(tmp_project_root)  

    #rm_rf_dir(tmp_project_dir)

if __name__ == '__main__':
    execute_main()
