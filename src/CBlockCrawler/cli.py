import argparse
from CBlockCrawler.regex import validate_regex

def parse_main_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('-p',
                        '--project-root',
                        type=str, 
                        required=True, 
                        help="Root diriectory of a project where source files will be searched in")
    parser.add_argument('-s','--block-start-regex', 
                        type=validate_regex,
                        required=True,
                        help="Regex to recognize the start of an extracted code block")
    parser.add_argument('-e','--block-end-regex', 
                        type=validate_regex,
                        required=True,
                        help="Regex to recognize the end of an extracted code block")
    parser.add_argument('-f',
                        '--format',
                        type=str,
                        choices=['txt','csv'],
                        default='txt', 
                        help="Output file format") 
    parser.add_argument('-S',
                        '--save-tmp-files',
                        action="store_true",
                        default=False, 
                        help="Save tmp files for debug purposes")

    return parser.parse_args()



