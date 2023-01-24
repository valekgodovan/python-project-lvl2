def build_diff(dict_1: dict, dict_2: dict) -> dict:
    tree = {}
    for key in sorted({**dict_1, **dict_2}):
        if isinstance(dict_1.get(key), dict) \
                and isinstance(dict_2.get(key), dict):
            node = {
                'type': 'nested',
                'children': build_diff(dict_1.get(key), dict_2.get(key)),
            }
            tree[key] = node
        else:
            if key in dict_1 and key not in dict_2:
                node = {
                    'type': 'removed',
                    'value': dict_1.get(key),
                }
                tree[key] = node
            elif key not in dict_1 and key in dict_2:
                node = {
                    'type': 'added',
                    'value': dict_2.get(key),
                }
                tree[key] = node
            elif dict_1.get(key) == dict_2.get(key):
                node = {
                    'type': 'unchanged',
                    'value': dict_1.get(key),
                }
                tree[key] = node
            else:
                node = {
                    'type': 'changed',
                    'value_1': dict_1.get(key),
                    'value_2': dict_2.get(key),
                }
                tree[key] = node
    return tree
