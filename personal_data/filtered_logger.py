#!/usr/bin/env python3
"""
Module for filtering sensitive information from log messages
"""
import re
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
