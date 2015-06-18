#! /usr/bin/env python

import unittest, logging
import sys

from mediameter.test.clifftest import *

test_classes = [
    CliffTest
]

# set up all logging to DEBUG (cause we're running tests here!)
logging.basicConfig(level=logging.DEBUG)
log_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
log_handler = logging.FileHandler('cliff-api-test.log')
log_handler.setFormatter(log_formatter)
# set up mediacloud logging to the file
mc_logger = logging.getLogger('mediameter')
mc_logger.propagate = False
mc_logger.addHandler(log_handler)
# set up requests logging to the file
requests_logger = logging.getLogger('requests')
requests_logger.propagate = False
requests_logger.addHandler(log_handler)

# now run all the tests
suites = [ unittest.TestLoader().loadTestsFromTestCase(test_class) for test_class in test_classes ]

if __name__ == "__main__":
    suite = unittest.TestSuite(suites)
    test_result = unittest.TextTestRunner(verbosity=2).run(suite)
    if not test_result.wasSuccessful():
        sys.exit(1)
