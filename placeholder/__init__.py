import argparse
import logging

import colorama
from colorama import Fore

__program_name__ = "placeholder"
__version__ = "0.0.0"  # version

log = logging.getLogger(__program_name__)
console = logging.StreamHandler()
log.addHandler(console)
log.setLevel(logging.DEBUG)
console.setFormatter(
    logging.Formatter(
        f"{{asctime}} [{Fore.YELLOW}{{levelname:>5}}{Fore.RESET}] {Fore.BLUE}{{name}}{Fore.RESET}: {{message}}",
        style="{", datefmt="%W %a %I:%M"))


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
