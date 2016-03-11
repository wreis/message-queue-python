import logging
import argparse


def get(name):
    """Get logger

    :param string name: Name of the file

    """
    logger  = logging.getLogger(name)
    handler = logging.StreamHandler()

    handler.setFormatter(
        logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    )

    logger.addHandler(handler)
    logger.setLevel(args.loglevel)

    return logger


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

