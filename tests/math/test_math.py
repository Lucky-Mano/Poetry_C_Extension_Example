from unittest import TestCase

import spam.math as math


class SpamTest(TestCase):
    def test_spam(self):
        print(dir(math))
        assert math.add(1, 2) == 3

        assert math.add(3, 4) == 7
