from gendiff.comparator import REMOVED, UPDATED, ADDED, EQUAL, DICT
from typing import Dict


templates = {
    ADDED: "Property '{}' was added with value: {}",
    REMOVED: "Property '{}' was removed",
    UPDATED: "Property '{}' was updated. From {} to {}"
}


def format_line(key: str, diff_type: str, first_value, second_value) -> str:
    if diff_type == ADDED:
        return templates[diff_type].format(key,
                                           format_value(first_value))
    elif diff_type == REMOVED:
        return templates[diff_type].format(key)
    elif diff_type == UPDATED:
        return templates[diff_type].format(key,
                                           format_value(first_value),
                                           format_value(second_value))
    raise Exception("wrong diff_type")


def format_value(value):
    if isinstance(value, (dict, list)):
        return "[complex value]"
    elif isinstance(value, str):
        return f"'{value}'"
    elif value is True:
        return "true"
    elif value is False:
        return "false"
    elif value is None:
        return "null"
    return value


def format(difference: Dict[str, list]) -> str:
    return to_plain_format(difference)


def to_plain_format(difference: Dict[str, list], path: str = '') -> str:
    result = []
    for key in sorted(difference.keys()):
        current_path = f'{path}.{key}' if path else key
        diff_type, first_value, second_value = difference[key]
        if diff_type == DICT:
            result.append(to_plain_format(first_value, current_path))
        elif diff_type != EQUAL:
            result.append(format_line(current_path, diff_type, first_value, second_value))
    return "\n".join(result)
