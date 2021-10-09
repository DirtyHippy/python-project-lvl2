from gendiff.scripts.gendiff import generate_diff
import os
import pytest


def get_fixture_path(file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, 'fixtures', file_name)


def read(file_path):
    with open(file_path, 'r') as f:
        result = f.read()
    return result


simple_json1 = get_fixture_path('simple1.json')
simple_json2 = get_fixture_path('simple2.json')
simple_yml1 = get_fixture_path('simple1.yml')
simple_yml2 = get_fixture_path('simple2.yml')
simple_expected_value = read(get_fixture_path('simple.txt'))


nested_json1 = get_fixture_path('nested1.json')
nested_json2 = get_fixture_path('nested2.json')
nested_yml1 = get_fixture_path('nested1.yaml')
nested_yml2 = get_fixture_path('nested2.yaml')
nested_expected_value = read(get_fixture_path('nested.txt'))
nested_expected_value_plain_format = read(get_fixture_path('nested_plain.txt'))


@pytest.mark.parametrize("file1, file2", [(simple_json1, simple_json2),
                                          (simple_yml1, simple_yml2)])
def test_plain(file1, file2):
    assert simple_expected_value == generate_diff(file1, file2)


@pytest.mark.parametrize("file1, file2", [(nested_json1, nested_json2),
                                          (nested_yml1, nested_yml2)])
def test_nested(file1, file2):
    assert nested_expected_value == generate_diff(file1, file2)


@pytest.mark.parametrize("file1, file2", [(nested_json1, nested_json2),
                                          (nested_yml1, nested_yml2)])
def test_nested_plain_format(file1, file2):
    assert nested_expected_value_plain_format == generate_diff(
        file1, file2, 'plain')
