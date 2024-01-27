import argparse
import warnings

from . import __version__


def make_wide(formatter, w=120, h=36):
    """Return a wider HelpFormatter, if possible."""
    try:
        # https://stackoverflow.com/a/5464440
        # beware: "Only the name of this class is considered a public API."
        kwargs = {"width": w, "max_help_position": h}
        formatter(None, **kwargs)
        return lambda prog: formatter(prog, **kwargs)
    except TypeError:
        warnings.warn("argparse help formatter failed, falling back.")
        return formatter


def create_argument_parser():
    # main_arguments
    parser = argparse.ArgumentParser(
        add_help=True,
        formatter_class=make_wide(argparse.ArgumentDefaultsHelpFormatter),
        description="This Python package is a command line tool for building phylogenetic trees"
        "from Darwin Tree of Life sample spread sheet.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="allow overwriting of output files. Note: some subcommands currently overwrite regardless of this flag.",
    )
    parser.add_argument(
        "-t",
        "--threads",
        type=int,
        default=1,
        required=False,
        help="number of threads to use",
    )
    parser.add_argument("--verbose", action="store_true", help="output DEBUG messages to log.")
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s {version}".format(version=__version__),
    )
    # subcommands: initialize
    # subparsers = parser.add_subparsers(dest="subcommand", required=True)
    # subcommands:
    return parser
