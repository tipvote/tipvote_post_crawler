from app import db
from app.models import CommonsPost, Comments
from datetime import datetime
from datetime import timedelta


def crawlposts():
    print("checking posts")
    specific_days_ago = datetime.today() - timedelta(days=5)
    getposts = db.session.query(CommonsPost)
    getposts = getposts.filter(CommonsPost.active == 1)
    getposts = getposts.filter(CommonsPost.last_active <= specific_days_ago)
    getposts = getposts.all()

    for post in getposts:
        print(post.id)
        post.active = 0
        post.hotness_rating_now = 0
        db.session.add(post)
    db.session.commit()


def posttozero():
    print("putting to zero")
    getposts = db.session.query(CommonsPost)
    getposts = getposts.filter(CommonsPost.active == 0)
    getposts = getposts.filter(CommonsPost.hotness_rating_now > 0)
    getposts = getposts.all()
    for f in getposts:
        print(f.id)
        f.hotness_rating_now = 0
        db.session.add(f)
    db.session.commit()


def crawlcomments():
    specific_days_ago = datetime.today() - timedelta(days=10)
    getcomments = db.session.query(Comments)
    getcomments = getcomments.filter(Comments.active == 1)
    getcomments = getcomments.filter(Comments.created <= specific_days_ago)
    getcomments = getcomments.all()

    for com in getcomments:
        com.active = 0
        db.session.add(com)
    db.session.commit()


if __name__ == '__main__':
    crawlposts()
    posttozero()
    crawlcomments()
