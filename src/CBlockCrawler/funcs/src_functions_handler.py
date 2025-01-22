import re
import subprocess
import sys
import os
from pathlib import Path
from CBlockCrawler.funcs.src_function import Src_function

class Src_functions_handler:
    def __init__(self, src_file : str):
        self.src_file = src_file

        ctags_file = Path(src_file)
        self.ctags_file = ctags_file.with_suffix(f"{ctags_file.suffix}.ctags") 

        self.functions = self.__get_functions()
        for func in self.functions:
            print(func.name,func.start_line,func.end_line )
   
    def __get_functions(self):
        functions = []
        self.__touch_ctags_file()
        if os.stat(self.ctags_file).st_size == 0: return functions
        print(self.src_file)
        with open(self.ctags_file,'r') as file:
            for line in file:
                if line.strip():
                    fields = line.split()
                    func_name = fields[0]
                    start_line = int(fields[2])
                    end_line =  self.__get_function_end(start_line)
                    functions.append(Src_function(self.src_file,func_name,start_line,end_line))  
        return functions

    def __get_function_end(self,start_line : int):
        with open(self.src_file, 'r') as file:
            lines = file.readlines()

        open_braces = 0
        function_began = False
        for idx, line in enumerate(lines[start_line-1:], start=start_line-1):
            if line.count('{') > 0 and not function_began:
                function_began = True

            open_braces += line.count('{')
            open_braces -= line.count('}')
            
            if open_braces == 0 and function_began:
                return idx + 1

        return None


    def __touch_ctags_file(self):
        try:
            subprocess.run(['ctags','-x','-f',self.ctags_file,'--languages=c','--c-types=f',self.src_file],check=True)
        except subprocess.CalledProcessError as e:
            print(f"Ctags call error: {e}")
            sys.exit(1) 








