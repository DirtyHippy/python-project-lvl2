from gendiff.output.stylish import create_dict_format
import json


def format(difference: dict) -> str:
    return json.dumps(create_dict_format(difference), indent=4, sort_keys=True)
