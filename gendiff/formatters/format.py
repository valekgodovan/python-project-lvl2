from .stylish import format_stylish
from .plain import format_plain


def format_diff(diff, formatter):
    if formatter == 'stylish':
        return format_stylish(diff)
    elif formatter == 'plain':
        return format_plain(diff)
