import logging

from my_logging import my_logger


class NoPassFilter(logging.Filter):
    def filter(self, record):
        log_message = record.getMessage()
        return 'password' not in log_message


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
    logger.addFilter(NoPassFilter())

    logger.info('from main')
    logger.info('from main password = test1')

    my_logger.main()
