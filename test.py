import logging
import sys
from cliff.test import *

test_classes = [
    BasicCliffTest
]

logging.basicConfig(level=logging.WARN)

# now run all the tests
suites = [unittest.TestLoader().loadTestsFromTestCase(test_class) for test_class in test_classes]

if __name__ == "__main__":
    suite = unittest.TestSuite(suites)
    test_result = unittest.TextTestRunner(verbosity=2).run(suite)
    if not test_result.wasSuccessful():
        sys.exit(1)
