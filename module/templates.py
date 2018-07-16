#!/usr/bin/env python3
import fileinput, re

# 与使用方括号括起的字段匹配
field_pat = re.compile(r'\[(.+?)\]')

# 我们将把变量收集到这里
scope = {}


# 用于调用re.sub
def replacement(match):
    code = match.group(1)
    try:
        return str(eval(code, scope))
    except SyntaxError:
        return ''


lines = []
for line in fileinput.input():
    lines.append(line)

text = ''.join(lines)

print(field_pat.sub(replacement, text))
