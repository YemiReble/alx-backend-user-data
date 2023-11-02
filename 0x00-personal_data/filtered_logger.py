#!/usr/bin/env python3
"""
A program that use re.sub to perform the
substitution with a single regex.python3
"""
import re
from typing import List


def filter_datum(fields: str, redaction: str, message: str, separator: str) -> List[str]:
    for field in fields:
        pattern = f"{field}=[^{separator}]*"
        message = re.sub(pattern, f"{field}={redaction}", message)
    return message
