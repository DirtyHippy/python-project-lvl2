from typing import Dict


REMOVED = 'removed'
UPDATED = 'updated'
ADDED = 'added'
EQUAL = 'equal'


def compare_dictionaries(dict_1: dict,  # noqa: C901
                         dict_2: dict,
                         ) -> Dict[str, dict]:

    result = {REMOVED: {}, UPDATED: {}, ADDED: {}, EQUAL: {}}

    def inner(dict_1, dict_2, path=()):
        orig_path = path
        for k in dict_1.keys():
            path = orig_path + (k,)
            if k not in dict_2:
                result[REMOVED][path] = dict_1[k]
            else:
                if isinstance(dict_1[k], dict) and isinstance(dict_2[k], dict):
                    inner(dict_1[k], dict_2[k], path)
                else:
                    if dict_1[k] != dict_2[k]:
                        result[UPDATED][path] = {'orig_value': dict_1[k],
                                                 'new_value': dict_2[k]}
                    else:
                        result[EQUAL][path] = dict_1[k]
        for k in dict_2.keys():
            path = orig_path + (k,)
            if k not in dict_1:
                result[ADDED][path] = dict_2[k]
        return result
    return inner(dict_1, dict_2)
