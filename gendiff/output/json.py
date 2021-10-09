import itertools


def format(difference: dict, indent=' ', indent_count=1) -> str:
    lines = []
    for _, diff_value in difference.items():
        for key, val in diff_value.items():
            lines.append(f'{key}: {val}')
    result = itertools.chain("{", lines, "}")
    return '\n'.join(result)
