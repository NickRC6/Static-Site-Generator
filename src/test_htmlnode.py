import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_multiple(self):
            node = HTMLNode(
                "a",
                None,
                None,
                {"href": "https://example.com", "target": "_blank"}
            )
            self.assertEqual(
                node.props_to_html(),
                ' href="https://example.com" target="_blank"'
            )

    def test_props_to_html_empty(self):
        node = HTMLNode("p")
        self.assertEqual(node.props_to_html(), "")

    def test_repr(self):
        node = HTMLNode("p", "Hello")
        self.assertIn("tag='p'", repr(node))
        self.assertIn("value='Hello'", repr(node))

if __name__ == "__main__":
    unittest.main()