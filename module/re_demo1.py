#!/usr/bin/env python3
import re

emphasis_pattern = r'\*([^\*]+)\*'
emphasis_pattern = re.compile(r'''
\*      # 起始突出标志
(       # 与要突出的内容匹配的编组的起始位置
[^\*]+  # 与除星号外的其他字符都匹配
)       # 编组到此结束
\*      # 结束突出标志
''', re.VERBOSE)

res = re.sub(emphasis_pattern, r'<em>\1</em>', 'Hello *world*!')
print(res)