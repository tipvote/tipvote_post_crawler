# coding=utf-8
from app import db
from datetime import datetime

class GiveawayAll(db.Model):
    __tablename__ = 'avengers_promotion_giveaway_all'
    __bind_key__ = 'avengers'
    __table_args__ = {"schema": "avengers_promotion", 'useexisting': True}

    id = db.Column(db.Integer, primary_key=True)
    # id of top post
    post_id = db.Column(db.Integer, db.ForeignKey('avengers_post.avengers_posts_posts.id'))
    # total amount raised for post
    total_usd = db.Column(db.DECIMAL(20, 2))

    # last promotion given
    last_promotion = db.Column(db.TIMESTAMP())
    # start of contest
    start_promotion = db.Column(db.TIMESTAMP())
    # end of contest
    end_promotion = db.Column(db.TIMESTAMP())
    # name of person leading contest
    leader_user_id = db.Column(db.Integer)
    leader_user_name = db.Column(db.String(140))


# List of user ids and postupvotes
# used so no double upvoting
class PostUpvotes(db.Model):
    __tablename__ = 'avengers_posts_upvotes'
    __bind_key__ = 'avengers'
    __table_args__ = {"schema": "avengers_post", 'useexisting': True}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    post_id = db.Column(db.Integer)


# List of user ids and commentupvotes
# used so no double upvoting
class CommentsUpvotes(db.Model):
    __tablename__ = 'avengers_comments_upvotes'
    __bind_key__ = 'avengers'
    __table_args__ = {"schema": "avengers_comments", 'useexisting': True}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    comment_id = db.Column(db.Integer)


class BchWallet(db.Model):
    __tablename__ = 'bch_wallet'
    __bind_key__ = 'avengers'
    __table_args__ = {"schema": "avengers_wallet_bch", "useexisting": True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.INTEGER, db.ForeignKey('avengers_user.users.id'))
    currentbalance = db.Column(db.DECIMAL(20, 8))
    address1 = db.Column(db.TEXT)
    address1status = db.Column(db.INTEGER, )
    address2 = db.Column(db.TEXT)
    address2status = db.Column(db.INTEGER)
    address3 = db.Column(db.TEXT)
    address3status = db.Column(db.INTEGER)
    locked = db.Column(db.INTEGER)
    transactioncount = db.Column(db.INTEGER)
    unconfirmed = db.Column(db.DECIMAL(20, 8))


