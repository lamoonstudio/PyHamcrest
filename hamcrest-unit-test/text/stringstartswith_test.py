if __name__ == '__main__':
    import sys
    sys.path.insert(0, '..')
    sys.path.insert(0, '../..')

import unittest

from hamcrest.core.core.isnot import not_
from hamcrest.core.matcher_assert import assert_that
from hamcrest.library.text.stringstartswith import startswith

from matcher_test import MatcherTest


EXCERPT = 'EXCERPT'
stringstartswith = startswith(EXCERPT)

class StringStartsWithTest(MatcherTest):

    def testEvaluatesToTrueIfArgumentContainsSpecifiedSubstring(self):
        self.assert_(stringstartswith.matches(EXCERPT + 'END'),
                    'should be true if excerpt at beginning')
        self.assert_(not stringstartswith.matches('START' + EXCERPT),
                    'should be false if excerpt at end')
        self.assert_(not stringstartswith.matches('START' + EXCERPT + 'END'),
                    'should be false if excerpt in middle')
        self.assert_(stringstartswith.matches(EXCERPT + EXCERPT),
                    'should be true if excerpt is at beginning and repeated')

        self.assert_(not stringstartswith.matches('Something else'),
                    'should be false if excerpt is not in string')
        self.assert_(not stringstartswith.matches(EXCERPT[1:]),
                    'should false if part of excerpt is at start of string')

    def testEvaluatesToTrueIfArgumentIsEqualToSubstring(self):
        self.assert_(stringstartswith.matches(EXCERPT),
                    'should be true if excerpt is entire string')

    def testHasAReadableDescription(self):
        self.assert_description("a string starting with 'a'", startswith('a'))

    def testConstructorRequiresString(self):
        self.assertRaises(TypeError, startswith, 3)

    def testFailsIfMatchingAgainstNonString(self):
        assert_that(object(), not_(stringstartswith))


if __name__ == '__main__':
    unittest.main()
