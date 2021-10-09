from gendiff.core.comparator import format_value


def stringify(difference: dict) -> str:  # noqa: C901
    result = []
    for diff_key, diff_value in difference.items():
        for key, val in diff_value.items():
            line = ''
            key = key.replace("][", '.').replace("]", "").replace("[", "")
            if diff_key == "added":
                line = f"'{key}' was {diff_key} with value: {format_value(val)}"
            elif diff_key == "removed":
                line = f"'{key}' was {diff_key}"
            elif diff_key == 'updated':
                orig = format_value(val['orig_value'])
                new = format_value(val['new_value'])
                line = f"'{key}' was {diff_key}. From {orig} to {new}"
            if line:
                result.append(line)
            result.sort()
    result = map(lambda line: 'Property ' + line, result)
    return '\n'.join(result)