class BchTransOrphan(db.Model):
    __tablename__ = 'bch_transorphan'
    __bind_key__ = 'avengers'
    __table_args__ = {"schema": "avengers_wallet_bch","useexisting": True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    bch = db.Column(db.DECIMAL(20, 8))
    bchaddress = db.Column(db.TEXT)
    txid = db.Column(db.TEXT)


class BchUnconfirmed(db.Model):
    __tablename__ = 'bch_unconfirmed'
    __bind_key__ = 'avengers'
    __table_args__ = {"schema": "avengers_wallet_bch", "useexisting": True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    user_id = db.Column(db.INTEGER, db.ForeignKey('avengers_user.users.id'))

    unconfirmed1 = db.Column(db.DECIMAL(20, 8))
    unconfirmed2 = db.Column(db.DECIMAL(20, 8))
    unconfirmed3 = db.Column(db.DECIMAL(20, 8))
    unconfirmed4 = db.Column(db.DECIMAL(20, 8))
    unconfirmed5 = db.Column(db.DECIMAL(20, 8))

    txid1 = db.Column(db.TEXT)
    txid2 = db.Column(db.TEXT)
    txid3 = db.Column(db.TEXT)
    txid4 = db.Column(db.TEXT)
    txid5 = db.Column(db.TEXT)


class BchWalletWork(db.Model):
    __tablename__ = 'bch_walletwork'
    __bind_key__ = 'avengers'
    __table_args__ = {"schema": "avengers_wallet_bch", "useexisting": True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.INTEGER)
    type = db.Column(db.INTEGER)
    amount = db.Column(db.DECIMAL(20, 8))
    sendto = db.Column(db.TEXT)
    comment = db.Column(db.TEXT)
    created = db.Column(db.TIMESTAMP(), default=datetime.utcnow())
    txtcomment = db.Column(db.TEXT)


class BchWalletAddresses(db.Model):
    __tablename__ = 'bch_walletaddresses'
    __bind_key__ = 'avengers'
    __table_args__ = {"schema": "avengers_wallet_bch", "useexisting": True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    bchaddress = db.Column(db.TEXT)
    status = db.Column(db.INTEGER)


class BchWalletFee(db.Model):
    __tablename__ = 'bch_walletfee'
    __bind_key__ = 'avengers'
    __table_args__ = {"schema": "avengers_wallet_bch", "useexisting": True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    bch = db.Column(db.DECIMAL(20, 8))


class TransactionsBch(db.Model):
    __tablename__ = 'bch_transactions'
    __bind_key__ = 'avengers'
    __table_args__ = {"schema": "avengers_wallet_bch", "useexisting": True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    category = db.Column(db.INTEGER)
    user_id = db.Column(db.INTEGER, db.ForeignKey('avengers_user.users.id'))
    senderid = db.Column(db.INTEGER)
    confirmations = db.Column(db.INTEGER)
    txid = db.Column(db.TEXT)
    amount = db.Column(db.DECIMAL(20, 8))
    blockhash = db.Column(db.TEXT)
    timeoft = db.Column(db.INTEGER)
    timerecieved = db.Column(db.INTEGER)
    commentbch = db.Column(db.TEXT)
    otheraccount = db.Column(db.INTEGER)
    address = db.Column(db.TEXT)
    fee = db.Column(db.DECIMAL(20, 8))
    created = db.Column(db.TIMESTAMP(), default=datetime.utcnow())
    balance = db.Column(db.DECIMAL(20, 8))
    orderid = db.Column(db.INTEGER)
    confirmed = db.Column(db.INTEGER)
    confirmed_fee = db.Column(db.DECIMAL(20, 8))
    digital_currency = db.Column(db.INTEGER)


class BtcWallet(db.Model):
    __tablename__ = 'btc_wallet'
    __bind_key__ = 'avengers'
    __table_args__ = {"schema": "avengers_wallet_btc", "useexisting": True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.INTEGER, db.ForeignKey('avengers_user.users.id'))
    currentbalance = db.Column(db.DECIMAL(20, 8))
    address1 = db.Column(db.TEXT)
    address1status = db.Column(db.INTEGER)
    address2 = db.Column(db.TEXT)
    address2status = db.Column(db.INTEGER)
    address3 = db.Column(db.TEXT)
    address3status = db.Column(db.INTEGER)
    locked = db.Column(db.INTEGER)
    transactioncount = db.Column(db.INTEGER)
    unconfirmed = db.Column(db.DECIMAL(20, 8))


class BtcUnconfirmed(db.Model):
    __tablename__ = 'btc_unconfirmed'
    __bind_key__ = 'avengers'
    __table_args__ = {"schema": "avengers_wallet_btc", "useexisting": True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.INTEGER, db.ForeignKey('avengers_user.users.id'))

    unconfirmed1 = db.Column(db.DECIMAL(20, 8))
    unconfirmed2 = db.Column(db.DECIMAL(20, 8))
    unconfirmed3 = db.Column(db.DECIMAL(20, 8))
    unconfirmed4 = db.Column(db.DECIMAL(20, 8))
    unconfirmed5 = db.Column(db.DECIMAL(20, 8))

    txid1 = db.Column(db.TEXT)
    txid2 = db.Column(db.TEXT)
    txid3 = db.Column(db.TEXT)
    txid4 = db.Column(db.TEXT)
    txid5 = db.Column(db.TEXT)


class BtcWalletWork(db.Model):
    __tablename__ = 'btc_walletwork'
    __bind_key__ = 'avengers'
    __table_args__ = {"schema": "avengers_wallet_btc", "useexisting": True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.INTEGER)
    type = db.Column(db.INTEGER)
    amount = db.Column(db.DECIMAL(20, 8))
    sendto = db.Column(db.TEXT)
    comment = db.Column(db.TEXT)
    created = db.Column(db.TIMESTAMP(), default=datetime.utcnow())
    txtcomment = db.Column(db.TEXT)


class BtcWalletAddresses(db.Model):
    __tablename__ = 'btc_walletaddresses'
    __bind_key__ = 'avengers'
    __table_args__ = {"schema": "avengers_wallet_btc", "useexisting": True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    btcaddress = db.Column(db.TEXT)
    status = db.Column(db.INTEGER)


class TransactionsBtc(db.Model):
    __tablename__ = 'btc_transactions'
    __bind_key__ = 'avengers'
    __table_args__ = {"schema": "avengers_wallet_btc", "useexisting": True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.INTEGER, db.ForeignKey('avengers_user.users.id'))
    category = db.Column(db.INTEGER)
    senderid = db.Column(db.INTEGER)
    confirmations = db.Column(db.INTEGER)
    txid = db.Column(db.TEXT)
    amount = db.Column(db.DECIMAL(20, 8))
    blockhash = db.Column(db.TEXT)
    timeoft = db.Column(db.INTEGER)
    timerecieved = db.Column(db.INTEGER)
    commentbtc = db.Column(db.TEXT)
    otheraccount = db.Column(db.INTEGER)
    address = db.Column(db.TEXT)
    fee = db.Column(db.DECIMAL(20, 8))
    created = db.Column(db.TIMESTAMP(), default=datetime.utcnow())
    balance = db.Column(db.DECIMAL(20, 8))
    orderid = db.Column(db.INTEGER)
    confirmed = db.Column(db.INTEGER)
    confirmed_fee = db.Column(db.DECIMAL(20, 8))
    digital_currency = db.Column(db.INTEGER)


class BtcWalletFee(db.Model):
    __tablename__ = 'btc_walletfee'
    __bind_key__ = 'avengers'
    __table_args__ = {"schema": "avengers_wallet_btc", "useexisting": True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    btc = db.Column(db.DECIMAL(20, 8))


class BtcTransOrphan(db.Model):
    __tablename__ = 'btc_transorphan'
    __bind_key__ = 'avengers'
    __table_args__ = {"schema": "avengers_wallet_btc", "useexisting": True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    btc = db.Column(db.DECIMAL(20, 8))
    btcaddress = db.Column(db.TEXT)
    txid = db.Column(db.TEXT)


class MoneroWallet(db.Model):
    __tablename__ = 'monero_wallet'
    __bind_key__ = 'avengers'
    __table_args__ = {"schema": "avengers_wallet_monero", "useexisting": True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.INTEGER, db.ForeignKey('avengers_user.users.id'))
    currentbalance = db.Column(db.DECIMAL(20, 8))
    address1 = db.Column(db.TEXT)
    address1status = db.Column(db.INTEGER)
    locked = db.Column(db.INTEGER)
    transactioncount = db.Column(db.INTEGER)
    unconfirmed = db.Column(db.DECIMAL(20, 8))


class MoneroTransactions(db.Model):
    __tablename__ = 'monero_transactions'
    __bind_key__ = 'avengers'
    __table_args__ = {"schema": "avengers_wallet_monero", "useexisting": True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    category = db.Column(db.INTEGER)
    user_id = db.Column(db.INTEGER, db.ForeignKey('avengers_user.users.id'))
    senderid = db.Column(db.INTEGER)
    confirmations = db.Column(db.INTEGER)
    confirmed = db.Column(db.INTEGER)
    txid = db.Column(db.TEXT)
    amount = db.Column(db.DECIMAL(20, 8))
    balance = db.Column(db.DECIMAL(20, 8))
    block = db.Column(db.INTEGER)
    created = db.Column(db.TIMESTAMP(), default=datetime.utcnow())
    address = db.Column(db.TEXT)
    fee = db.Column(db.DECIMAL(20, 8))
    orderid = db.Column(db.INTEGER)
    digital_currency = db.Column(db.INTEGER)


class MoneroTransOrphan(db.Model):
    __tablename__ = 'monero_transorphan'
    __bind_key__ = 'avengers'
    __table_args__ = {"schema": "avengers_wallet_monero", "useexisting": True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    btc = db.Column(db.DECIMAL(20, 8))
    txid = db.Column(db.TEXT)


class MoneroUnconfirmed(db.Model):
    __tablename__ = 'monero_unconfirmed'
    __bind_key__ = 'avengers'
    __table_args__ = {"schema": "avengers_wallet_monero", "useexisting": True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.INTEGER, db.ForeignKey('avengers_user.users.id'))

    unconfirmed1 = db.Column(db.DECIMAL(20, 8))
    unconfirmed2 = db.Column(db.DECIMAL(20, 8))
    unconfirmed3 = db.Column(db.DECIMAL(20, 8))
    unconfirmed4 = db.Column(db.DECIMAL(20, 8))
    unconfirmed5 = db.Column(db.DECIMAL(20, 8))

    txid1 = db.Column(db.TEXT)
    txid2 = db.Column(db.TEXT)
    txid3 = db.Column(db.TEXT)
    txid4 = db.Column(db.TEXT)
    txid5 = db.Column(db.TEXT)


class MoneroWalletWork(db.Model):
    __tablename__ = 'monero_wallet_work'
    __bind_key__ = 'avengers'
    __table_args__ = {"schema": "avengers_wallet_monero", "useexisting": True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.INTEGER)
    type = db.Column(db.INTEGER)
    amount = db.Column(db.DECIMAL(20, 8))
    sendto = db.Column(db.TEXT)
    created = db.Column(db.TIMESTAMP(), default=datetime.utcnow())
    txnumber = db.Column(db.INTEGER)


class MoneroWalletFee(db.Model):
    __tablename__ = 'monero_walletfee'
    __bind_key__ = 'avengers'
    __table_args__ = {"schema": "avengers_wallet_monero", "useexisting": True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    amount = db.Column(db.DECIMAL(20, 8))


class MoneroWalletAddresses(db.Model):
    __tablename__ = 'moneroaddresses'
    __bind_key__ = 'avengers'
    __table_args__ = {"schema": "avengers_wallet_monero", "useexisting": True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    address = db.Column(db.TEXT)
    status = db.Column(db.INTEGER)


class MoneroBlockHeight(db.Model):
    __tablename__ = 'monero_blockheight'
    __bind_key__ = 'avengers'
    __table_args__ = {"schema": "avengers_wallet_monero", "useexisting": True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    blockheight = db.Column(db.INTEGER)


class SavedPost(db.Model):
    __tablename__ = 'user_saved_posts'
    __bind_key__ = 'avengers'
    __table_args__ = {"schema": "avengers_user", 'useexisting': True}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    created = db.Column(db.TIMESTAMP(), default=datetime.utcnow)
    post_id = db.Column(db.Integer, db.ForeignKey('avengers_post.avengers_posts_posts.id'))


class Subscribed(db.Model):
    __tablename__ = 'subscribed_rooms'
    __bind_key__ = 'avengers'
    __table_args__ = {"schema": "avengers_user", 'useexisting': True}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    subcommon_id = db.Column(db.Integer, db.ForeignKey('avengers_subforum.avengers_subforum_subforum.id'))


class SubForumStats(db.Model):
    __tablename__ = 'avengers_subforum_subforum_Stats'
    __bind_key__ = 'avengers'
    __table_args__ = {"schema": "avengers_subforum", 'useexisting': True}
    id = db.Column(db.Integer, primary_key=True)
    subcommon_name = db.Column(db.String(140))
    subcommon_id = db.Column(db.Integer, db.ForeignKey('avengers_subforum.avengers_subforum_subforum.id'))
    total_posts = db.Column(db.Integer)
    total_exp_subcommon = db.Column(db.Integer)
    members = db.Column(db.Integer)

    def __repr__(self):
        return '<Subcommon {}>'.format(self.subcommon_name)


class SubForumCustom(db.Model):
    __tablename__ = 'avengers_subforum_subforum_custom'
    __bind_key__ = 'avengers'
    __table_args__ = {"schema": "avengers_subforum", 'useexisting': True}
    id = db.Column(db.Integer, primary_key=True)
    subcommon_name = db.Column(db.String(140))
    subcommon_id = db.Column(db.Integer, db.ForeignKey('avengers_subforum.avengers_subforum_subforum.id'))
    banner_image = db.Column(db.String(140))
    mini_image = db.Column(db.String(140))

    def __repr__(self):
        return '<Subcommon {}>'.format(self.subcommon_name)


class SubForumCustomInfoOne(db.Model):
    __tablename__ = 'avengers_subforum_subforum_info_one'
    __bind_key__ = 'avengers'
    __table_args__ = {"schema": "avengers_subforum", 'useexisting': True}
    id = db.Column(db.Integer, primary_key=True)
    subcommon_name = db.Column(db.String(140))
    subcommon_id = db.Column(db.Integer, db.ForeignKey('avengers_subforum.avengers_subforum_subforum.id'))
    enabled = db.Column(db.Integer)
    description = db.Column(db.TEXT)


class PrivateMembers(db.Model):
    __tablename__ = 'avengers_subforum_privatemembers'
    __bind_key__ = 'avengers'
    __table_args__ = {"schema": "avengers_subforum", 'useexisting': True}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    user_name = db.Column(db.String(140))
    subcommon_id = db.Column(db.Integer, db.ForeignKey('avengers_subforum.avengers_subforum_subforum.id'))


class PrivateApplications(db.Model):
    __tablename__ = 'avengers_subforum_privatemembers_application'
    __bind_key__ = 'avengers'
    __table_args__ = {"schema": "avengers_subforum", 'useexisting': True}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    created = db.Column(db.TIMESTAMP(), default=datetime.utcnow)
    user_name = db.Column(db.String(140))
    subcommon_id = db.Column(db.Integer, db.ForeignKey('avengers_subforum.avengers_subforum_subforum.id'))
    message = db.Column(db.TEXT)


# the subforums
class SubForums(db.Model):
    __tablename__ = 'avengers_subforum_subforum'
    __bind_key__ = 'avengers'
    __table_args__ = {"schema": "avengers_subforum", 'useexisting': True}
    id = db.Column(db.Integer, primary_key=True)
    posts = db.relationship('CommonsPost', backref='posts', lazy='dynamic')

    subscription = db.relationship('Subscribed', backref='subscriber', lazy='dynamic')
    privmembers = db.relationship('PrivateMembers', backref='privatemembers', lazy='dynamic')
    privapps = db.relationship('PrivateMembers', backref='privateapps', lazy='dynamic')
    recenttips = db.relationship('RecentTips', backref='recentips', lazy='dynamic')
    subcustom = db.relationship('SubForumCustom', backref='custom', uselist=False)
    custominfoone = db.relationship('SubForumCustomInfoOne', backref='infoone', uselist=False)
    substats = db.relationship('SubForumStats', backref='stats', uselist=False)
    reported_posts = db.relationship('ReportedPosts', backref='reportedposts', lazy='dynamic')
    reported_comments = db.relationship('ReportedComments', backref='reportedcomments', lazy='dynamic')
    mods = db.relationship('Mods', backref='mods', lazy='dynamic')
    banned = db.relationship('Banned', backref='banned', lazy='dynamic')
    muted = db.relationship('Muted', backref='muted', lazy='dynamic')
    room_deleted = db.Column(db.Integer)
    subcommon_name = db.Column(db.String(140))
    # date created
    created = db.Column(db.TIMESTAMP(), default=datetime.utcnow)
    creator_user_id = db.Column(db.Integer)
    creator_user_name = db.Column(db.String(140))
    description = db.Column(db.TEXT)
    type_of_subcommon = db.Column(db.Integer)
    exp_required = db.Column(db.Integer)
    age_required = db.Column(db.Integer)
    allow_text_posts = db.Column(db.Integer)
    allow_url_posts = db.Column(db.Integer)
    allow_image_posts = db.Column(db.Integer)
    total_exp_subcommon = db.Column(db.Integer)
    members = db.Column(db.Integer)
    mini_image = db.Column(db.String(140))

    def __repr__(self):
        return '<Subcommon {}>'.format(self.subcommon_name)


# the comments on posts
class Comments(db.Model):
    __tablename__ = 'avengers_comments_comments'
    __bind_key__ = 'avengers'
    __table_args__ = {"schema": "avengers_comments", 'useexisting': True}

    id = db.Column(db.Integer, primary_key=True)
    # user_name
    user_name = db.Column(db.String(140))
    user_id = db.Column(db.Integer, db.ForeignKey('avengers_user.users.id'))

    # connect for vote commentupvotes
    commons_post_id = db.Column(db.Integer, db.ForeignKey('avengers_post.avengers_posts_posts.id'))

    realid = db.Column(db.String(40))
    created = db.Column(db.TIMESTAMP(), default=datetime.utcnow)

    visible_user_id = db.Column(db.Integer)
    visible_user_name = db.Column(db.String(140))
    userhidden = db.Column(db.Integer)
    body = db.Column(db.TEXT)
    total_exp_commons = db.Column(db.Integer)
    downvotes_on_comment = db.Column(db.Integer)
    upvotes_on_comment = db.Column(db.Integer)
    # reported
    active = db.Column(db.Integer)
    hidden = db.Column(db.Integer)
    # donations
    total_recieved_btc = db.Column(db.DECIMAL(20, 8))
    total_recieved_btc_usd = db.Column(db.DECIMAL(20, 2))
    total_recieved_xmr = db.Column(db.DECIMAL(20, 8))
    total_recieved_xmr_usd = db.Column(db.DECIMAL(20, 2))
    total_recieved_bch = db.Column(db.DECIMAL(20, 8))
    total_recieved_bch_usd = db.Column(db.DECIMAL(20, 2))
    subcommon_id = db.Column(db.Integer)

    # factor how many digits ..6 = 1 million
    _N = 6
    # used for sorting
    thread_timestamp = db.Column(db.TIMESTAMP())
    thread_upvotes = db.Column(db.Integer)
    thread_downvotes = db.Column(db.Integer)

    path = db.Column(db.TEXT, index=True)

    comment_parent_id = db.Column(db.Integer, db.ForeignKey('avengers_comments.avengers_comments_comments.id'))
    replies = db.relationship('Comments', backref=db.backref('parent', remote_side=[id]), lazy='dynamic')

    def save(self):
        db.session.add(self)
        db.session.commit()
        prefix = self.parent.path + '.' if self.parent else ''
        self.path = prefix + '{:0{}d}'.format(self.id, self._N)

        db.session.commit()

    def level(self):
        return len(self.path) // self._N - 1


# the posts
class CommonsPost(db.Model):
    __tablename__ = 'avengers_posts_posts'
    __bind_key__ = 'avengers'
    __table_args__ = {"schema": "avengers_post", 'useexisting': True}

    id = db.Column(db.Integer, primary_key=True)

    user_name = db.Column(db.String(140))
    user_id = db.Column(db.Integer, db.ForeignKey('avengers_user.users.id'))

    visible_user_id = db.Column(db.Integer)
    visible_user_name = db.Column(db.String(140))
    userhidden = db.Column(db.Integer)

    age = db.Column(db.Integer)


    subcommon_id = db.Column(db.Integer, db.ForeignKey('avengers_subforum.avengers_subforum_subforum.id'))

    saved = db.relationship('SavedPost', backref='saved', lazy='dynamic', cascade="all,delete")
    reported_posts = db.relationship('ReportedPosts', backref='postreports', lazy='dynamic', cascade="all,delete")
    thecomments = db.relationship('Comments', backref='postcomments', lazy='dynamic',)
    giveaway_post = db.relationship('GiveawayAll', backref='giveawayall', uselist=False)

    # tips
    xmr_post_tips = db.relationship('XmrPostTips', backref='xmrtips', lazy='dynamic')
    btc_post_tips = db.relationship('BtcPostTips', backref='btctips', lazy='dynamic')
    bch_post_tips = db.relationship('BchPostTips', backref='bchtips', lazy='dynamic')

    # Coins
    post_coins = db.relationship('PostCoins', backref='postcoins', uselist=False)
    post_donations = db.relationship('PostDonations', backref='postdonations',  uselist=False)
    post_promotions = db.relationship('PostPromotions', backref='postpromotions',  uselist=False)

    realid = db.Column(db.String(40))
    created = db.Column(db.TIMESTAMP(), default=datetime.utcnow)
    edited = db.Column(db.TIMESTAMP(), default=datetime.utcnow)

    crawlneed = db.Column(db.Integer)
    type_of_post = db.Column(db.Integer)

    url_image = db.Column(db.TEXT)
    url_title = db.Column(db.TEXT)
    url_of_post = db.Column(db.TEXT)
    url_description = db.Column(db.TEXT)
    url_image_server = db.Column(db.TEXT)

    # the text of post
    post_text = db.Column(db.TEXT)
    image_server_1 = db.Column(db.TEXT)

    subcommon_name = db.Column(db.String(140))
    comment_count = db.Column(db.Integer)
    vote_timestamp = db.Column(db.TIMESTAMP(), default=datetime.utcnow)
    last_active = db.Column(db.TIMESTAMP(), default=datetime.utcnow)
    active = db.Column(db.Integer)
    locked = db.Column(db.Integer)
    hidden = db.Column(db.Integer)
    muted = db.Column(db.Integer)
    downvotes_on_post = db.Column(db.Integer)
    upvotes_on_post = db.Column(db.Integer)
    hotness_rating_now = db.Column(db.Integer)
    total_exp_commons = db.Column(db.Integer)
    highest_exp_reached = db.Column(db.Integer)
    page_views = db.Column(db.Integer)
    sticky = db.Column(db.Integer)

    # origonal id of post
    shared_post = db.Column(db.Integer)

    content_user_name = db.Column(db.String(100))
    content_user_id = db.Column(db.Integer, db.ForeignKey('avengers_user.users.id'))
    creator_anon = db.Column(db.Integer)
    shared_time = db.Column(db.TIMESTAMP(), default=datetime.utcnow)
    shared_thoughts = db.Column(db.TEXT)



class PostPromotions(db.Model):
    __tablename__ = 'avengers_post_promotions'
    __bind_key__ = 'avengers'
    __table_args__ = {"schema": "avengers_post", 'useexisting': True}

    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey('avengers_post.avengers_posts_posts.id'))
    # tipvote coins
    total_recieved_btc = db.Column(db.DECIMAL(20, 8))
    total_recieved_btc_usd = db.Column(db.DECIMAL(20, 2))

    total_recieved_bch = db.Column(db.DECIMAL(20, 8))
    total_recieved_bch_usd = db.Column(db.DECIMAL(20, 2))

    total_recieved_xmr = db.Column(db.DECIMAL(20, 8))
    total_recieved_xmr_usd = db.Column(db.DECIMAL(20, 2))

class PostPromote(db.Model):
    __tablename__ = 'avengers_promotion_post'
    __bind_key__ = 'avengers'
    __table_args__ = {"schema": "avengers_promotion", 'useexisting': True}

    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.TIMESTAMP(), default=datetime.utcnow())

    # from to
    created_user_id = db.Column(db.Integer)
    created_user_name = db.Column(db.String(140))

    # identify forum, post, and comment
    subcommon_id = db.Column(db.Integer)
    subcommon_name = db.Column(db.String(140))
    post_id = db.Column(db.Integer)

    # amounts
    amount_btc = db.Column(db.DECIMAL(20, 8))
    amount_bch = db.Column(db.DECIMAL(20, 8))
    amount_xmr = db.Column(db.DECIMAL(20, 8))

    amount_usd = db.Column(db.DECIMAL(20, 2))


class PostDonations(db.Model):
    __tablename__ = 'avengers_post_donations'
    __bind_key__ = 'avengers'
    __table_args__ = {"schema": "avengers_post", 'useexisting': True}

    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey('avengers_post.avengers_posts_posts.id'))
    # promotions
    total_recieved_btc = db.Column(db.DECIMAL(20, 8))
    total_recieved_btc_usd = db.Column(db.DECIMAL(20, 2))

    total_recieved_bch = db.Column(db.DECIMAL(20, 8))
    total_recieved_bch_usd = db.Column(db.DECIMAL(20, 2))

    total_recieved_xmr = db.Column(db.DECIMAL(20, 8))
    total_recieved_xmr_usd = db.Column(db.DECIMAL(20, 2))


class PostCoins(db.Model):
    __tablename__ = 'avengers_post_coins'
    __bind_key__ = 'avengers'
    __table_args__ = {"schema": "avengers_post", 'useexisting': True}

    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey('avengers_post.avengers_posts_posts.id'))

    coin_1 = db.Column(db.Integer)
    coin_2 = db.Column(db.Integer)
    coin_3 = db.Column(db.Integer)
    coin_4 = db.Column(db.Integer)
    coin_5 = db.Column(db.Integer)
    coin_6 = db.Column(db.Integer)
    coin_7 = db.Column(db.Integer)
    coin_8 = db.Column(db.Integer)
    coin_9 = db.Column(db.Integer)
    coin_10 = db.Column(db.Integer)


class Coins(db.Model):
    __tablename__ = 'coins'
    __bind_key__ = 'avengers'
    __table_args__ = {"schema": "avengers_coins", 'useexisting': True}

    id = db.Column(db.Integer, primary_key=True)
    image_thumbnail = db.Column(db.String(300))
    created = db.Column(db.TIMESTAMP())
    # coin info
    coin_name = db.Column(db.String(140))
    coin_rarity = db.Column(db.Integer)
    coin_description = db.Column(db.TEXT)
    points_value = db.Column(db.Integer)


class UserCoins(db.Model):
    __tablename__ = 'usercoins'
    __bind_key__ = 'avengers'
    __table_args__ = {"schema": "avengers_coins", 'useexisting': True}

    id = db.Column(db.Integer, primary_key=True)
    image_thumbnail = db.Column(db.String(300))

    user_name = db.Column(db.String(140))
    user_id = db.Column(db.Integer, db.ForeignKey('avengers_user.users.id'))

    obtained = db.Column(db.TIMESTAMP())
    quantity = db.Column(db.Integer)

    # coin info
    coin_name = db.Column(db.String(140))
    coin_rarity = db.Column(db.Integer)
    coin_description = db.Column(db.TEXT)
    points_value = db.Column(db.Integer)


class DisplayCoins(db.Model):
    __tablename__ = 'displayrewardcoins'
    __bind_key__ = 'avengers'
    __table_args__ = {"schema": "avengers_coins", 'useexisting': True}

    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.TIMESTAMP())
    user_name = db.Column(db.String(140))
    user_id = db.Column(db.Integer, db.ForeignKey('avengers_user.users.id'))

    # coin info
    image_thumbnail_0 = db.Column(db.String(300))
    coin_name_0 = db.Column(db.String(140))
    coin_rarity_0 = db.Column(db.Integer)
    coin_description_0 = db.Column(db.TEXT)
    points_value_0 = db.Column(db.Integer)

    # coin info
    image_thumbnail_1 = db.Column(db.String(300))
    coin_name_1 = db.Column(db.String(140))
    coin_rarity_1 = db.Column(db.Integer)
    coin_description_1 = db.Column(db.TEXT)
    points_value_1 = db.Column(db.Integer)

    seen_by_user = db.Column(db.Integer)
    new_user_level = db.Column(db.Integer)


class TempUrl(db.Model):
    __tablename__ = 'temp_url'
    __bind_key__ = 'avengers'
    __table_args__ = {"schema": "avengers_subforum", 'useexisting': True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.TEXT)
    user_id = db.Column(db.INTEGER)
    timestamp = db.Column(db.TIMESTAMP(), default=datetime.utcnow())
    url = db.Column(db.TEXT)
    title = db.Column(db.TEXT)
    description = db.Column(db.TEXT)
    image = db.Column(db.TEXT)
    subcommon_name = db.Column(db.String(140))
    subcommon_id = db.Column(db.Integer)


class Notifications(db.Model):
    __tablename__ = 'avengers_msg_notifications'
    __bind_key__ = 'avengers'
    __table_args__ = {"schema": "avengers_main", 'useexisting': True}

    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.TIMESTAMP(), default=datetime.utcnow())
    read = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('avengers_user.users.id'))
    user_name = db.Column(db.String(140))
    subcommon_id = db.Column(db.Integer)
    subcommon_name = db.Column(db.String(140))
    post_id = db.Column(db.Integer)
    comment_id = db.Column(db.Integer)
    msg_type = db.Column(db.Integer)


class BtcPrices(db.Model):
    __tablename__ = 'prices_btc'
    __bind_key__ = 'avengers'
    __table_args__ = {"schema": "avengers_main", 'useexisting': True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    price = db.Column(db.DECIMAL(50, 2))


class MoneroPrices(db.Model):
    __tablename__ = 'prices_monero'
    __bind_key__ = 'avengers'
    __table_args__ = {"schema": "avengers_main", 'useexisting': True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    price = db.Column(db.DECIMAL(50, 2))


class BchPrices(db.Model):
    __tablename__ = 'prices_bch'
    __bind_key__ = 'avengers'
    __table_args__ = {"schema": "avengers_main", 'useexisting': True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    price = db.Column(db.DECIMAL(50, 2))


class LtcPrices(db.Model):
    __tablename__ = 'prices_ltc'
    __bind_key__ = 'avengers'
    __table_args__ = {"schema": "avengers_main", 'useexisting': True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    price = db.Column(db.DECIMAL(50, 2))


# Posts that have been reported
class ReportedPosts(db.Model):
    __tablename__ = 'avengers_subforum_reported_posts'
    __bind_key__ = 'avengers'
    __table_args__ = {"schema": "avengers_subforum", 'useexisting': True}

    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.TIMESTAMP(), default=datetime.utcnow)
    reporter_id = db.Column(db.Integer)
    reporter_user_name = db.Column(db.String(140))

    subcommon_id = db.Column(db.Integer, db.ForeignKey('avengers_subforum.avengers_subforum_subforum.id'))
    subcommon_name = db.Column(db.String(140))

    post_id = db.Column(db.Integer, db.ForeignKey('avengers_post.avengers_posts_posts.id'))
    poster_user_id = db.Column(db.Integer)
    poster_user_name = db.Column(db.String(140))
    poster_visible_user_id = db.Column(db.Integer)
    poster_visible_user_name = db.Column(db.String(140))


# Posts that have been reported
class ReportedComments(db.Model):
    __tablename__ = 'avengers_subforum_reported_comments'
    __bind_key__ = 'avengers'
    __table_args__ = {"schema": "avengers_subforum", 'useexisting': True}

    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.TIMESTAMP(), default=datetime.utcnow)
    reporter_id = db.Column(db.Integer)
    reporter_user_name = db.Column(db.String(140))
    subcommon_id = db.Column(db.Integer, db.ForeignKey('avengers_subforum.avengers_subforum_subforum.id'))
    subcommon_name = db.Column(db.String(140))

    comment_id = db.Column(db.Integer)
    comment_body = db.Column(db.TEXT)
    commenter_user_id = db.Column(db.Integer)
    commenter_user_name = db.Column(db.String(140))
    commenter_visible_user_id = db.Column(db.Integer)
    commenter_visible_user_name = db.Column(db.String(140))


# banned sub users
class Mods(db.Model):
    __tablename__ = 'avengers_subforum_mods'
    __bind_key__ = 'avengers'
    __table_args__ = {"schema": "avengers_subforum", 'useexisting': True}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    user_name = db.Column(db.String(140))

    subcommon_id = db.Column(db.Integer, db.ForeignKey('avengers_subforum.avengers_subforum_subforum.id'))


# banned sub users
class Banned(db.Model):
    __tablename__ = 'avengers_subforum_banned'
    __bind_key__ = 'avengers'
    __table_args__ = {"schema": "avengers_subforum", 'useexisting': True}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    user_name = db.Column(db.String(140))

    subcommon_id = db.Column(db.Integer, db.ForeignKey('avengers_subforum.avengers_subforum_subforum.id'))


# banned sub users
class Muted(db.Model):
    __tablename__ = 'avengers_subforum_muted'
    __bind_key__ = 'avengers'
    __table_args__ = {"schema": "avengers_subforum", 'useexisting': True}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    user_name = db.Column(db.String(140))

    subcommon_id = db.Column(db.Integer, db.ForeignKey('avengers_subforum.avengers_subforum_subforum.id'))
    muted_start = db.Column(db.TIMESTAMP(), default=datetime.utcnow)
    muted_end = db.Column(db.TIMESTAMP(), default=datetime.utcnow)




class BtcCommentTips(db.Model):
    __tablename__ = 'avengers_tips_btc_comments'
    __bind_key__ = 'avengers'
    __table_args__ = {"schema": "avengers_tips", 'useexisting': True}

    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.TIMESTAMP(), default=datetime.utcnow())

    # from to
    created_user_id = db.Column(db.Integer)
    created_user_name = db.Column(db.String(140))
    recieved_user_id = db.Column(db.Integer)
    recieved_user_name = db.Column(db.String(140))

    # identify forum, post, and comment
    subcommon_id = db.Column(db.Integer)
    subcommon_name = db.Column(db.String(140))
    post_id = db.Column(db.Integer)
    comment_id = db.Column(db.Integer)

    # amounts
    amount_btc = db.Column(db.DECIMAL(20, 8))
    amount_usd = db.Column(db.DECIMAL(20, 2))


class XmrCommentTips(db.Model):
    __tablename__ = 'avengers_tips_xmr_comments'
    __bind_key__ = 'avengers'
    __table_args__ = {"schema": "avengers_tips", 'useexisting': True}

    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.TIMESTAMP(), default=datetime.utcnow())

    # from to
    created_user_id = db.Column(db.Integer)
    created_user_name = db.Column(db.String(140))
    recieved_user_id = db.Column(db.Integer)
    recieved_user_name = db.Column(db.String(140))

    # identify forum, post, and comment
    subcommon_id = db.Column(db.Integer)
    subcommon_name = db.Column(db.String(140))
    post_id = db.Column(db.Integer)
    comment_id = db.Column(db.Integer)

    # amounts
    amount_xmr = db.Column(db.DECIMAL(20, 8))
    amount_usd = db.Column(db.DECIMAL(20, 2))


class BchCommentTips(db.Model):
    __tablename__ = 'avengers_tips_bch_comments'
    __bind_key__ = 'avengers'
    __table_args__ = {"schema": "avengers_tips", 'useexisting': True}

    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.TIMESTAMP(), default=datetime.utcnow())

    # from to
    created_user_id = db.Column(db.Integer)
    created_user_name = db.Column(db.String(140))
    recieved_user_id = db.Column(db.Integer)
    recieved_user_name = db.Column(db.String(140))

    # identify forum, post, and comment
    subcommon_id = db.Column(db.Integer)
    subcommon_name = db.Column(db.String(140))
    post_id = db.Column(db.Integer)
    comment_id = db.Column(db.Integer)

    # amounts
    amount_bch = db.Column(db.DECIMAL(20, 8))
    amount_usd = db.Column(db.DECIMAL(20, 2))


class BtcPostTips(db.Model):
    __tablename__ = 'avengers_tips_btc_posts'
    __bind_key__ = 'avengers'
    __table_args__ = {"schema": "avengers_tips", 'useexisting': True}

    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.TIMESTAMP(), default=datetime.utcnow())

    # from to
    created_user_id = db.Column(db.Integer)
    created_user_name = db.Column(db.String(140))
    recieved_user_id = db.Column(db.Integer)
    recieved_user_name = db.Column(db.String(140))

    # identify forum, post, and comment
    subcommon_id = db.Column(db.Integer)
    subcommon_name = db.Column(db.String(140))
    post_id = db.Column(db.Integer, db.ForeignKey('avengers_post.avengers_posts_posts.id'))
    # amounts
    amount_btc = db.Column(db.DECIMAL(20, 8))
    amount_usd = db.Column(db.DECIMAL(20, 2))


class XmrPostTips(db.Model):
    __tablename__ = 'avengers_tips_xmr_posts'
    __bind_key__ = 'avengers'
    __table_args__ = {"schema": "avengers_tips", 'useexisting': True}

    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.TIMESTAMP(), default=datetime.utcnow())
    # from to
    created_user_id = db.Column(db.Integer)
    created_user_name = db.Column(db.String(140))
    recieved_user_id = db.Column(db.Integer)
    recieved_user_name = db.Column(db.String(140))

    # identify forum, post, and comment
    subcommon_id = db.Column(db.Integer)
    subcommon_name = db.Column(db.String(140))
    post_id = db.Column(db.Integer,  db.ForeignKey('avengers_post.avengers_posts_posts.id'))

    # amounts
    amount_xmr = db.Column(db.DECIMAL(20, 8))
    amount_usd = db.Column(db.DECIMAL(20, 2))


class BchPostTips(db.Model):
    __tablename__ = 'avengers_tips_bch_posts'
    __bind_key__ = 'avengers'
    __table_args__ = {"schema": "avengers_tips", 'useexisting': True}

    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer,  db.ForeignKey('avengers_post.avengers_posts_posts.id'))

    created = db.Column(db.TIMESTAMP(), default=datetime.utcnow())
    # from to
    created_user_id = db.Column(db.Integer)
    created_user_name = db.Column(db.String(140))
    recieved_user_id = db.Column(db.Integer)
    recieved_user_name = db.Column(db.String(140))

    # identify forum, post, and comment
    subcommon_id = db.Column(db.Integer)
    subcommon_name = db.Column(db.String(140))

    # amounts
    amount_bch = db.Column(db.DECIMAL(20, 8))
    amount_usd = db.Column(db.DECIMAL(20, 2))


class RecentTips(db.Model):
    __tablename__ = 'avengers_tips_stats_recent'
    __bind_key__ = 'avengers'
    __table_args__ = {"schema": "avengers_tips", 'useexisting': True}

    id = db.Column(db.Integer, primary_key=True)
    # identify forum, post, and comment
    subcommon_id = db.Column(db.Integer, db.ForeignKey('avengers_subforum.avengers_subforum_subforum.id'))
    post_id = db.Column(db.Integer)
    comment_id = db.Column(db.Integer)

    created = db.Column(db.TIMESTAMP(), default=datetime.utcnow())
    subcommon_name = db.Column(db.String(140))
    created_user_id = db.Column(db.Integer)
    created_user_name = db.Column(db.String(140))
    recieved_user_id = db.Column(db.Integer)
    recieved_user_name = db.Column(db.String(140))

    # amounts
    currency_type = db.Column(db.Integer)
    amount_btc = db.Column(db.DECIMAL(20, 8))
    amount_bch = db.Column(db.DECIMAL(20, 8))
    amount_xmr = db.Column(db.DECIMAL(20, 8))
    amount_usd = db.Column(db.DECIMAL(20, 2))


class UserStatsXMR(db.Model):
    __tablename__ = 'user_stats_xmr'
    __bind_key__ = 'avengers'
    __table_args__ = {"schema": "avengers_user", 'useexisting': True}

    id = db.Column(db.INTEGER, autoincrement=True, primary_key=True)
    user_name = db.Column(db.TEXT)
    user_id = db.Column(db.Integer, db.ForeignKey('avengers_user.users.id'))
    # given to posters/commenters
    total_donated_to_postcomments_xmr = db.Column(db.DECIMAL(20, 8))
    total_donated_to_postcomments_usd = db.Column(db.DECIMAL(20, 2))
    # recieved from posting
    total_recievedfromposts_xmr = db.Column(db.DECIMAL(20, 8))
    total_recievedfromposts_usd = db.Column(db.DECIMAL(20, 2))
    # recieved from comments
    total_recievedfromcomments_xmr = db.Column(db.DECIMAL(20, 8))
    total_recievedfromcomments_usd = db.Column(db.DECIMAL(20, 2))
    # given to charities
    total_donated_to_cause_xmr = db.Column(db.DECIMAL(20, 8))
    total_donated_to_cause_usd = db.Column(db.DECIMAL(20, 2))


class UserStatsBTC(db.Model):
    __tablename__ = 'user_stats_btc'
    __bind_key__ = 'avengers'
    __table_args__ = {"schema": "avengers_user", 'useexisting': True}

    id = db.Column(db.INTEGER, autoincrement=True, primary_key=True)
    user_name = db.Column(db.TEXT)
    user_id = db.Column(db.Integer, db.ForeignKey('avengers_user.users.id'))
    # given to posters/commenters
    total_donated_to_postcomments_btc = db.Column(db.DECIMAL(20, 8))
    total_donated_to_postcomments_usd = db.Column(db.DECIMAL(20, 2))
    # recieved from posting
    total_recievedfromposts_btc = db.Column(db.DECIMAL(20, 8))
    total_recievedfromposts_usd = db.Column(db.DECIMAL(20, 2))
    # recieved from comments
    total_recievedfromcomments_btc = db.Column(db.DECIMAL(20, 8))
    total_recievedfromcomments_usd = db.Column(db.DECIMAL(20, 2))
    # given to charities
    total_donated_to_cause_btc = db.Column(db.DECIMAL(20, 8))
    total_donated_to_cause_usd = db.Column(db.DECIMAL(20, 2))


class UserStatsBCH(db.Model):
    __tablename__ = 'user_stats_bch'
    __bind_key__ = 'avengers'
    __table_args__ = {"schema": "avengers_user", 'useexisting': True}

    id = db.Column(db.INTEGER, autoincrement=True, primary_key=True)
    user_name = db.Column(db.TEXT)
    user_id = db.Column(db.Integer, db.ForeignKey('avengers_user.users.id'))
    # given to posters/commenters
    total_donated_to_postcomments_bch = db.Column(db.DECIMAL(20, 8))
    total_donated_to_postcomments_usd = db.Column(db.DECIMAL(20, 2))
    # recieved from posting
    total_recievedfromposts_bch = db.Column(db.DECIMAL(20, 8))
    total_recievedfromposts_usd = db.Column(db.DECIMAL(20, 2))
    # recieved from comments
    total_recievedfromcomments_bch = db.Column(db.DECIMAL(20, 8))
    total_recievedfromcomments_usd = db.Column(db.DECIMAL(20, 2))
    # given to charities
    total_donated_to_cause_bch = db.Column(db.DECIMAL(20, 8))
    total_donated_to_cause_usd = db.Column(db.DECIMAL(20, 2))


class ExpTable(db.Model):
    __tablename__ = 'user_exp'
    __bind_key__ = 'avengers'
    __table_args__ = {"schema": "avengers_user", 'useexisting': True}

    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('avengers_user.users.id'))
    type = db.Column(db.INTEGER)
    amount = db.Column(db.INTEGER)
    created = db.Column(db.TIMESTAMP())


class PgpKey(db.Model):
    __tablename__ = 'user_pgpkey'
    __bind_key__ = 'avengers'
    __table_args__ = {"schema": "avengers_user", 'useexisting': True}

    id = db.Column(db.Integer, autoincrement=True, primary_key=True, unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('avengers_user.users.id'))
    userkey = db.Column(db.TEXT)


class UserTimers(db.Model):
    __tablename__ = 'user_timers'
    __bind_key__ = 'avengers'
    __table_args__ = {"schema": "avengers_user", 'useexisting': True}

    id = db.Column(db.INTEGER, autoincrement=True, primary_key=True)
    user_name = db.Column(db.TEXT)
    user_id = db.Column(db.Integer)
    account_created = db.Column(db.TIMESTAMP(), default=datetime.utcnow())
    last_post = db.Column(db.TIMESTAMP(), default=datetime.utcnow())
    last_common_creation = db.Column(db.TIMESTAMP(), default=datetime.utcnow())
    last_comment = db.Column(db.TIMESTAMP(), default=datetime.utcnow())
    last_report = db.Column(db.TIMESTAMP(), default=datetime.utcnow())


class UserPublicInfo(db.Model):
    __tablename__ = 'user_public_info'
    __bind_key__ = 'avengers'
    __table_args__ = {"schema": "avengers_user", 'useexisting': True}

    id = db.Column(db.INTEGER, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('avengers_user.users.id'))
    bio = db.Column(db.TEXT)
    short_bio = db.Column(db.TEXT)


class Followers(db.Model):
    __tablename__ = 'followers'
    __bind_key__ = 'avengers'
    __table_args__ = {"schema": "avengers_user", 'useexisting': True}

    id = db.Column(db.INTEGER, autoincrement=True, primary_key=True)
    follower_id = db.Column(db.Integer, db.ForeignKey('avengers_user.users.id'))
    followed_id = db.Column(db.Integer, db.ForeignKey('avengers_user.users.id'))


class UserStats(db.Model):
    __tablename__ = 'user_stats_common'
    __bind_key__ = 'avengers'
    __table_args__ = {"schema": "avengers_user", 'useexisting': True}

    id = db.Column(db.INTEGER, autoincrement=True, primary_key=True)
    user_name = db.Column(db.TEXT)
    user_id = db.Column(db.Integer, db.ForeignKey('avengers_user.users.id'))
    comment_upvotes = db.Column(db.INTEGER)
    comment_downvotes = db.Column(db.INTEGER)
    post_upvotes = db.Column(db.INTEGER)
    post_downvotes = db.Column(db.INTEGER,)
    total_posts = db.Column(db.INTEGER)
    total_comments = db.Column(db.INTEGER)
    user_level = db.Column(db.INTEGER)
    user_exp = db.Column(db.INTEGER)
    user_width_next_level = db.Column(db.String)


class User(db.Model):
    __tablename__ = 'users'
    __bind_key__ = 'avengers'
    __table_args__ = {"schema": "avengers_user", 'useexisting': True}

    id = db.Column(db.Integer, autoincrement=True, primary_key=True, unique=True)

    user_name = db.Column(db.TEXT)
    password_hash = db.Column(db.TEXT)
    member_since = db.Column(db.TIMESTAMP(), default=datetime.utcnow())
    wallet_pin = db.Column(db.TEXT)
    profileimage = db.Column(db.TEXT)
    bannerimage = db.Column(db.TEXT)
    last_seen = db.Column(db.TIMESTAMP(), default=datetime.utcnow())
    admin = db.Column(db.INTEGER)
    admin_role = db.Column(db.INTEGER)
    fails = db.Column(db.INTEGER)
    locked = db.Column(db.INTEGER)
    anon_id = db.Column(db.TEXT)
    anon_mode = db.Column(db.INTEGER)
    over_age = db.Column(db.BOOLEAN)
    email = db.Column(db.TEXT)
    followed = db.relationship('User',
                               secondary='avengers_user.followers',
                               primaryjoin=Followers.follower_id == id,
                               secondaryjoin=Followers.followed_id == id,
                               backref=db.backref('followers', lazy='dynamic'),
                               lazy='dynamic',
                               cascade="all,delete")
    contentownerposts = db.relationship('CommonsPost', backref='contentownerposts', lazy='dynamic', primaryjoin="User.id == CommonsPost.content_user_id")
    userposts = db.relationship('CommonsPost', backref='userposts', lazy='dynamic', primaryjoin="User.id == CommonsPost.user_id")
    usercomments = db.relationship('Comments', backref='usercomments', lazy='dynamic', primaryjoin="User.id == Comments.user_id")
    coins_user_coins = db.relationship('UserCoins', backref='usercoins', lazy='dynamic', cascade="all,delete")
    coins_display_user_coins = db.relationship('DisplayCoins', backref='displaycoins', cascade="all,delete")
    main_notes = db.relationship('Notifications', backref='notes', lazy='dynamic', cascade="all,delete")
    user_exptable = db.relationship('ExpTable', backref='exp', lazy='dynamic', cascade="all,delete")
    userpublicinfo = db.relationship('UserPublicInfo', backref='userinfo', uselist=False, cascade="all,delete")
    user_stats_common = db.relationship('UserStats', backref='userstats', uselist=False, cascade="all,delete")
    user_pgp_key = db.relationship('PgpKey', backref='pgp', uselist=False, cascade="all,delete")

    # bch wallet
    bch = db.relationship('BchWallet', backref='bch', uselist=False)
    user_bch_transactions = db.relationship('TransactionsBch', backref='user_bch_transactions', lazy='dynamic')
    user_bch_unconfirmed = db.relationship('BchUnconfirmed', backref='user_bch_unconfirmed', lazy='dynamic')

    # btc wallet
    btc = db.relationship('BtcWallet', backref='btc', uselist=False)
    user_btc_transactions = db.relationship('TransactionsBtc', backref='user_btc_transactions', lazy='dynamic')
    user_btc_unconfirmed = db.relationship('BtcUnconfirmed', backref='user_btc_unconfirmed', lazy='dynamic')

    # xmr wallet
    xmr = db.relationship('MoneroWallet', backref='xmr', uselist=False)
    user_xmr_transactions = db.relationship('MoneroTransactions', backref='user_xmr_transactions', lazy='dynamic')
    user_xmr_unconfirmed = db.relationship('MoneroUnconfirmed', backref='user_xmr_unconfirmed', lazy='dynamic')

    def __init__(self,
                 user_name,
                 password_hash,
                 wallet_pin,
                 member_since,
                 profileimage,
                 bannerimage,
                 bio,
                 last_seen,
                 admin,
                 admin_role,
                 fails,
                 locked,
                 anon_id,
                 anon_mode,
                 over_age
                 ):

        self.user_name = user_name
        self.password_hash = password_hash
        self.wallet_pin = wallet_pin
        self.member_since = member_since
        self.profileimage = profileimage
        self.bannerimage = bannerimage
        self.bio = bio
        self.last_seen = last_seen
        self.admin = admin
        self.admin_role = admin_role
        self.fails = fails
        self.locked = locked
        self.anon_id = anon_id
        self.anon_mode = anon_mode
        self.over_age = over_age

