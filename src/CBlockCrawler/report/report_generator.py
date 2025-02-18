from abc import ABC, abstractmethod
from CBlockCrawler.datafile.cblock_datafile_handler import CBlock_datafile_handler
from CBlockCrawler.cblock.cblock_handler import CBlock_handler
from CBlockCrawler.funcs.src_functions_handler import Src_functions_handler

class ReportGenerator(ABC):
    def __init__(self, datafile_handler : CBlock_datafile_handler, report_name : str, coverage_file : str):
        self.name = report_name
        self.fields = ["Source file","Id","Lines","Num of Lines","Functions inside","In function"]

        if coverage_file is not None:
            self.fields.append("Coverage")
            coverage_collection = True
        else: coverage_collection = False

        self.cblock_handlers = []
        for datafile in datafile_handler.datafiles:
            src_func_handler = Src_functions_handler(datafile.src_file)
            cblock_handler = CBlock_handler(datafile, src_func_handler,coverage_collection)
            self.cblock_handlers.append(cblock_handler)
        
        self.all_records = []
        for handler in self.cblock_handlers:
            one_file_records = []
            for block in handler.blocks:
                record = block.get_record()
                if coverage_collection:
                    record.append(block.get_block_coverage(coverage_file))
                one_file_records.append(record)
            self.all_records.append(one_file_records)





    def generate_report(self):
        pass

