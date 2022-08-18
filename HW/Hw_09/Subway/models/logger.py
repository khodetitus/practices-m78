import logging

logger = logging.getLogger(__name__)
logger.setLevel(10)
f_handler = logging.FileHandler("metro.log")
f_handler.setLevel(logging.DEBUG)
f_format = logging.Formatter("%(asctime)s - %(name)-s - %(levelname)-s - %(message)s")
f_handler.setFormatter(f_format)
logger.addHandler(f_handler)


