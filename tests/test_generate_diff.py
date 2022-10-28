from gendiff.gendiff import generate_diff


def test_generate_diff():
    with open('tests/fixtures/res.txt') as f:
        result = f.read()
        assert generate_diff(
            'tests/fixtures/file1.json',
            'tests/fixtures/file2.json',
        ) == result
