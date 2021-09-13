from gendiff.scripts.gendiff import generate_diff
import os


def test_generate_diff():
    tests_dir = os.path.dirname(os.path.realpath(__file__))
    with open(tests_dir + "/fixtures/test1.txt", "r") as test1:
        assert generate_diff(
            tests_dir + "/fixtures/file1.json",
            tests_dir + "/fixtures/file2.json",
        ) == test1.read()
