

class CBlock:
    def __init__(self, block_id : int, src_file : str, start_line : int, end_line : int, func_inside, func_contain_block, block_lines : list ):
        self.id = block_id
        self.src_file = src_file
        self.start_line = start_line
        self.end_line = end_line
        self.lines = "{}-{}".format(start_line, end_line)
        self.num_of_lines = end_line - start_line + 1
        self.func_inside = func_inside
        self.func_contain_block = func_contain_block
        self.block_lines = block_lines

    def get_record(self):
        func_inside_names = f"\"{',\n'.join(list(map(lambda x: x.name, self.func_inside)))}\""
        in_function_name = self.func_contain_block.name if self.func_contain_block else ''
        record = [self.src_file, self.id, self.lines, self.num_of_lines, func_inside_names, in_function_name]
        return record
