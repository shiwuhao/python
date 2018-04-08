#~/usr/bin/python
template = '''
<html>
<head>
 <title>%(title)s</title>
</head>
    <body>
        <h1>%(title)s</h1>
        <p>%(text)s</p>
    </body>
</html>
'''
data = {'title':'My Home Page', 'text':'This is My Home Page'}
print template % data
