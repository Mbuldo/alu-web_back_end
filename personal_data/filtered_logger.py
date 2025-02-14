#!/usr/bin/env python3
"""
Module for logging user data while redacting sensitive information.
"""

import logging
import re
from typing import List

# Define the PII fields to be redacted
PII_FIELDS = ("name", "email", "phone", "ssn", "password")


class RedactingFormatter(logging.Formatter):
    """Redacts sensitive PII fields in log messages."""

    REDACTION = "***"
    FORMAT = "[USER_DATA] %(levelname)s %(name)s: %(message)s"
    SEPARATOR = "; "

    def __init__(self, fields: List[str]):
        """Initialize formatter with PII fields."""
        super().__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Redacts sensitive fields before formatting log messages."""
        record.msg = self.filter_message(record.msg)
        return super().format(record)

    def filter_message(self, message: str) -> str:
        """Redact PII fields in the message."""
        for field in self.fields:
            message = re.sub(rf"{field}=[^;]+", f"{field}={self.REDACTION}", message)
        return message


def get_logger() -> logging.Logger:
    """Creates and returns a logger with a RedactingFormatter."""
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    # Create a StreamHandler with RedactingFormatter
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(RedactingFormatter(PII_FIELDS))

    logger.addHandler(stream_handler)
    return logger

