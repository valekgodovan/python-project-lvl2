import json
import itertools


def to_str(value):
    if isinstance(value, bool) or value is None:
        return json.dumps(value)
    return value


def iter_(data, depth=0, replacer=' ', spaces_count=4):
    char = {
        'added': '+ ',
        'removed': '- ',
        'unchanged': '  ',
    }

    if not isinstance(data, dict):
        return str(data)

    deep_indent_next = depth + spaces_count
    deep_indent = replacer * deep_indent_next
    current_indent = replacer * depth
    lines = []

    for key, node in data.items():
        if isinstance(node, dict) and "type" in node:
            if node.get("type") == 'changed':
                lines.append(
                    f'{deep_indent[2:]}{char["removed"]}{key}:'
                    f' {iter_(to_str(node.get("value_1")), deep_indent_next)}'
                )
                lines.append(
                    f'{deep_indent[2:]}{char["added"]}{key}: '
                    f'{iter_(to_str(node.get("value_2")), deep_indent_next)}'
                )
            elif node.get("type") == 'nested':
                lines.append(
                    f'{deep_indent}{key}: '
                    f'{iter_(to_str(node.get("children")), deep_indent_next)}'
                )
            else:
                lines.append(
                    f'{deep_indent[2:]}{char[node.get("type")]}{key}: '
                    f'{iter_(to_str(node.get("value")), deep_indent_next)}'
                )
        else:
            lines.append(
                f'{deep_indent}{key}: '
                f'{iter_(to_str(node), deep_indent_next)}'
            )

    result = itertools.chain("{", lines, [current_indent + "}"])
    return '\n'.join(result)


def format_stylish(diff_tree):
    return iter_(diff_tree)
