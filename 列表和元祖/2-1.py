#!/usr/bin/python encoding: utf-8
# 根据给定的年月日 以数字形式打印出日期
months = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'August',
    'September',
    'October',
    'November',
    'December'
]

# 以1--31的数字为结尾的列表
endings = ['st', 'nd', 'rd'] + 17 * ['th'] \
        + ['st', 'nd', 'rd'] + 17 * ['th'] \
        + ['st']

year = raw_input('Year: ')
month = raw_input('Month (1-12): ')
day = raw_input('Day (1-31): ')

month_number = int(month)
day_number = int(day)

month_name = months[month_number - 1]
ordinal = day + endings[day_number - 1]

print month_name + ' ' + ordinal + '. ' + year

