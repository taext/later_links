import unittest, re
import paper_links

class TestPaperLinks(unittest.TestCase):

## TEST RANDOM URL FUNCTIONS

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


## TEST BUILD-IN CONSTANTS

    def test_date(self):
        self.assertEqual(len(paper_links.date), 10)

    def test_version(self):
        self.assertEqual(len(paper_links.version), 6)

    def test_author(self):
        self.assertEqual(paper_links.author, "https://github.com/taext")

    def test_feedback_welcome(self):
        self.assertEqual(paper_links.feedback_welcome, "gh@v1d.dk")

    def test_whats_new(self):
        self.assertNotEqual(len(paper_links.whats_new), 0)
