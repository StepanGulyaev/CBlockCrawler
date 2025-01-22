import re
from CBlockCrawler.datafile.cblock_datafile import CBlock_datafile
from CBlockCrawler.files_func import get_src_files

class CBlock_datafile_handler:

    def __init__(self, tmp_project_root : str, args):
        self.tmp_project_root = tmp_project_root
        self.args = args
        self.src_files = get_src_files(tmp_project_root)
        self.datafiles = self.__get_datafiles()


    def __get_datafiles(self):
        datafiles = []
        for file in self.src_files:
            if self.__check_if_block_in_file(file):
                datafile = CBlock_datafile(file, self.tmp_project_root, self.args)
                datafile.touch_datafile()
                datafiles.append(datafile)
                
        return datafiles

    def __check_if_block_in_file(self, src_file):
        inside_block = False
        level = 0

        with open(src_file, 'r') as file:
            for line_number, line in enumerate(file, start=1):
                if self.args.block_start_regex.search(line):
                    if not level:
                        inside_block = True
                    level += 1
                elif self.args.inner_level_regex and \
                        any(re.search(regex, line) for regex in self.args.inner_level_regex) and \
                        inside_block:
                    level += 1
                elif self.args.block_end_regex.search(line):
                    if inside_block:
                        level -= 1
                        if level == 0:
                            inside_block = False
                            return True
        return False

