import json


def to_str(val):
    if isinstance(val, dict):
        return '[complex value]'
    if isinstance(val, bool) or val is None:
        return json.dumps(val)
    if isinstance(val, str):
        return f"'{val}'"
    return val


def iter_(data, path=''):
    result_list = []
    for key, node in data.items():
        node_type = node.get('type')
        node_children = node.get('children')
        node_value = node.get('value')
        node_old_value = node.get('value_1')
        node_new_value = node.get('value_2')
        if node_type == 'added':
            result_list.append(
                f'Property \'{path + key}\' '
                f'was added with value: {to_str(node_value)}'
            )
        if node_type == 'removed':
            result_list.append(
                f'Property \'{path + key}\' was removed'
            )
        if node_type == 'changed':
            result_list.append(
                f'Property \'{path + key}\' was updated. '
                f'From {to_str(node_old_value)} to {to_str(node_new_value)}'
            )
        if node_type == 'nested':
            new_path = f'{path}{key}.'
            result_list.append(iter_(node_children, new_path))
    return '\n'.join(result_list)


def format_plain(diff_tree):
    return iter_(diff_tree)
