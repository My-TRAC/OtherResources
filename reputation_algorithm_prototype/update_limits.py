from datetime import datetime, date
import peewee

# open database
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


def change_maximum(name_, value_):
    for limit in Limits_user.select().filter(name=name_):
        limit.maximum = value_
        limit.save()


def change_weight(name_, value_):
    for limit in Limits_user.select().filter(name=name_):
        limit.weight = value_
        limit.save()


if __name__ == "__main__":
    start_time = datetime.now()

    # example
    change_weight("uses_app", 17.1)
    change_maximum("uses_app", 200)

    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))
