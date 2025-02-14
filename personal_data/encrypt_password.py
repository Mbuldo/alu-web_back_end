#!/usr/bin/env python3
"""
Module for securely hashing and validating passwords using bcrypt.
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hashes a password using bcrypt with automatic salting.

    Args:
        password (str): The plaintext password to hash.

    Returns:
        bytes: The salted, hashed password.
    """
    salt = bcrypt.gensalt()  # Generate a salt
    hashed = bcrypt.hashpw(password.encode(), salt)  # Hash password with salt
    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Validates that the provided password matches the hashed password.

    Args:
        hashed_password (bytes): The hashed password to validate against.
        password (str): The plaintext password to check.

    Returns:
        bool: True if the password matches the hashed password, False otherwise.
    """
    return bcrypt.checkpw(password.encode(), hashed_password)

