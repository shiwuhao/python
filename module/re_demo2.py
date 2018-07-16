#!/usr/bin/env python3
import re

emphasis_pattern = r'\*\*(.+?)\*\*'
res = re.sub(emphasis_pattern, r'<em>\1</em>', '**This** is **it**')
print(res)