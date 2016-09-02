import logging


def setup_loggers(*loggers):
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(formatter)

    for logger in loggers:
        logger.setLevel(logging.DEBUG)
        logger.addHandler(console_handler)
