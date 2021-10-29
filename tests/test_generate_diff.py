import os
import pytest
from gendiff.generator import PLAIN, STYLISH, generate_diff


def get_fixture_path(file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, 'fixtures/', file_name)


def read(file_path):
    with open(file_path, 'r') as f:
        result = f.read()
    return result


def simple_expected_value(test_path: str):
    return read(get_fixture_path(f'{test_path}simple_stylish.txt'))


def nested_expected_value(test_path: str):
    return read(get_fixture_path(f'{test_path}nested_stylish.txt'))


def nested_expected_value_plain_format(test_path: str):
    return read(get_fixture_path(f'{test_path}nested_plain.txt'))


simple_json1 = 'simple1.json'
simple_json2 = 'simple2.json'
simple_yml1 = 'simple1.yml'
simple_yml2 = 'simple2.yml'


nested_json1 = 'nested1.json'
nested_json2 = 'nested2.json'
nested_yml1 = 'nested1.yaml'
nested_yml2 = 'nested2.yaml'

test1_path = 'test1/'
test2_path = 'test2/'


@ pytest.mark.parametrize("file1, file2, test_path, test_function, format", [
                            (simple_json1, simple_json2, test1_path, simple_expected_value, STYLISH),              # noqa E501
                            (simple_yml1, simple_yml2, test1_path, simple_expected_value, STYLISH),                # noqa E501
                            (nested_json1, nested_json2, test1_path, nested_expected_value, STYLISH),              # noqa E501
                            (nested_yml1, nested_yml2, test1_path, nested_expected_value, STYLISH),                # noqa E501
                            (nested_json1, nested_json2, test1_path, nested_expected_value_plain_format, PLAIN),   # noqa E501
                            (nested_yml1, nested_yml2, test1_path, nested_expected_value_plain_format, PLAIN),     # noqa E501
                            (nested_json1, nested_json2, test2_path, nested_expected_value, STYLISH),              # noqa E501
                            (nested_yml1, nested_yml2, test2_path, nested_expected_value, STYLISH),                # noqa E501
                            (nested_json1, nested_json2, test2_path, nested_expected_value_plain_format, PLAIN),   # noqa E501
                            (nested_yml1, nested_yml2, test2_path, nested_expected_value_plain_format, PLAIN)])    # noqa E501
def test_generate_diff(file1, file2, test_path, test_function, format):
    assert test_function(test_path) == generate_diff(get_fixture_path(test_path + file1),
                                                     get_fixture_path(test_path + file2),
                                                     format)
