from gendiff.output.stylish import create_dict_format, stringify


def format(difference: dict) -> str:
    return stringify(create_dict_format(difference))
