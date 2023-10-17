import logging
from utils import ensure_dir


def setup_logging(log_config="logging_config.ini"):
    """
    Setup logging configuration
    """
    ensure_dir("logs")

    logging.config.fileConfig(log_config)
