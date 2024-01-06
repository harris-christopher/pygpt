import argparse
from pathlib import Path

from dotenv import load_dotenv

from pygpt.pygpt import PyGPT


def run():
    args = get_args()
    pygpt = PyGPT(args.infile, args.outfile, args.start, args.end)
    pygpt.process_file()


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-in",
        "--infile",
        help="Input file to be translated (line by line)",
        dest="infile",
        type=Path,
        required=True,
    )
    parser.add_argument(
        "-ls",
        "--line_start",
        help="Line number with which to start processing (inclusive)",
        dest="start",
        type=int,
        default=0,
        required=False,
    )
    parser.add_argument(
        "-out",
        "--outfile",
        help="Output file to store translated text",
        type=Path,
        dest="outfile",
        required=True,
    )
    parser.add_argument(
        "-le",
        "--line_end",
        help="Line number with which to stop processing (exclusive)",
        dest="end",
        type=int,
        required=False,
    )

    return parser.parse_args()


if __name__ == "__main__":
    load_dotenv()
    run()
