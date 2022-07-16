import pytest
from gendiff.scripts.gendiff import generate_diff


FILE_1 = "/tests/file1.json"
FILE_2 = "/tests/file2.json"
FILE_3 = '{"-follow": false,"host": "hexlet.io","-proxy": "123.234.53.22","-timeout": 50, "+timeout": 20, "+verbose": true}'


def generate_diff_1():
    assert generate_diff(FILE_1, FILE_2) == FILE_3