## Folder: utils
# File: helpers.py

import os
import logging
from datetime import datetime
from typing import Any

# --- Logging Setup ---
def setup_logger(name: str = "AutoGitLogger", level: int = logging.INFO) -> logging.Logger:
    logger = logging.getLogger(name)
    if not logger.hasHandlers():
        logger.setLevel(level)
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        handler = logging.StreamHandler()
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    return logger

logger = setup_logger()


# --- Safe File Reader ---
def read_file(path: str) -> str:
    if not os.path.exists(path):
        logger.error(f"File not found: {path}")
        return ""
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        logger.exception(f"Failed to read file {path}")
        return ""


# --- Safe File Writer ---
def write_file(path: str, content: str) -> bool:
    try:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    except Exception as e:
        logger.exception(f"Failed to write to file {path}")
        return False


# --- Date Formatter ---
def format_date(dt: datetime = None) -> str:
    dt = dt or datetime.now()
    return dt.strftime("%Y-%m-%d %H:%M:%S")


# --- General Safe Executor ---
def try_execute(func, *args, **kwargs) -> Any:
    try:
        return func(*args, **kwargs)
    except Exception as e:
        logger.exception(f"Error executing function {func.__name__}")
        return None
