import itertools
from gendiff.comparator import REMOVED, UPDATED, ADDED, EQUAL, DICT
from typing import Dict


signs = {
    EQUAL: '  ',
    ADDED: '+ ',
    REMOVED: '- ',
    UPDATED: '- '
}

indent = '    '
indent_sign = '  '


def format_dict(dict_value: dict, depth: int) -> str:
    lines = []
    for key, value in dict_value.items():
        lines.append(format_line(key, EQUAL, format_value(value, depth + 1), depth))
    result = itertools.chain("{", lines, [indent * depth + "}"])
    return '\n'.join(result)


def format_line(key: str, diff_type: str, value, depth: int) -> str:
    return f"{indent * depth}{indent_sign}{signs[diff_type]}{key}: {value}"


def format_value(value, depth: int):
    if isinstance(value, str):
        return f"{value}"
    elif value is True:
        return "true"
    elif value is False:
        return "false"
    elif value is None:
        return "null"
    elif isinstance(value, dict):
        return format_dict(value, depth)
    return value


def to_stylish_format(difference: Dict[str, list], depth: int = 0) -> str:
    lines = []
    for key in sorted(difference.keys()):
        diff_type, first_value, second_value = difference[key]
        if diff_type == DICT:
            lines.append(format_line(key, EQUAL, to_stylish_format(first_value, depth + 1), depth))
        else:
            dict_depth = depth + 1 if isinstance(first_value, dict) else depth
            lines.append(format_line(key, diff_type, format_value(first_value, dict_depth), depth))
            if diff_type == UPDATED:
                dict_depth = depth + 1 if isinstance(second_value, dict) else depth
                lines.append(format_line(key, ADDED, format_value(second_value, dict_depth), depth))
    result = itertools.chain("{", lines, [indent * depth + "}"])
    return '\n'.join(result)


def format(difference: Dict[str, list]) -> str:
    return to_stylish_format(difference)
