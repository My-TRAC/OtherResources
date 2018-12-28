from datetime import datetime, date
from math import log
import peewee

# open DataBase
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


class Activities(peewee.Model):
    id = peewee.IntegerField(primary_key=True)
    activity_date = peewee.DateField()
    views = peewee.IntegerField()
    reputation = peewee.FloatField()

    class Meta:
        database = db


class Ratings(peewee.Model):
    id_user = peewee.IntegerField()
    id_activity = peewee.IntegerField(primary_key=True)
    rating = peewee.IntegerField()
    reputation_user = peewee.IntegerField()

    class Meta:
        database = db


def f_log(x_, x_max=100, slope_=100):
    return log(slope_*(x_/x_max)+1)/log(2+slope_)


def f_exp(x_, x_max=100, slope_=2):
    return pow((x_/x_max), slope_)


def weighted_average(activity_number_):
    query = Ratings.select().where(Ratings.id_activity == activity_number_)
    if query.count():
        numerator = 0
        denominator = 0
        for activity_ in query:
            numerator += activity_.rating * activity_.reputation_user
            denominator += activity_.reputation_user
        average = numerator / denominator

        return average
    else:
        return 1


if __name__ == "__main__":
    start_time = datetime.now()

    # calculate reputation
    for activity in Activities.select():
        days_registered = (date.today() - activity.activity_date).days
        avg_rating_reputation = weighted_average(activity.id)

        activity.reputation = f_log(activity.views, days_registered*Maximum.views, 50)*Weight.views + \
                              f_exp(avg_rating_reputation, Maximum.average_rating)*Weight.average_rating

        if activity.reputation > 100:
            activity.reputation = 100
        elif activity.reputation < 0:
            activity.reputation = 0
        print(activity.save())

    print('Duration: {}'.format(datetime.now() - start_time))
