import unittest
from textnode import TextNode, TextType
from split_nodes_images_links import split_nodes_image, split_nodes_link


class TestSplitNodes(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "Text ![img](url1) more ![img2](url2)",
            TextType.TEXT,
        )
        result = split_nodes_image([node])

        self.assertListEqual(
            [
                TextNode("Text ", TextType.TEXT),
                TextNode("img", TextType.IMAGE, "url1"),
                TextNode(" more ", TextType.TEXT),
                TextNode("img2", TextType.IMAGE, "url2"),
            ],
            result,
        )

    def test_split_links(self):
        node = TextNode(
            "Go to [A](url1) and [B](url2)",
            TextType.TEXT,
        )
        result = split_nodes_link([node])

        self.assertListEqual(
            [
                TextNode("Go to ", TextType.TEXT),
                TextNode("A", TextType.LINK, "url1"),
                TextNode(" and ", TextType.TEXT),
                TextNode("B", TextType.LINK, "url2"),
            ],
            result,
        )

    def test_no_images(self):
        node = TextNode("plain text", TextType.TEXT)
        result = split_nodes_image([node])
        self.assertEqual(result, [node])

    def test_no_links(self):
        node = TextNode("plain text", TextType.TEXT)
        result = split_nodes_link([node])
        self.assertEqual(result, [node])


if __name__ == "__main__":
    unittest.main()