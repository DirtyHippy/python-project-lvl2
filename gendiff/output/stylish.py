from collections import OrderedDict


def format_value(value):
    if isinstance(value, str):
        return f"{value}"
    elif isinstance(value, bool):
        if value is True:
            return "true"
        else:
            return "false"
    elif value is None:
        return "null"
    return value


def format(difference: dict) -> str:
    return stringify(create_dict_format(difference))


def stringify(value, replacer='    ', spaces_count=1):
    def inner(inner_value, counter):
        result = ''
        if not isinstance(inner_value, dict):
            result = str(inner_value)
        else:
            result += "{\n"
            deep_size = spaces_count + counter
            for key, val in inner_value.items():
                temp = replacer * (deep_size - 1) + \
                    "{}: {}".format(key, inner(val, deep_size)) + "\n"
                if key.startswith("+") or key.startswith("-"):
                    temp = temp[2:]
                result += temp
            result += replacer * (counter - 1) + "}"
        return result
    return inner(value, 1)


def get_sorted_keys(difference: dict) -> list:
    list_keys = []
    for diff_value in difference.values():
        for key in diff_value.keys():
            list_keys.append(key)
    list_keys.sort()
    return list_keys


def create_dict_format(difference: dict) -> dict:  # noqa: C901
    result = OrderedDict()
    list_keys = get_sorted_keys(difference)
    for key in list_keys:
        prev = None
        counter = 0
        for el in key:
            counter += 1
            value = {}
            second_sigh, second_value = '', ''
            if counter == len(key):
                sign, value, second_sigh, second_value = get_sign_and_value(
                    difference, key)
                el2 = f"{second_sigh} {el}" if second_sigh != '' else f"{el}"
                el = f"{sign} {el}" if sign != '' else f"{el}"
                value = format_value(value)
                second_value = format_value(second_value)
            if prev is None:
                if el not in result:
                    result[el] = value
                    if second_sigh != '':
                        result[el2] = second_value  # type: ignore
                prev = result[el]
            else:
                if el not in prev:
                    prev[el] = value
                    if second_sigh != '':
                        prev[el2] = second_value
                prev = prev[el]
    return result


def get_sign_and_value(difference: dict, key: tuple) -> tuple:
    added = difference["added"]
    removed = difference["removed"]
    updated = difference["updated"]
    equal = difference["equal"]
    if key in added:
        return "+", added[key], '', ''
    elif key in removed:
        return "-", removed[key], '', ''
    elif key in updated:
        return "-", updated[key]["orig_value"], "+", updated[key]["new_value"]
    elif key in equal:
        return "", equal[key], '', ''
    else:
        raise Exception("wrong key")
