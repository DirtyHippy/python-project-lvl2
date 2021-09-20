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
plain_yaml1 = get_fixture_path('plain1.yml')
plain_yaml2 = get_fixture_path('plain2.yml')
plain_expected = get_fixture_path('nested_expected.txt')
plain_expected_value = read(plain_expected)


@pytest.mark.parametrize("file1, file2", [(plain_json1, plain_json2),
                                          (plain_yaml1, plain_yaml2)])
def test_plain(file1, file2):
    assert plain_expected_value == generate_diff(file1, file2)
