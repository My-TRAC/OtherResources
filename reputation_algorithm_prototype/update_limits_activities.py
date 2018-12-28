from datetime import datetime, date
import peewee

# open database
db = peewee.MySQLDatabase('my-trac', user='root', passwd='')


class Limits_activities(peewee.Model):
    name = peewee.TextField()
    weight = peewee.FloatField()
    maximum = peewee.IntegerField()

    class Meta:
        database = db


class Weight:
    creation = Limits_activities.get(Limits_activities.name == 'creation').weight
    views = Limits_activities.get(Limits_activities.name == 'views').weight
    ratings_reputation = Limits_activities.get(Limits_activities.name == 'ratings_reputation').weight
    average_rating = Limits_activities.get(Limits_activities.name == 'average_rating').weight


class Maximum:
    creation = Limits_activities.get(Limits_activities.name == 'creation').maximum
    views = Limits_activities.get(Limits_activities.name == 'views').maximum
    ratings_reputation = Limits_activities.get(Limits_activities.name == 'ratings_reputation').maximum
    average_rating = Limits_activities.get(Limits_activities.name == 'average_rating').maximum


def change_maximum(name_, value_):
    for limit in Limits_activities.select().filter(name=name_):
        limit.maximum = value_
        limit.save()


def change_weight(name_, value_):
    for limit in Limits_activities.select().filter(name=name_):
        limit.weight = value_
        limit.save()


if __name__ == "__main__":
    start_time = datetime.now()

    # example
    change_weight("views", 55.91)
    change_maximum("views", 50)

    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))
