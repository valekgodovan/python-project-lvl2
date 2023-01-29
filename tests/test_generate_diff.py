from gendiff import generate_diff


def test_generate_diff_json():
    with open('tests/fixtures/result_stylish.txt') as f:
        result = f.read()
        assert generate_diff(
            'tests/fixtures/file1.json',
            'tests/fixtures/file2.json',
        ) == result


def test_generate_diff_json_nested():
    with open('tests/fixtures/result_stylish_nested.txt') as f:
        result = f.read()
        assert generate_diff(
            'tests/fixtures/file3.json',
            'tests/fixtures/file4.json',
        ) == result


def test_generate_diff_yaml():
    with open('tests/fixtures/result_stylish.txt') as f:
        result = f.read()
        assert generate_diff(
            'tests/fixtures/file1.yaml',
            'tests/fixtures/file2.yaml',
        ) == result


def test_generate_diff_yaml_nested():
    with open('tests/fixtures/result_stylish_nested.txt') as f:
        result = f.read()
        assert generate_diff(
            'tests/fixtures/file3.yaml',
            'tests/fixtures/file4.yaml',
        ) == result


def test_generate_diff_json_yaml():
    with open('tests/fixtures/result_stylish.txt') as f:
        result = f.read()
        assert generate_diff(
            'tests/fixtures/file1.json',
            'tests/fixtures/file2.yaml',
        ) == result


def test_generate_diff_plain():
    with open('tests/fixtures/result_plain') as f:
        result = f.read()
        assert generate_diff(
            'tests/fixtures/file1.json',
            'tests/fixtures/file2.yaml',
            format_name='plain'
        ) == result


def test_generate_diff_plain_nested():
    with open('tests/fixtures/result_plain_nested') as f:
        result = f.read()
        assert generate_diff(
            'tests/fixtures/file3.json',
            'tests/fixtures/file4.yaml',
            format_name='plain'
        ) == result
