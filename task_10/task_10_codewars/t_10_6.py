import re

def class_rename(cls, new_name):
    if not re.match(r'^[A-Z][A-Za-z0-9]*$', new_name):
        raise ValueError("Invalid class name. Must start with uppercase letter and contain only alphanumeric characters.")
    cls.__name__ = new_name
    return cls
