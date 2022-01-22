import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

h = logging.FileHandler('log/logtest.log')
logger.addHandler(h)


def main():
    logger.info('from logger')
    logger.debug('from debug')
