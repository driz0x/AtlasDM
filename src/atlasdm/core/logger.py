"""
Centralized logging for AtlasDM.
"""

import logging

from atlasdm.core.paths import PathManager


def get_logger(name: str) -> logging.Logger:
    """
    Return a configured Logger instance.

    Args:
        name: The name of the logger.

    Returns:
        A configured logging.Logger instance.
    """
    logger = logging.getLogger(name)

    if not logger.handlers:
        logger.setLevel(logging.DEBUG)

        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

        # Console handler
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        ch.setFormatter(formatter)
        logger.addHandler(ch)

        # File handler
        pm = PathManager()
        log_file = pm.logs_dir / "application.log"
        try:
            fh = logging.FileHandler(log_file, encoding="utf-8")
            fh.setLevel(logging.DEBUG)
            fh.setFormatter(formatter)
            logger.addHandler(fh)
        except OSError:
            # Logging to file is unavailable.
            # Console logging remains active.
            pass

    return logger
