import logging

class Logger():
    
    def getLogger(self, name, level, formatter):
        logger = logging.getLogger(name)
        consoleHandler = logging.StreamHandler()
        consoleHandler.setFormatter(logging.Formatter(formatter))
        if len(logger.handlers) > 0:
            logger.handlers = []
        logger.addHandler(consoleHandler)
        logger.setLevel(level)
        logger.propagate = False
        return logger