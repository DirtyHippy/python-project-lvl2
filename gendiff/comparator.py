from typing import Dict


REMOVED = 'removed'
UPDATED = 'updated'
ADDED = 'added'
EQUAL = 'equal'


def compare_dictionaries(dict_1: dict, dict_2: dict) -> Dict[str, list]:
    all_keys = (dict_1.keys() | dict_2.keys())
    keys1 = (dict_1.keys() - dict_2.keys())
    keys2 = (dict_2.keys() - dict_1.keys())
    result = {}
    for key in all_keys:
        orig_value = dict_1.get(key)
        new_value = dict_2.get(key)
        if key in keys1:
            value = [REMOVED, orig_value, None]
        elif key in keys2:
            value = [ADDED, new_value, None]
        elif isinstance(orig_value, dict) and isinstance(new_value, dict):
            value = [None, compare_dictionaries(orig_value, new_value), None]
        elif orig_value == new_value:
            value = [EQUAL, orig_value, None]
        else:
            value = [UPDATED, orig_value, new_value]
        result[key] = value
    return result
