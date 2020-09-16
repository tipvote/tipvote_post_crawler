from app import db
from app.models import Comments
from datetime import datetime
from datetime import timedelta

# multipliers
upvote_var = 2
downvote_var = 1
comment_var = 3
post_tip_var = 25


def crawlcomments():
    time_ago = datetime.today() - timedelta(days=10)
    getthecomments = db.session.query(Comments)
    getthecomments = getthecomments.filter(Comments.active == 1)
    getthecomments = getthecomments.filter(Comments.created >= time_ago)
    getthecomments = getthecomments.all()

    # need to activate a way to add negative over time ration
    for com in getthecomments:
        # get money given
        dollars_tips = com.total_recieved_btc_usd

        # get post votes
        comment_downvotes = com.downvotes_on_comment
        comment_upvotes = com.upvotes_on_comment

        # calculate it
        rated_downvotes = comment_downvotes * downvote_var
        rated_upvotes = comment_upvotes * upvote_var
        rated_tips = dollars_tips * post_tip_var

        if rated_tips < 1:
            rated_tips = 0
        else:
            rated_tips = rated_tips

        # add together
        postrating = rated_downvotes + rated_upvotes + rated_tips

        com.total_exp_commons = postrating
        db.session.add(com)
    db.session.commit()


if __name__ == '__main__':
    crawlcomments()
