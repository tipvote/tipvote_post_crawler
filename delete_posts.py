from app import db
from app.models import CommonsPost, Comments, PostPromotions, PostCoins, PostDonations


def delete_a_posts(postid):

    thepost = CommonsPost.query.filter(CommonsPost.id == postid).first()
    thecomments = db.session.query(Comments).filter(Comments.commons_post_id == postid).all()
    for f in thecomments:
        db.session.delete(f)
    db.session.delete(thepost)
    db.session.commit()


def delete_all_posts():
    post = CommonsPost.query.all()
    comments = Comments.query.all()
    promotes = PostPromotions.query.all()
    pcoins = PostCoins.query.all()
    pdonates = PostDonations.query.all()

    for f in post:
        db.session.delete(f)

    for g in comments:
        db.session.delete(g)
    db.session.commit()

    for h in promotes:
        db.session.delete(h)
    db.session.commit()

    for j in pcoins:
        db.session.delete(j)
    db.session.commit()

    for k in pdonates:
        db.session.delete(k)
    db.session.commit()

#delete_a_posts()
delete_all_posts()
