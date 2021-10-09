from typing import Dict


REMOVED = 'removed'
UPDATED = 'updated'
ADDED = 'added'
EQUAL = 'equal'

result: Dict[str, dict]
result = {REMOVED: {}, UPDATED: {}, ADDED: {}, EQUAL: {}}


def format_value(value):
    if isinstance(value, dict):
        return "[complex value]"
    elif isinstance(value, str):
        return f"'{value}'"
    elif isinstance(value, bool):
        if value is True:
            return "true"
        else:
            return "false"
    elif value is None:
        return "null"
    return value


def compare_dictionaries(dict_1: dict,  # noqa: C901
                         dict_2: dict,
                         path="") -> Dict[str, dict]:
    orig_path = path
    for k in dict_1.keys():
        path = orig_path + f"[{k}]"
        if k not in dict_2:
            result[REMOVED][path] = dict_1[k]
        else:
            if isinstance(dict_1[k], dict) and isinstance(dict_2[k], dict):
                compare_dictionaries(dict_1[k], dict_2[k], path)
            else:
                if dict_1[k] != dict_2[k]:
                    result[UPDATED][path] = {'orig_value': dict_1[k],
                                             'new_value': dict_2[k]}
                else:
                    result[EQUAL][path] = dict_1[k]
    for k in dict_2.keys():
        path = orig_path + f"[{k}]"
        if k not in dict_1:
            result[ADDED][path] = dict_2[k]
    return result
