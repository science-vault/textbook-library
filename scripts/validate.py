"""Validate the published textbook catalogue. No network or dependencies required."""
import json
from pathlib import Path
from urllib.parse import urlparse
def validate(value):
    if value.get('version') != 1 or not isinstance(value.get('books'), list):
        raise ValueError('Expected version 1 and a books list')
    ids = set()
    for book in value['books']:
        for key in ('id', 'title', 'author', 'subject', 'url'):
            if not isinstance(book.get(key), str) or not book[key].strip():
                raise ValueError(f'Missing {key}')
        if book['id'] in ids:
            raise ValueError('Duplicate textbook ID: ' + book['id'])
        ids.add(book['id'])
        years = book.get('years')
        if not isinstance(years, list) or any(type(y) is not int or y not in range(1, 13) for y in years):
            raise ValueError('Years must be integers from 1 to 12; use an empty list when unspecified')
        for key in ('url', 'cover'):
            if not book.get(key):
                continue
            u = urlparse(book[key])
            if u.scheme != 'https' or not u.netloc or u.username or u.password:
                raise ValueError(key + ' must be an HTTPS URL without credentials')
    return len(ids)
if __name__ == '__main__':
    root = Path(__file__).resolve().parents[1]
    count = validate(json.loads((root/'site/catalog.json').read_text()))
    print(f'Catalogue validated: {count} textbooks')
