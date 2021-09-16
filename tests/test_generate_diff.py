from gendiff.scripts.gendiff import generate_diff
import os


def test_generate_diff():
    test_dir = os.path.dirname(os.path.realpath(__file__))
    with open(test_dir + "/fixtures/test1.txt", "r") as test1:
        assert generate_diff(
            test_dir + "/fixtures/file1.json",
            test_dir + "/fixtures/file2.json",
        ) == test1.read()


test_generate_diff()
