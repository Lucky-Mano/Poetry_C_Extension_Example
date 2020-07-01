from unittest import TestCase

import spam.ext as sp

class SpamTest(TestCase):
    def test_spam(self):
        #print(sp.__path__)
        print(dir(sp))
        sp.system("ls -l")
