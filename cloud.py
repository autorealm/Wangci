# coding: utf-8

from leancloud import Engine

from app import app


engine = Engine(app)


@engine.define
def hello(**params):
    if 'name' in params:
        return 'Hello, {}!'.format(params['name'])
    else:
        return 'Hello, LeanCloud!'


from leancloud import Query

@engine.define
def averageStars(movie):
    sum = 0
    query = Query('Review')
    try:
        reviews = query.find()
    except leancloud.LeanCloudError, e:
        // 如果不想做特殊处理，可以不捕获这个异常，直接抛出
        print e
        raise e
    for review in reviews:
        sum += review.get('starts')
    return sum / len(reviews)
