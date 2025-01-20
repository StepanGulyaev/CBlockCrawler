import re
from pathlib import Path

class CBlock_datafile:

    def __init__(self, tmp_src_file : str, tmp_project_root : str, block_start_regex: re.Pattern, block_end_regex : re.Pattern):
        self.src_file = tmp_src_file
        self.tmp_project_root = tmp_project_root
        self.block_start_regex = block_start_regex
        self.block_end_regex = block_end_regex

        datafile = Path(tmp_src_file)
        self.datafile = datafile.with_suffix(f"{datafile.suffix}.cblock")

        self.datafile_content = ''.join(self.__get_block_from_file(tmp_src_file,block_start_regex,block_end_regex))
        

    def __get_block_from_file(self, src_file : str, block_start_regex : re.Pattern, block_end_regex : re.Pattern ):
        inside_block = False
        level = 0
        lines = []

        with open(src_file, 'r') as file:
            for line_number, line in enumerate(file, start=1):
                if block_start_regex.search(line):
                    if not level:
                        inside_block = True
                        lines.append(f"{line_number} {line}")
                    level += 1
                elif block_end_regex.search(line):
                    if inside_block:
                        level -= 1
                        if level == 0:
                            inside_block = False
                        lines.append(f"{line_number} {line}\n")
                elif inside_block \
                and not block_start_regex.search(line) \
                and not block_end_regex.search(line):
                        lines.append(f"{line_number} {line}")
        return lines

    def touch_datafile(self):
        with open(self.datafile, 'w') as datafile:
            datafile.write(''.join(self.datafile_content))
            
