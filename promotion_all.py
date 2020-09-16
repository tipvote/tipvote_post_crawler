from app import db
from app.models import GiveawayAll, CommonsPost, PostPromote
from sqlalchemy import func


def crawlposts():
    tipvote_giveaway = 100
    # get this weeks giveaway
    thegiveaway = GiveawayAll.query.order_by(GiveawayAll.id.desc()).first()
    startofcontest = thegiveaway.start_promotion
    endofcontest = thegiveaway.end_promotion

    # get all the post between it
    getpoststhisweek = db.session.query(CommonsPost)
    getpoststhisweek = getpoststhisweek.filter(CommonsPost.created >= startofcontest)
    getpoststhisweek = getpoststhisweek.filter(CommonsPost.created <= endofcontest)
    getpoststhisweek = getpoststhisweek.order_by(CommonsPost.upvotes_on_post.desc())
    getpoststhisweek = getpoststhisweek.first()

    # calcuate promotions this week and assign to pot
    promotionsthisweek = PostPromote.query.with_entities(func.sum(PostPromote.amount_usd).label('theavg'))
    promotionsthisweek = promotionsthisweek.filter(PostPromote.created >= startofcontest)
    promotionsthisweek = promotionsthisweek.filter(PostPromote.created <= endofcontest)
    promotionsthisweek = promotionsthisweek.scalar()

    if promotionsthisweek is None:
        thesum = 0
    else:
        thesum = promotionsthisweek

    print("*"*10)
    print(getpoststhisweek.id)
    print(getpoststhisweek.content_user_name)
    print(getpoststhisweek.upvotes_on_post)
    print(thesum)

    # assign post and user to giveaway
    thegiveaway.post_id = getpoststhisweek.id
    thegiveaway.leader_user_id = getpoststhisweek.content_user_id
    thegiveaway.leader_user_name = getpoststhisweek.content_user_name
    thegiveaway.total_usd = tipvote_giveaway + thesum

    db.session.add(thegiveaway)
    db.session.commit()


if __name__ == '__main__':
    crawlposts()
