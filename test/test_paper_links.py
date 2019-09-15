import unittest, re
import paper_links

class TestPaperLinks(unittest.TestCase):
    def test_bitly(self):
        result = paper_links.main(bitly=True)
        self.assertEqual(result[0][:15], "https://bit.ly/")

    def test_bitly_length(self):
        result = paper_links.main(bitly=True)
        self.assertEqual(len(result[0]), 22)

    def test_tinycc(self):
        result = paper_links.main(tinycc=True)
        self.assertEqual(result[0][:16], "https://tiny.cc/")
    
    def test_tinycc_length(self):
        result = paper_links.main(tinycc=True)
        self.assertEqual(len(result[0]), 22)

    def test_tinyurl(self):
        result = paper_links.main(tinyurl=True)
        self.assertEqual(result[0][:20], "https://tinyurl.com/")
    
    def test_tinyurl_length(self):
        result = paper_links.main(tinyurl=True)
        self.assertEqual(len(result[0]), 28)

    def test_isgd(self):
        result = paper_links.main(isgd=True)
        self.assertEqual(result[0][:14], "https://is.gd/")

    def test_isgd_length(self):
        result = paper_links.main(isgd=True)
        self.assertEqual(len(result[0]), 20)

    def test_soogd(self):
        result = paper_links.main(soogd=True)
        self.assertEqual(result[0][:15], "https://soo.gd/")
    
    def test_soogd_length(self):
        result = paper_links.main(soogd=True)
        self.assertEqual(len(result[0]), 19)

    def test_all_urls_length(self):
        result = paper_links.main(all_urls=True)
        self.assertEqual(len(result), 5)

    def test_long_hash(self):
        result = paper_links.main(bitly=True, long_hash=True)[0]
        m = re.search('bit.ly/(.{12})$', result)
        self.assertEqual(len(m.group(1)), 12)
