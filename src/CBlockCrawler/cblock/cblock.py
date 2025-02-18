import re

class CBlock:
    def __init__(self, block_id : int, src_file : str, start_line : int, end_line : int, func_inside, func_contain_block, block_lines : list):
        self.id = block_id
        self.src_file = src_file
        self.start_line = start_line
        self.end_line = end_line
        self.lines = "{}-{}".format(start_line, end_line)
        self.num_of_lines = end_line - start_line + 1
        self.func_inside = func_inside
        self.func_contain_block = func_contain_block
        self.block_lines = block_lines
        self.lines_covered = 0

    def get_record(self):
        func_inside_names = f"\"{',\n'.join(list(map(lambda x: x.name, self.func_inside)))}\""
        in_function_name = self.func_contain_block.name if self.func_contain_block else ''
        record = [self.src_file, self.id, self.lines, self.num_of_lines, func_inside_names, in_function_name]
        return record

    def get_block_coverage(self, coverage_file : str):
        with open(coverage_file, "r", encoding="utf-8") as f:
            lines = f.readlines()
        
        escaped_src_file = re.escape(self.src_file)
        start_pattern = r"^SF:.*" + escaped_src_file + r"$"
        da_pattern = r"DA:.*"
        end_pattern = r"^end_of_record$"
        
        inside_block = False
        for line in lines:
            if re.match(start_pattern, line):
                inside_block = True

            if inside_block and re.match(da_pattern,line):
                line_data = line[3:]
                line_num,exec_count = line_data.split(",")
                line_num = int(line_num)
                exec_count = int(exec_count)
                if self.start_line <= line_num and line_num <= self.end_line and exec_count > 0:
                    self.lines_covered += 1

            if inside_block and re.match(end_pattern, line): 
                break

        return round(float(self.lines_covered)/float(self.num_of_lines) * 100,1) 






            


            


