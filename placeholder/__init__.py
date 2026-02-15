import argparse
import logging

import colorama
from colorama import Fore

__program_name__ = "placeholder"
__version__ = "0.0.0"  # version

import placeholder.mydefaults as mydefaults

mydefaults.create_logger(__program_name__)
log = logging.getLogger(__program_name__)


def command_entry_point():
    try:
        main()
    except KeyboardInterrupt:
        log.warning("Program was interrupted by user")


def main():
    parser = argparse.ArgumentParser(prog=__program_name__,
                                     description="Placeholder description",
                                     allow_abbrev=True, add_help=True, exit_on_error=True)

    parser.add_argument('-v', '--verbose', action='store_true', help="Show more output")
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")

    args = parser.parse_args()

    log.setLevel(logging.DEBUG if args.verbose else logging.INFO)
    log.debug(f"Starting {__program_name__}...")
