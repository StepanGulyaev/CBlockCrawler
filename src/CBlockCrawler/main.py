import os
from CBlockCrawler.files_func import get_src_files
from CBlockCrawler.files_func import create_tmp_project_copy
from CBlockCrawler.files_func import rm_rf_dir
from CBlockCrawler.cblock_datafile import CBlock_datafile
from CBlockCrawler.cli import parse_main_args


def execute_main():
    main_args = parse_main_args()
    tmp_project_dir = create_tmp_project_copy(main_args.project_root)
    src_files = get_src_files(tmp_project_dir)
    
    data_files = []
    for file in src_files:
        datafile = CBlock_datafile(file, main_args.block_start_regex ,main_args.block_end_regex)
    data_files = list(filter(bool,data_files))
    print(''.join(data_files))

    #rel_paths = list(map(lambda x: os.path.relpath(x, project_root),src_files))
    #print(src_files)
    rm_rf_dir(tmp_project_dir)

if __name__ == '__main__':
    execute_main()
