import clang.cindex
from CBlockCrawler.funcs.src_function import Src_function

class Src_functions_handler:
    def __init__(self, src_file : str, libclang : str):
        self.src_file = src_file
        self.libclang = libclang
        self.functions = self.__get_functions()
    
    def __get_functions(self):
        index = clang.cindex.Index.create()
        translation_unit = index.parse(self.src_file,args=['--with-http_ssl_module'])
        functions = []

        for cursor in translation_unit.cursor.get_children():
            if cursor.kind == clang.cindex.CursorKind.FUNCTION_DECL and \
                    cursor.is_definition() \
                    and cursor.location.file.name == self.src_file:
                function_name = cursor.spelling
                start_line, end_line = cursor.extent.start.line, cursor.extent.end.line
                func = Src_function(self.src_file, function_name, start_line, end_line) 
                functions.append(func)
        return functions


