import logging

class ColoredFormatter(logging.Formatter):
    grey = "\033[90m"      
    blue = "\033[94m"
    yellow = "\033[93m"
    red = "\033[91m"
    bold_red = "\033[91;1m"
    reset = "\033[0m"

    FORMATS = {
        logging.DEBUG: grey,
        logging.INFO: blue,
        logging.WARNING: yellow,
        logging.ERROR: red,
    }

    def format(self, record):
        color = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(
            f'{color}%(asctime)s - [%(pathname)s:%(lineno)d] - %(levelname)s - %(message)s{self.reset}'
        )
        return formatter.format(record)

class Logger:
    def __init__(self, name='default'):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        
        colored_formatter = ColoredFormatter()
        console_handler.setFormatter(colored_formatter)
        
        self.logger.addHandler(console_handler)
    
    def debug(self, message):
        self.logger.debug(message)
    
    def info(self, message):
        self.logger.info(message)
    
    def warning(self, message):
        self.logger.warning(message)
    
    def error(self, message):
        self.logger.error(message)
