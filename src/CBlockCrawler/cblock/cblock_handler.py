import os
import re
from pathlib import Path
from CBlockCrawler.cblock_datafile import CBlock_datafile
from CBlockCrawler.cblock.cblock import CBlock


class CBlock_handler:

    def __init__( self, cblock_datafile : CBlock_datafile ):
        self.cblock_datafile = cblock_datafile
        self.src_file_relpath = os.path.relpath(cblock_datafile.src_file, cblock_datafile.tmp_project_root)
        self.blocks = self.__get_blocks()

    def __get_blocks(self):
        with open(self.cblock_datafile.datafile,'r') as datafile:
            content = datafile.read()
        blocks_text = re.split(r'\n\s*\n',content)
        blocks_text = list(filter(lambda x: x and x.strip(), blocks_text))

        block_id = 1
        for block_text in blocks_text:
            block_lines = self.__parse_block(block_text)
            print(block_lines)
            block_id += 1

        #print(blocks_text)

    def __parse_block(self, block_text : list):
        #block_text = "1234 printf(\"Something good\n aaaa\");\n1235 char a = '\n';"
        pattern = r'\n(?![^"\']*")'
        block_lines = re.split(pattern, block_text) 
        return block_lines

