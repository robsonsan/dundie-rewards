import argparse
from dundie.core import load

def main():
    parser = argparse.ArgumentParser(
        description='Dunder Mifflin Rewards CLI'   
    )
    parser.add_argument(
        'subcommand',
        type=str,
        help='The subcommand to run',
        choices=('load', 'show', 'send'),
        
    )   
    parser.add_argument(
        'filepath',
        type=str,
        help='File path to load',
        
    ) 
    args = parser.parse_args()
    try:
        globals()[args.subcommand](args.filepath)
    except KeyError:
        print('Subcommand is invalid')