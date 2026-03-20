import unittest

from extract_markdown import extract_markdown_images, extract_markdown_links


class TestExtractMarkdown(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual(
            [("image", "https://i.imgur.com/zjjcJKZ.png")],
            matches
        )

    def test_extract_multiple_images(self):
        text = "![a](url1) and ![b](url2)"
        matches = extract_markdown_images(text)
        self.assertListEqual([("a", "url1"), ("b", "url2")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "Check [Google](https://google.com)"
        )
        self.assertListEqual(
            [("Google", "https://google.com")],
            matches
        )

    def test_extract_multiple_links(self):
        text = "[a](url1) and [b](url2)"
        matches = extract_markdown_links(text)
        self.assertListEqual([("a", "url1"), ("b", "url2")], matches)


if __name__ == "__main__":
    unittest.main()