import unittest
from bs4 import BeautifulSoup

class TestHtml(unittest.TestCase):
    def test_h1_tag_is_correct(self):
        with open('index.html', 'r') as f:
            soup = BeautifulSoup(f, 'lxml')

        h1_tag = soup.find('h1')
        self.assertIsNotNone(h1_tag, "h1 tag should exist")
        self.assertEqual(h1_tag.name, 'h1', "The tag should be a h1 tag")
        self.assertNotIn('<>', str(h1_tag), "The h1 tag should not contain malformed closing tag characters")

if __name__ == '__main__':
    unittest.main()