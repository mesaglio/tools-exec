import logging
import sys

FORMAT = '%(asctime)s - pid:%(process)d - tid:%(thread)d - %(levelname)-8s - %(message)s'

def logger(name: str) -> logging.Logger:
    log = logging.getLogger(name)
    log.setLevel(logging.DEBUG)

    fh = logging.StreamHandler(sys.stdout)
    fh.setLevel(logging.DEBUG)

    log_formatter = logging.Formatter(FORMAT)
    fh.setFormatter(log_formatter)

    log.addHandler(fh)
    return log