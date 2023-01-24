from .stylish import format_stylish


def format_diff(diff, formatter):
    if formatter == 'stylish':
        return format_stylish(diff)
