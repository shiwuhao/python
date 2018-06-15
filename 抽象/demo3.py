# /usr/bin/env python3
def story(**kwds):
    return 'Once upon a time, there was a {job} called {name}.'.format_map(kwds)


def power(x, y, *others):
    if others:
        print('Received redundant parameters:', others)
    return pow(x, y)


def interval(start, stop=None, step=1):
    'Imitates range() for step > 0'
    if stop is None:
        start, stop = 0, start
    result = []

    i = start
    while i < stop:
        result.append(i)
        i += step
    return result


print(story(job='king', name='Gumby'))
print(story(name='shiwuhao', job='php'))
params = {'job': 'language', 'name': 'Python'}
print(story(**params))
del params['job']
print(story(job='stroke of genius', **params))
print('--' * 50)

print(power(2, 3))
print(power(3, 2))
print(power(x=3, y=2))
print(power(y=2, x=3))

params = (5,) * 2
print(params)
print(power(*params))
print(power(3, 3, 'Hello World'))
print('--' * 50)

print(interval(10))
print(interval(1, 5))
print(interval(3, 12, 4))
print(power(*interval(3,7)))
