#!/usr/bin/env python3
"""
Module for filtering sensitive information from log messages
"""
import re
import logging
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    Obfuscates specified fields in a log message.

    Args:
        fields: List of strings representing fields to obfuscate
        redaction: String to replace sensitive information with
        message: Log line to process
        separator: Character separating fields in log line

    Returns:
        Log message with specified fields obfuscated
    """
    pattern = f'({"|".join(fields)})=[^{separator}]*'
    return re.sub(pattern, f'\\1={redaction}', message)


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Format log records while redacting sensitive fields.

        Args:
            record: LogRecord instance containing log information

        Returns:
            Formatted log string with sensitive information redacted
        """
        record.msg = filter_datum(self.fields, self.REDACTION,
                                record.getMessage(), self.SEPARATOR)
        return super(RedactingFormatter, self).format(record)
