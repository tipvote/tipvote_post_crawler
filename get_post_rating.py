from app import db
from app.models import CommonsPost, Comments, PostPromotions, PostCoins, PostDonations
from datetime import datetime, timedelta
from decimal import Decimal

# multipliers
upvote_var = 2
downvote_var = 1
comment_var = 2
post_tip_var = 5
post_promotion_var = 50


def crawlposts():
    print("crawling ...")
    time_ago = datetime.today() - timedelta(days=5)
    getposts = db.session.query(CommonsPost)
    getposts = getposts.filter(CommonsPost.active == 1)
    getposts = getposts.filter(CommonsPost.last_active >= time_ago)
    getposts = getposts.all()

    # need to activate a way to add negative over time ration
    for post in getposts:

        gettips = PostDonations.query.filter(post.id == PostDonations.post_id).first()
        getpromote = PostPromotions.query.filter(post.id == PostPromotions.post_id).first()
        thecoins = PostCoins.query.filter(PostCoins.post_id == post.id).first()
        getcomments = db.session.query(Comments)
        getcomments = getcomments.filter(Comments.commons_post_id == post.id)
        getcomments_count = getcomments.count()

        # get money given
        if gettips:
            dollars_tips = gettips.total_recieved_btc_usd\
                           + gettips.total_recieved_bch_usd\
                           + gettips.total_recieved_xmr_usd
            if dollars_tips < 1:
                dollars_tips = 5
            else:
                dollars_tips = dollars_tips
        else:
            dollars_tips = 0

        if getpromote:
            dollars_promotions = getpromote.total_recieved_btc_usd + getpromote.total_recieved_bch_usd + getpromote.total_recieved_xmr_usd
            if dollars_promotions < 1:
                dollars_promotions = 5
            else:
                dollars_promotions = dollars_promotions
        else:
            dollars_promotions = 0

        # get post votes
        post_downvotes = post.downvotes_on_post
        post_upvotes = post.upvotes_on_post

        rated_tips = dollars_tips * post_tip_var
        rated_promote = dollars_promotions * post_promotion_var

        rated_comment = getcomments_count * comment_var
        rated_downvotes = post_downvotes * downvote_var
        rated_upvotes = post_upvotes * upvote_var

        if thecoins:
            coin_value_1 = 25
            coin_value_2 = 10
            coin_value_3 = 25
            coin_value_4 = 50
            coin_value_5 = 5

            amount_coin_1 = thecoins.coin_1 * coin_value_1
            amount_coin_2 = thecoins.coin_2 * coin_value_2
            amount_coin_3 = thecoins.coin_3 * coin_value_3
            amount_coin_4 = thecoins.coin_4 * coin_value_4
            amount_coin_5 = thecoins.coin_5 * coin_value_5

            thecoinamount = amount_coin_1 + amount_coin_2 + amount_coin_3 + amount_coin_4 + amount_coin_5
        else:
            thecoinamount = 0


        # get time variable
        now = datetime.utcnow()
        one_day_age = datetime.utcnow() - timedelta(days=1)
        two_day_age = datetime.utcnow() - timedelta(days=2)
        three_day_age = datetime.utcnow() - timedelta(days=3)
        four_day_age = datetime.utcnow() - timedelta(days=4)
        five_day_age = datetime.utcnow() - timedelta(days=5)
        six_day_age = datetime.utcnow() - timedelta(days=6)
        seven_day_age = datetime.utcnow() - timedelta(days=7)
        eight_day_age = datetime.utcnow() - timedelta(days=8)
        nine_day_age = datetime.utcnow() - timedelta(days=9)
        ten_day_age = datetime.utcnow() - timedelta(days=10)

        # calculte variable coefficient multiplier
        if now >= post.created >= one_day_age:
            time_depletion_variable = 1
        elif one_day_age >= post.created >= two_day_age:
            time_depletion_variable = 0.7
        elif two_day_age >= post.created >= three_day_age:
            time_depletion_variable = 0.5
        elif three_day_age >= post.created >= four_day_age:
            time_depletion_variable = 0.3
        elif four_day_age >= post.created >= five_day_age:
            time_depletion_variable = 0.05
        elif five_day_age >= post.created >= six_day_age:
            time_depletion_variable = 0
        elif six_day_age >= post.created >= seven_day_age:
            time_depletion_variable = 0
        elif seven_day_age >= post.created >= eight_day_age:
            time_depletion_variable = 0
        elif eight_day_age >= post.created >= nine_day_age:
            time_depletion_variable = 0
        elif nine_day_age >= post.created >= ten_day_age:
            time_depletion_variable = 0
        else:
            time_depletion_variable = 0

        post.decay_rate = time_depletion_variable
        postrating = rated_comment + rated_downvotes + rated_upvotes +\
                     rated_tips + rated_promote + thecoinamount

        # determine final hotness rating over time
        timedrating = Decimal(postrating) * Decimal(time_depletion_variable)

        if int(timedrating) > int(post.highest_exp_reached):
            post.highest_exp_reached = int(timedrating)
        post.hotness_rating_now = int(timedrating)

    db.session.commit()


if __name__ == '__main__':
    crawlposts()
