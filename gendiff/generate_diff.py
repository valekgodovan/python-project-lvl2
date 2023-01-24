from .internal_representation import build_diff
from .parser import get_content
from gendiff.formatters.format import format_diff


def generate_diff(file_path1, file_path2, format_name='stylish'):
    data1 = get_content(file_path1)
    data2 = get_content(file_path2)
    diff_tree = build_diff(data1, data2)
    return format_diff(diff_tree, format_name)
