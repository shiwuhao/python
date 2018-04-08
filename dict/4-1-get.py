#!/usr/bin/python encoding=utf-8
people = {
    'shiwuhao' : {
        'phone' : '18501367987',
        'addr' : 'Foo drive 23',
    },

    'chenxiaoding' : {
        'phone' : '18501367990',
        'addr' : 'Foo drive 24',
    },
    'xiaoxiaoding' : {
        'phone' : '18501367989',
        'addr' : 'Foo drive 25',
    },
    'xiaoxiaohao' : {
        'phone' : '18501367988',
        'addr' : 'Foo drive 26',
    },
}
labels = {
    'phone' : 'phone number',
    'addr' : 'address',
}

name = raw_input('Name: ')
request = raw_input('Phone number (p) or address (a)')
key = request

if request == 'p' : key = 'phone'
if request == 'a' : key = 'addr'

# 使用get提供默认值:
person = people.get(name, {})
label  = labels.get(key, key)
result = person.get(key, 'not available')

if name in people :
    print "%s's %s is %s" % (name, label, result)
