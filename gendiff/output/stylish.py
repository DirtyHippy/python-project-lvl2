import itertools
from gendiff.comparator import REMOVED, UPDATED, ADDED, EQUAL
from typing import Dict


signs = {
    EQUAL: '  ',
    ADDED: '+ ',
    REMOVED: '- ',
    UPDATED: '- '
}


def to_stylish_format(diff_dict: dict, replacer='    ', spaces_count=1) -> str:
    def inner(current_value, depth):
        if not isinstance(current_value, dict):
            return str(current_value)

        deep_indent_size = depth + spaces_count
        deep_indent = replacer * deep_indent_size
        current_indent = replacer * depth
        lines = []
        for key, val in current_value.items():
            line = f'{deep_indent}{key}: {inner(val, deep_indent_size)}'
            if key[:2] in signs.values():
                line = line[2:]
            lines.append(line)
        result = itertools.chain("{", lines, [current_indent + "}"])
        return '\n'.join(result)
    return inner(diff_dict, 0)


def format_key(key: str, diff_type: str) -> str:
    return f'{signs[diff_type]}{key}'


def format_value(value):
    if isinstance(value, str):
        return f"{value}"
    elif value is True:
        return "true"
    elif value is False:
        return "false"
    elif value is None:
        return "null"
    return value


def create_dict_from_diff(difference: Dict[str, list]) -> dict:
    result = {}
    for key in sorted(difference.keys()):
        diff_type, first_value, second_value = difference[key]
        if diff_type is None:
            result[key] = create_dict_from_diff(first_value)
        else:
            result[format_key(key, diff_type)] = format_value(first_value)
            if diff_type == UPDATED:
                result[format_key(key, ADDED)] = format_value(second_value)
    return result


def format(difference: Dict[str, list]) -> str:
    diff_dict = create_dict_from_diff(difference)
    return to_stylish_format(diff_dict)
