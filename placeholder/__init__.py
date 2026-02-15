import logging
from argparse import ArgumentParser

import colorama
import mydefaults
from colorama import Fore

mydefaults.create_logger(__package__)
log = logging.getLogger(__package__)


@mydefaults.command(version="0.0.0")
def placeholder(parser: ArgumentParser): #TODO
    """Placeholder description""" # TODO

    args = parser.parse_args()

    log.setLevel(logging.DEBUG if args.verbose else logging.INFO)
    log.debug(f"Starting {parser.prog}...")
