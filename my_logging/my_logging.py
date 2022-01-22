import logging


def main():
    # logging.basicConfig(filename='log/test.log', level=logging.DEBUG)
    # logging.critical('critical')
    # logging.error('error')
    # logging.warning('warning')
    # logging.info('info')
    # logging.debug('debug')
    # logging.info('info %s %s' % ('test', 'test2'))

    formatter = '%(levelname)s: %(asctime)s %(message)s'
    logging.basicConfig(level=logging.INFO, format=formatter)

    logging.info('info %s %s' % ('test', 'test2'))
