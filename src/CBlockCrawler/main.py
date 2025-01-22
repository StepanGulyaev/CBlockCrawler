import os
from CBlockCrawler.files_func import create_tmp_project_copy
from CBlockCrawler.files_func import rm_rf_dir
from CBlockCrawler.datafile.cblock_datafile_handler import CBlock_datafile_handler
#from CBlockCrawler.cblock.cblock_handler import CBlock_handler
#from CBlockCrawler.funcs.src_functions_handler import Src_functions_handler
from CBlockCrawler.report.txt_report_generator import TXTReportGenerator
from CBlockCrawler.cli import parse_main_args

def execute_main():
    main_args = parse_main_args()
    tmp_project_root = create_tmp_project_copy(main_args.project_root)
    datafile_handler = CBlock_datafile_handler(tmp_project_root,main_args)
    
    match main_args.format:
        case 'txt':
            report_gen = TXTReportGenerator(datafile_handler,main_args.report_name)
            report_gen.generate_report()


    #for datafile in datafile_handler.datafiles: 
        #src_func_handler = Src_functions_handler(datafile.src_file)
        #cblock_handler = CBlock_handler(datafile, src_func_handler)
        
    
    if not main_args.save_tmp_files: rm_rf_dir(tmp_project_root)  


if __name__ == '__main__':
    execute_main()
