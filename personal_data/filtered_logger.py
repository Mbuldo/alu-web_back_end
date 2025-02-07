#!/usr/bin/env python3
"""
Module for filtering sensitive information from log messages
"""
import re
import os
import logging
import mysql.connector
from typing import List


PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


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


def get_logger() -> logging.Logger:
    """
    Creates a logger with specific configuration.

    Returns:
        logging.Logger: Configured logger object
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.addHandler(handler)

    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """
    Connect to MySQL database using credentials from environment.

    Returns:
        MySQLConnection: Database connection object
    """
    username = os.getenv('PERSONAL_DATA_DB_USERNAME', 'root')
    password = os.getenv('PERSONAL_DATA_DB_PASSWORD', '')
    host = os.getenv('PERSONAL_DATA_DB_HOST', 'localhost')
    db_name = os.getenv('PERSONAL_DATA_DB_NAME')

    return mysql.connector.connect(
        user=username,
        password=password,
        host=host,
        database=db_name
    )


def main() -> None:
    """
    Retrieve and display filtered user data from database.
    """
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users;")
    
    logger = get_logger()
    fields = cursor.column_names

    for row in cursor:
        record = '; '.join(
            f"{fields[i]}={row[i]}" for i in range(len(fields))
        )
        logger.info(record)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
