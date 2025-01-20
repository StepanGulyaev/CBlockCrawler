

class CBlock:
    def __init__(self, block_id : int, src_file : str, start_line : int, end_line : int, func_inside : list, func_contain_block : str, block_text : list ):
        self.block_id = block_id
        self.src_file = src_file
        self.start_line = start_line
        self.end_line = end_line
        self.lines = "{}-{}".format(start_line, end_line)
        self.num_of_lines = end_line - start_line + 1
        self.func_inside = func_inside
        self.func_contain_block = func_contain_block
        self.block_text = block_text
