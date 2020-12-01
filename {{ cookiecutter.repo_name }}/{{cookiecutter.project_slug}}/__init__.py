import logging

class CustomFormatter(logging.Formatter):
    """Logging Formatter to add colors and count warning / errors"""
    cyan = "\x1b[36;21m"
    green = "\x1b[32;21m"
    yellow = "\x1b[33;21m"
    red = "\x1b[31;21m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    format = "{color}\x1B[1m[%(levelname)s]\x1b[0m %(asctime)s - \x1b[4m(%(filename)s:%(lineno)d)\x1b[0m %(name)s:\x1B[7m%(message)s\x1b[0m"

    FORMATS = {
        logging.DEBUG: format.format(color=cyan),
        logging.INFO: format.format(color=green),
        logging.WARNING: format.format(color=yellow),
        logging.ERROR: format.format(color=red),
        logging.CRITICAL: format.format(color=bold_red)
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# create console handler with a higher log level
ch = logging.StreamHandler()
#ch = logging.NullHandler()
ch.setLevel(logging.DEBUG)

ch.setFormatter(CustomFormatter())

logger.addHandler(ch)
