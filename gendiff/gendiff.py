import json
import yaml


def get_file(name_file: str) -> dict:
    if name_file.endswith('json'):
        with open(name_file, 'r') as stream:
            file = json.load(stream)
    elif name_file.endswith('yaml'):
        with open(name_file, 'r') as stream:
            file = yaml.safe_load(stream)
    return file


def generate_diff(path_to_file1: str, path_to_file2: str) -> str:
    file1_dict = get_file(path_to_file1)
    file2_dict = get_file(path_to_file2)
    keys = file1_dict.keys() | file2_dict.keys()
    merge_dict = {}
    result = {}
    for v in keys:
        merge_dict[v] = [file1_dict.get(v, []), file2_dict.get(v, [])]
    for i in sorted(merge_dict.keys()):
        if i not in file1_dict:
            result[f'+ {i}'] = file2_dict[i]
        elif i not in file2_dict:
            result[f'- {i}'] = file1_dict[i]
        elif file1_dict[i] == file2_dict[i]:
            result[f'  {i}'] = file1_dict[i]
        else:
            result[f'- {i}'] = file1_dict[i]
            result[f'+ {i}'] = file2_dict[i]
    file_json = json.dumps(result, indent=2)
    return file_json.translate({ord('"'): None, ord(','): None})
