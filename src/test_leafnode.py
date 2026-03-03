import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    def test_leaf_to_html_strong(self):
        node = LeafNode("strong", "Bold text")
        self.assertEqual(node.to_html(), "<strong>Bold text</strong>")

    def test_leaf_to_html_em(self):
        node = LeafNode("em", "Italic text")
        self.assertEqual(node.to_html(), "<em>Italic text</em>")

if __name__ == "__main__":
    unittest.main()