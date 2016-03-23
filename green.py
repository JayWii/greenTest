import datetime
import os
import random

# from heavy import special_commit


def modify():
    file = open('zero.md', 'r')
    flag = file.readline() == '0'
    file.close()
    file = open('zero.md', 'w+')
    if flag:
        file.write('1')
    else:
        file.write('0')
        file.close()


def commit():
    os.system('git commit -a -m test_github_streak')


def set_sys_time(day, month, year):
    os.system('date %02d%02d1720%04d' % (month, day, year))


def trick_commit(year, month, day):
    set_sys_time(year, month, day)
    modify()
    commit()


def daily_commit(start_date, end_date):
    for i in range((end_date - start_date).days - 5):
        if (i%random.randint(1,2)):
            cur_date = start_date + datetime.timedelta(days=(i+random.randint(1,5)))
            trick_commit(cur_date.day, cur_date.month, cur_date.year)


if __name__ == '__main__':
    daily_commit(datetime.date(2015, 9, 29), datetime.date(2016, 3, 23))
