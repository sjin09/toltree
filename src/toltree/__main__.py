#!/usr/bin/env python3

# modules
import sys

import toltree.treelib
from toltree.parse_args import create_argument_parser


def main(arguments=sys.argv[1:]) -> int:
    parser = create_argument_parser()

    if len(arguments) == 0:
        parser.print_help()
        parser.exit()

    options = parser.parse_args(arguments)
    toltree.treelib.build_tree(
        options.input,  # Darwin Tree of Life sample spread sheet with taxonomic ranking
        options.output  # file to return phylogentic tree
    )
    return 0


if __name__ == "__main__":
    exit_code = main()
    print("Exiting toltree")
    sys.exit(exit_code)
