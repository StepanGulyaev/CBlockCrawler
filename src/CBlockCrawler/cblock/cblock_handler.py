import os
import re
from pathlib import Path
from CBlockCrawler.datafile.cblock_datafile import CBlock_datafile
from CBlockCrawler.cblock.cblock import CBlock
from CBlockCrawler.funcs.src_functions_handler import Src_functions_handler

class CBlock_handler:

    def __init__( self, cblock_datafile : CBlock_datafile, src_functions_handler : Src_functions_handler, coverage_collection : bool):
        self.cblock_datafile = cblock_datafile
        self.src_file_relpath = os.path.relpath(cblock_datafile.src_file, cblock_datafile.tmp_project_root)
        self.src_functions_handler = src_functions_handler
        self.blocks = self.__get_blocks()
        self.coverage_collection = coverage_collection
        
    def __get_blocks(self):
        with open(self.cblock_datafile.datafile,'r') as datafile:
            content = datafile.read()
        blocks_text = re.split(r'\n\s*\n',content)
        blocks_text = list(filter(lambda x: x and x.strip(), blocks_text))
        
        blocks = []
        block_id = 0
        for block_text in blocks_text:
            block_id += 1
            block_lines = self.__parse_block(block_text)
            b_start_line = self.__get_line_num(block_lines[0])
            b_end_line = self.__get_line_num(block_lines[-1])
            functions_inside = self.__get_functions_inside(b_start_line, b_end_line)
            function_outside = self.__get_function_outside(b_start_line, b_end_line)
            blocks.append(CBlock(block_id, \
                    self.src_file_relpath, \
                    b_start_line, \
                    b_end_line, \
                    functions_inside, \
                    function_outside, \
                    block_lines))
        return blocks

    def __get_functions_inside(self, b_start_line : int ,b_end_line : int):
        functions_inside = []
        for func in self.src_functions_handler.functions:
            if b_start_line <= func.start_line and func.end_line <= b_end_line:
                functions_inside.append(func)
        return functions_inside

    def __get_function_outside(self, b_start_line : int, b_end_line : int):
        for func in self.src_functions_handler.functions:
            if func.start_line <= b_start_line and b_end_line <= func.end_line:
                return func
        return None

    def __parse_block(self, block_text : list):
        pattern = r'\n(?![^"\']*")'
        block_lines = re.split(pattern, block_text) 
        return block_lines
 
    def __get_line_num(self, block_line : str):
        pattern = r'^\d+'
        return int(re.match(pattern,block_line).group())
    

