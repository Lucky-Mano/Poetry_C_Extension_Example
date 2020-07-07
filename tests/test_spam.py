from unittest import TestCase

import spam as sp


class SpamTest(TestCase):
    def test_spam(self):
        print(dir(sp))
        sp.system("ls -l")
