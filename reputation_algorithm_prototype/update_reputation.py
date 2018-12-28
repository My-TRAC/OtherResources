from datetime import datetime, date
from math import log
import peewee

# open DataBase
db = peewee.MySQLDatabase('my-trac', user='root', passwd='')


class Limits_user(peewee.Model):
    name = peewee.TextField()
    weight = peewee.FloatField()
    maximum = peewee.IntegerField()

    class Meta:
        database = db


class Weight:
    registration = Limits_user.get(Limits_user.name == 'registration').weight
    valuations = Limits_user.get(Limits_user.name == 'valuations').weight
    uses_app = Limits_user.get(Limits_user.name == 'uses_app').weight
    tickets_purchased = Limits_user.get(Limits_user.name == 'tickets_purchased').weight
    groups = Limits_user.get(Limits_user.name == 'groups').weight


class Maximum:
    registration = Limits_user.get(Limits_user.name == 'registration').maximum
    valuations = Limits_user.get(Limits_user.name == 'valuations').maximum
    uses_app = Limits_user.get(Limits_user.name == 'uses_app').maximum
    tickets_purchased = Limits_user.get(Limits_user.name == 'tickets_purchased').maximum
    groups = Limits_user.get(Limits_user.name == 'groups').maximum


class Users(peewee.Model):
    id = peewee.IntegerField()
    registration = peewee.DateField()
    valuations = peewee.IntegerField()
    uses_app = peewee.IntegerField()
    tickets_purchased = peewee.IntegerField()
    groups = peewee.IntegerField()
    reputation = peewee.FloatField()

    class Meta:
        database = db


def f_log(x_, x_max=100, slope_=100):
    return log(slope_*(x_/x_max)+1)/log(2+slope_)


def f_exp(x_, x_max=1, slope_=2):
    return pow((x_/x_max), slope_)


if __name__ == "__main__":
    start_time = datetime.now()

    # calculate reputation
    for user in Users.select():
        days_registered = (date.today() - user.registration).days
        user.reputation = f_log(user.valuations, Maximum.valuations)*Weight.valuations + \
                          f_exp(user.uses_app, Maximum.uses_app)*Weight.uses_app + \
                          f_log(user.tickets_purchased, Maximum.tickets_purchased)*Weight.tickets_purchased + \
                          (days_registered/Maximum.registration)*Weight.registration + \
                          f_log(user.groups, Maximum.groups)*Weight.groups

        if user.reputation > 100:
            user.reputation = 100
        elif user.reputation < 0:
            user.reputation = 0
        print(user.save())

    print('Duration: {}'.format(datetime.now() - start_time))
