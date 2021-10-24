from gendiff.generator import generate_diff
import os
import pytest


def get_fixture_path(file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, 'fixtures/test2', file_name)


def read(file_path):
    with open(file_path, 'r') as f:
        result = f.read()
    return result


nested_json1 = get_fixture_path('nested1.json')
nested_json2 = get_fixture_path('nested2.json')
nested_yml1 = get_fixture_path('nested1.yml')
nested_yml2 = get_fixture_path('nested2.yml')
nested_expected_value = read(get_fixture_path('nested_stylish.txt'))
nested_expected_value_plain_format = read(get_fixture_path('nested_plain.txt'))


@pytest.mark.parametrize("file1, file2", [(nested_json1, nested_json2),
                                          (nested_yml1, nested_yml2)])
def test_nested(file1, file2):
    assert nested_expected_value == generate_diff(file1, file2)


@pytest.mark.parametrize("file1, file2", [(nested_json1, nested_json2),
                                          (nested_yml1, nested_yml2)])
def test_nested_plain_format(file1, file2):
    assert nested_expected_value_plain_format == generate_diff(
        file1, file2, 'plain')
