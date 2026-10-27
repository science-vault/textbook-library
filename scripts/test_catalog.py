import copy
import unittest
from validate import validate
BOOK = dict(id='physics-12', title='Example book', author='Example author', subject='Physics ATAR', years=[11,12], url='https://example.com/book.pdf')
class CatalogueTests(unittest.TestCase):
    def test_empty(self): self.assertEqual(validate(dict(version=1,books=[])),0)
    def test_multiple_years(self): self.assertEqual(validate(dict(version=1,books=[BOOK])),1)
    def test_duplicates(self):
        with self.assertRaises(ValueError): validate(dict(version=1,books=[BOOK,BOOK]))
    def test_unsafe_url_and_invalid_year(self):
        for change in (dict(url='javascript:alert(1)'),dict(url='https://user:password@example.com/book'),dict(years=[13]),dict(years=[True]),dict(title='')):
            with self.assertRaises(ValueError): validate(dict(version=1,books=[{**BOOK,**change}]))
if __name__=='__main__': unittest.main()
