import logging

from my_logging import my_logger


def main():
    # logging.basicConfig(filename='log/test.log', level=logging.DEBUG)
    # logging.critical('critical')
    # logging.error('error')
    # logging.warning('warning')
    # logging.info('info')
    # logging.debug('debug')
    # logging.info('info %s %s' % ('test', 'test2'))

    # formatter = '%(levelname)s: %(asctime)s %(message)s'
    # logging.basicConfig(level=logging.INFO, format=formatter)
    #
    # logging.info('info %s %s' % ('test', 'test2'))

    # logging.basicConfig(level=logging.INFO)
    # logger = logging.getLogger(__name__)
    # logger.setLevel(logging.DEBUG)
    # logger.debug('debug')
    # logging.debug('logging debug')

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    logger.info('from main')

    my_logger.main()
