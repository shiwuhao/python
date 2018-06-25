# /usr/bin/env python3
from warnings import warn, filterwarnings

filterwarnings("ignore")
warn('这个信息看不到')

filterwarnings("error")
warn('这个信息能看到')
