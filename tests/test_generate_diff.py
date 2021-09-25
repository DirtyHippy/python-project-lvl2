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


plain_json1 = get_fixture_path('plain1.json')
plain_json2 = get_fixture_path('plain2.json')
plain_yml1 = get_fixture_path('plain1.yml')
plain_yml2 = get_fixture_path('plain2.yml')
plain_expected_value = read(get_fixture_path('plain.txt'))


nested_json1 = get_fixture_path('nested1.json')
nested_json2 = get_fixture_path('nested2.json')
nested_yml1 = get_fixture_path('nested1.yaml')
nested_yml2 = get_fixture_path('nested2.yaml')
nested_expected_value = read(get_fixture_path('nested.txt'))


@pytest.mark.parametrize("file1, file2", [(plain_json1, plain_json2),
                                          (plain_yml1, plain_yml2)])
def test_plain(file1, file2):
    assert plain_expected_value == generate_diff(file1, file2)


'''
@pytest.mark.parametrize("file1, file2", [(nested_json1, nested_json2),
                                          (nested_yml1, nested_yml2)])
def test_nested(file1, file2):
    assert nested_expected_value == generate_diff(file1, file2)
'''
