import re
import argparse

def validate_regex( regex : str):
    try:
        compiled_regex = re.compile(regex)
        return compiled_regex
    except re.error:
        raise argparse.ArgumentTypeError(f"Incorrect regular expression: {regex}")


