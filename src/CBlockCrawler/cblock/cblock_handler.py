import os
import re
from pathlib import Path
from CBlockCrawler.cblock_datafile import CBlock_datafile
from CBlockCrawler.cblock.cblock import CBlock
from CBlockCrawler.funcs.src_functions_handler import Src_functions_handler

class CBlock_handler:

    def __init__( self, cblock_datafile : CBlock_datafile, src_functions_handler : Src_functions_handler):
        self.cblock_datafile = cblock_datafile
        self.src_file_relpath = os.path.relpath(cblock_datafile.src_file, cblock_datafile.tmp_project_root)
        self.src_functions_handler = src_functions_handler
        self.blocks = self.__get_blocks()
        
    def __get_blocks(self):
        with open(self.cblock_datafile.datafile,'r') as datafile:
            content = datafile.read()
        blocks_text = re.split(r'\n\s*\n',content)
        blocks_text = list(filter(lambda x: x and x.strip(), blocks_text))

        block_id = 0
        for block_text in blocks_text:
            block_id += 1
            block_lines = self.__parse_block(block_text)
            b_start_line_n = self.__get_line_num(block_lines[0])
            b_end_line_n = self.__get_line_num(block_lines[-1])
            functions_inside = self.__get_functions_inside(b_start_line_n,b_end_line_n)
            for func in functions_inside:
                print(func.name)

    def __get_functions_inside(self, b_start_line_n : int ,b_end_line_n : int):
        functions_inside = []
        for func in self.src_functions_handler.functions:
            if b_start_line_n <= func.start_line and func.end_line <= b_end_line_n:
                functions_inside.append(func)
        return functions_inside

    def __parse_block(self, block_text : list):
        pattern = r'\n(?![^"\']*")'
        block_lines = re.split(pattern, block_text) 
        return block_lines
 
    def __get_line_num(self, block_line : str):
        pattern = r'^\d+'
        return int(re.match(pattern,block_line).group())


