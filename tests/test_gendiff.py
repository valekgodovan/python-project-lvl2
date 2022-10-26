from gendiff.gendiff import gen_diff


def test_gen_diff():
    with open('tests/fixtures/res.txt') as f:
        result = f.read()
        assert gen_diff(
            'tests/fixtures/file1.json',
            'tests/fixtures/file2.json'
            ) == result
