"""Core module of dundie"""

from dundie.utils.log import get_logger

log = get_logger()

def load(filepath):
    try:
        lines = []
        with open(filepath) as file_:
            for line in file_:
                print(line)
                lines.append(line)
        return lines 
    except FileNotFoundError as e:
        print(f'File not found {e}')  