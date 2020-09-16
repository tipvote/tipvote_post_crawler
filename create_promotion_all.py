from app import db
from app.models import GiveawayAll
from datetime import datetime, timedelta


def creategiveaway():
    now = datetime.utcnow()
    week = datetime.utcnow() + timedelta(days=7)
    newgiveaway = GiveawayAll(
            post_id=2564,
            total_usd=100,
            last_promotion=now,
            start_promotion=now,
            end_promotion=week,
            leader_user_id=1,
            leader_user_name='tipvote',

    )
    db.session.add(newgiveaway)
    db.session.commit()


if __name__ == '__main__':
    creategiveaway()
