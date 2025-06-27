import string
import random
import base64
import hashlib
import hmac
from enum import Enum
from typing import TypeVar

T = TypeVar("T")


def action(path, method="POST"):

    def decorator(function: T) -> T:
        def wrapper(*args, **kwargs):
            kwargs.update({"path": path, "method": method})
            return function(*args, **kwargs)

        wrapper.__doc__ = function.__doc__
        return wrapper

    return decorator
