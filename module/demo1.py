# /usr/bin/env python3
import sys

sys.path.append('~/Documents/code/python')

import hello  # Hello World!

import importlib
hello = importlib.reload(hello)
