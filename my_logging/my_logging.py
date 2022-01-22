import logging.config

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

    # logging.basicConfig(level=logging.INFO)
    # logger = logging.getLogger(__name__)
    # logger.addFilter(NoPassFilter())
    #
    # logger.info('from main')
    # logger.info('from main password = test1')
    #
    # my_logger.main()

    # logging.config.fileConfig('my_logging/logging.ini')
    logging.config.dictConfig({
        'version': 1,
        'formatters': {
            'sampleFormatter': {
                'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
            }
        },
        'handlers': {
            'sampleHandlers': {
                'class': 'logging.StreamHandler',
                'formatter': 'sampleFormatter',
                'level': logging.DEBUG
            }
        },
        'root': {
            'handlers': ['sampleHandlers'],
            'level': logging.WARNING
        },
        'loggers': {
            'simpleExample': {
                'handlers': ['sampleHandlers'],
                'level': logging.DEBUG,
                'propagate': 0
            }
        }
    })

    # logger = logging.getLogger(__name__)
    logger = logging.getLogger('simpleExample')

    logger.debug('debug message')
    logger.info('info message')
    logger.warning('warning message')
    logger.error('error message')
    logger.critical('critical message')
