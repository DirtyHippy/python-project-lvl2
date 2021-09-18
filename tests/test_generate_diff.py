from gendiff.scripts.gendiff import generate_diff
import os


def generate_diff_by_file_ext(file_ext):
    test_dir = os.path.dirname(os.path.realpath(__file__))
    with open(test_dir + "/fixtures/simple.txt", "r") as test1:
        assert generate_diff(
            test_dir + "/fixtures/simple1.{}".format(file_ext),
            test_dir + "/fixtures/simple2.{}".format(file_ext)
        ) == test1.read()


def test_simple_json():
    generate_diff_by_file_ext("json")


def test_simple_yml():
    generate_diff_by_file_ext("yml")
