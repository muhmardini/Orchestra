import logging
import sys

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%D - %H:%M:%S",
    stream=sys.stdout
    )
logger = logging.getLogger("__name__")

logger.warning("the oven is hot")
logger.debug("The oven is working")
logger.critical("the oven is burning")
