from abc import ABC, abstractmethod
from CBlockCrawler.datafile.cblock_datafile_handler import CBlock_datafile_handler
from CBlockCrawler.cblock.cblock_handler import CBlock_handler
from CBlockCrawler.funcs.src_functions_handler import Src_functions_handler

class ReportGenerator(ABC):
    def __init__(self, datafile_handler : CBlock_datafile_handler, report_name : str):
        self.name = report_name
        self.fields = ["Source file","Id","Lines","Num of Lines","Functions inside","In function"]
        self.cblock_handlers = []
        for datafile in datafile_handler.datafiles:
            src_func_handler = Src_functions_handler(datafile.src_file)
            cblock_handler = CBlock_handler(datafile, src_func_handler)
            self.cblock_handlers.append(cblock_handler)

    def generate_report(self):
        pass

