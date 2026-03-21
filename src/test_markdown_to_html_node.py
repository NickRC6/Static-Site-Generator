import unittest
from markdown_to_html_node import markdown_to_html_node


def test_heading(self):
    md = "# Title"
    html = markdown_to_html_node(md).to_html()
    self.assertEqual(html, "<div><h1>Title</h1></div>")


def test_unordered_list(self):
    md = "- a\n- b"
    html = markdown_to_html_node(md).to_html()
    self.assertEqual(html, "<div><ul><li>a</li><li>b</li></ul></div>")


def test_ordered_list(self):
    md = "1. a\n2. b"
    html = markdown_to_html_node(md).to_html()
    self.assertEqual(html, "<div><ol><li>a</li><li>b</li></ol></div>")