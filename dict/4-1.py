#!/usr/bin/python
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

if request == 'p' : key = 'phone'
if request == 'a' : key = 'addr'

if name in people :
    print "%s's %s is %s" % (name, labels[key], people[name][key])
