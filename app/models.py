from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime


@login_manager.user_loader
def load_user(community_id):
    return Community.query.get(int(community_id))


class Community(UserMixin, db.Model):
    """
    The Community class defines users who can verify and heat-map reported claims
    """

    __tablename__ = 'community_members'

    id = id.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255))
    password_hash = db.Column(db.String(255))
    reports = db.relationship("Reports", backref="users", lazy="dynamic")
    comments = db.relationship("Comments", backref="users")

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'Community{self.username}'


class Reports(db.Model):

    __tablename__ = "reports"

    id = id.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(255))
    institution = db.Column(db.String(255))
    department = db.Column(db.String(255))
    category = db.Column(db.String(255))
    title = db.Column(db.String(255))
    description = db.Column(db.String())
    pic_path = db.Column(db.String)
    video_path = db.Column(db.String)
    upvote = db.Column(db.Integer)
    downvote = db.Column(db.Integer)
    posted = db.Column(db.DateTime, default=datetime.utcnow)
    community_id = db.Column(db.Integer, db.ForeignKey("community.id"))

    def __init__(self,
                 location,
                 institution,
                 department,
                 category,
                 title,
                 description,
                 pic_path,
                 video_path,
                 upvote,
                 downvote,
                 posted,
                 community_id):

        self.location = location
        self.institution = institution
        self.department = department
        self.category = category
        self.title = title
        self.description = description
        self.pic_path = pic_path
        self.video_path = video_path
        self.upvote = upvote
        self.downvote = downvote
        self.posted = posted
        self.community_id = community_id

        def save_report(self):
            db.session.add(self)
            db.session.commit()


class Comments(db.Model):
    '''
    Comment class that creates instances of Comments class that will be
    attached to a particular report
    '''
    __tablename__ = 'comments'

    # add columns
    id = db.Column(db. Integer, primary_key=True)
    comment = db.Column(db.String(255))
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    community_id = db.Column(db.Integer, db.ForeignKey("community.id"))
    report_id = db.Column(db.Integer, db.ForeignKey("report.id"))

    def __init__(self, comment, date_posted, community_id):
        self.comment = comment
        self.date_posted = date_posted
        self.community_id = community_id

    def save_comment(self):
        '''
        Save the comments per reports
        '''
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(self, id):
        comment = Comments.query.order_by(
            Comments.date_posted.desc()).filter_by(report_id=id).all()
        return comment