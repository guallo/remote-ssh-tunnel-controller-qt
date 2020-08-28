#!/usr/bin/env python3

import os
import sys

devnull_file = open(os.devnull, 'w')
sys.stdout = devnull_file
sys.stderr = devnull_file

from rssht_controller_qt.main import main


status = main(sys.argv)
sys.exit(status)
