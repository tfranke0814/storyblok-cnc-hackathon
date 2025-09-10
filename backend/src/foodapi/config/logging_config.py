"""
Logging configuration for the Food API.

Currently, it is set to DEBUG level for detailed output. Change to INFO in production.
"""

import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

def get_logger(name: str) -> logging.Logger:
    """Create and return a logger with the specified name."""
    return logging.getLogger(name)