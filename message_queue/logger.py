import logging
import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    '-d', '--debug',
    help='Debug',
    action='store_const',
    dest='loglevel',
    const=logging.DEBUG,
    default=logging.WARNING,
)
args = parser.parse_args()

def get(name):
    """Get logger
    """
    logger    = logging.getLogger(__name__)
    handler   = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    handler.setFormatter(formatter)

    logger.addHandler(handler)
    logger.setLevel(args.loglevel)

    return logger

