import os
import pytest
from gendiff.generator import PLAIN, STYLISH, generate_diff


def get_fixture_path(file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, 'fixtures/test2', file_name)


def read(file_path):
    with open(file_path, 'r') as f:
        result = f.read()
    return result


def nested_expected_value():
    return read(get_fixture_path('nested_stylish.txt'))


def nested_expected_value_plain_format():
    return read(get_fixture_path('nested_plain.txt'))


nested_json1 = get_fixture_path('nested1.json')
nested_json2 = get_fixture_path('nested2.json')
nested_yml1 = get_fixture_path('nested1.yml')
nested_yml2 = get_fixture_path('nested2.yml')


@ pytest.mark.parametrize("file1, file2, test_function, format", [(nested_json1, nested_json2, nested_expected_value, STYLISH),                # noqa E501
                                                                  (nested_yml1, nested_yml2, nested_expected_value, STYLISH),                  # noqa E501
                                                                  (nested_json1, nested_json2, nested_expected_value_plain_format, PLAIN),     # noqa E501
                                                                  (nested_yml1, nested_yml2, nested_expected_value_plain_format, PLAIN)])      # noqa E501
def test_generate_diff(file1, file2, test_function, format):
    assert test_function() == generate_diff(file1, file2, format)
