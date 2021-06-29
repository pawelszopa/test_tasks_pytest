import json


def test_igor_in_krakow(author_file_json):
    with author_file_json.open() as f:
        authors = json.load(f)

    assert authors['Igor']['City'] == 'Krakow'


def test_all_have_cities(author_file_json):
    with author_file_json.open() as f:
        authors = json.load(f)

    for a in authors:
        assert len(authors[a]['City']) > 0
