from typing import Dict


REMOVED = 'removed'
UPDATED = 'updated'
ADDED = 'added'
EQUAL = 'equal'
DICT = 'dict'


def compare_dictionaries(dict_1: dict, dict_2: dict) -> Dict[str, list]:
    all_keys = (dict_1.keys() | dict_2.keys())
    diff_keys1 = (dict_1.keys() - dict_2.keys())
    diff_keys2 = (dict_2.keys() - dict_1.keys())
    result = {}
    for key in all_keys:
        orig_value = dict_1.get(key)
        new_value = dict_2.get(key)
        if key in diff_keys1:
            value = [REMOVED, orig_value, None]
        elif key in diff_keys2:
            value = [ADDED, new_value, None]
        elif isinstance(orig_value, dict) and isinstance(new_value, dict):
            value = [DICT, compare_dictionaries(orig_value, new_value), None]
        elif orig_value == new_value:
            value = [EQUAL, orig_value, None]
        else:
            value = [UPDATED, orig_value, new_value]
        result[key] = value
    return result
