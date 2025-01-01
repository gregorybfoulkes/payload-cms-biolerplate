import unittest
from models.content import Content

class TestContent(unittest.TestCase):
    """
    Test cases for the Content class in the Payload CMS.
    """

    def setUp(self):
        """Set up test variables."""
        self.content = Content(title='Test Title', body='Test Body')

    def test_content_initialization(self):
        """Test that the Content class initializes correctly."""
        self.assertEqual(self.content.title, 'Test Title')
        self.assertEqual(self.content.body, 'Test Body')

    def test_to_dict(self):
        """Test the to_dict method of the Content class."""
        expected_dict = {'title': 'Test Title', 'body': 'Test Body'}
        self.assertEqual(self.content.to_dict(), expected_dict)

if __name__ == '__main__':
    unittest.main()