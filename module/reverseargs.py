# /usr/bin/env python3

import sys
args = sys.argv[1:]
args.reverse()
print(' '.join(args))
print(' '.join(reversed(sys.argv[1:0])))