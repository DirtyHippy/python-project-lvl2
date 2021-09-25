REMOVED = 'removed'
UPDATED = 'updated'
ADDED = 'added'
EQUAL = 'equal'

result = {}


def compare_dictionaries(dict_1: dict,  # noqa: C901
                         dict_2: dict,
                         path="") -> dict:
    orig_path = path
    for k in dict_1.keys():
        path = orig_path + f"[{k}]"
        if k not in dict_2:
            result.setdefault(REMOVED, dict())[path] = dict_1[k]
        else:
            if isinstance(dict_1[k], dict) and isinstance(dict_2[k], dict):
                compare_dictionaries(dict_1[k], dict_2[k], path)
            else:
                if dict_1[k] != dict_2[k]:
                    result.setdefault(UPDATED, dict())[path] = {
                        'orig_value': dict_1[k], 'new_value': dict_2[k]}
                else:
                    result.setdefault(EQUAL, dict())[path] = dict_1[k]
    for k in dict_2.keys():
        path = orig_path + f"{k}"
        if k not in dict_1:
            result.setdefault(ADDED, dict())[path] = dict_2[k]
    return result
