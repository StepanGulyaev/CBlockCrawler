import argparse
import os
from CBlockCrawler.regex import validate_regex

def validate_path(path : str):
    if not os.path.exists(path):
        raise argparse.ArgumentTypeError(f"Path '{path}' doesn't exist")
    return path

def parse_main_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('-p',
                        '--project-root',
                        type=validate_path, 
                        required=True, 
                        help="Root diriectory of a project where source files will be searched in")
    parser.add_argument('-s',
                        '--block-start-regex', 
                        type=validate_regex,
                        required=True,
                        help="Regex to recognize the start of an extracted code block") 
    parser.add_argument('-i',
                        '--inner-level-regex', 
                        type=validate_regex,
                        nargs='*',
                        help="Regex used when inner blocks which have different start have the same ending as the start one.\
                                For example preprocessor conditions may differ from start-regex but they all end with #endif. \
                                If it happens and you didnt't specify inner-level regex, your block will be cut on inner #endif \
                                instead of #endif of your block. Please consider that")
    parser.add_argument('-e',
                        '--block-end-regex', 
                        type=validate_regex,
                        required=True,
                        help="Regex to recognize the end of an extracted code block") 
    parser.add_argument('-n',
                        '--report-name', 
                        type=str,
                        required=False,
                        default='cblock_report',
                        help="Cblock report file name")
    parser.add_argument('-f',
                        '--format',
                        type=str,
                        choices=['txt','csv', 'html'],
                        default='txt', 
                        help="Cblock report format") 
    parser.add_argument('-S',
                        '--save-tmp-files',
                        action="store_true",
                        default=False, 
                        help="Save tmp files for debug purposes")  
    parser.add_argument('-c',
                        '--coverage-file', 
                        type=validate_path,
                        required=False,
                        help="Coverage.info file produced by llvm-cov export. Needed for block coverage calculation.")
    return parser.parse_args()



