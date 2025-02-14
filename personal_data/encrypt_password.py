#!/usr/bin/env python3
"""
Module for securely hashing passwords using bcrypt.
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

