from src.read_so_data import _filter_post


def test_read_so_data():
    with open('test_so.xml') as f:
        f.readline()
        f.readline()
        match = []
        for line in f:
            match.append(_filter_post(line, 'datetime'))

        assert match[0]
        assert not match[1]
