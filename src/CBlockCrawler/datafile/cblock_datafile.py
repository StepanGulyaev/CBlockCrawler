import re
from pathlib import Path

class CBlock_datafile:

    def __init__(self, tmp_src_file : str, tmp_project_root : str, args):

        self.src_file = tmp_src_file
        self.tmp_project_root = tmp_project_root
        self.block_start_regex = args.block_start_regex
        self.inner_level_regex = args.inner_level_regex
        self.block_end_regex = args.block_end_regex
        datafile = Path(tmp_src_file)
        self.datafile = datafile.with_suffix(f"{datafile.suffix}.cblock")
        self.datafile_content = ''.join(self.__get_block_from_file())
        

    def __get_block_from_file(self):
        inside_block = False
        level = 0
        lines = []

        with open(self.src_file, 'r') as file:
            for line_number, line in enumerate(file, start=1):
                if self.block_start_regex.search(line):
                    if not level:
                        inside_block = True
                        lines.append(f"{line_number} {line}")
                    level += 1
                elif self.inner_level_regex and \
                        any(re.search(regex, line) for regex in self.inner_level_regex) and \
                        inside_block:
                    level += 1
                    lines.append(f"{line_number} {line}")
                elif self.block_end_regex.search(line):
                    if inside_block:
                        level -= 1
                        if level == 0:
                            inside_block = False
                            lines.append(f"{line_number} {line}\n")
                        else:
                            lines.append(f"{line_number} {line}")
                elif inside_block \
                and not self.block_start_regex.search(line) \
                and not self.block_end_regex.search(line):
                        lines.append(f"{line_number} {line}")
        return lines

    def touch_datafile(self):
        with open(self.datafile, 'w') as datafile:
            datafile.write(''.join(self.datafile_content))
            
