from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField, RadioField
# from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import Required


class ReportForm(FlaskForm):
    institution = StringField('Institution Name', validators=[Required()])
    department = SelectField('Department',
                             choices=[('ict', 'ICT'),
                                      ('finance', 'Finance'),
                                      ('admin', 'Administration'),
                                      ('procurement', 'Procurement')],
                             validators=[Required()])

    category = RadioField('Type of Institution',
                          choices=[('private', 'Private'),
                                   ('public', 'Public')],
                          validators=[Required()])

    location = SelectField('Location',
                           choices=[('westlands', 'Westlands'),
                                    ('dagorettiN', 'Dagoretti North'),
                                    ('dagorettiS', 'Dagoretti South'),
                                    ('langata', 'Langata'),
                                    ('kibra', 'Kibra'),
                                    ('roysa', 'Roysambu'),
                                    ('kasarani', 'Kasarani'),
                                    ('ruaraka', 'Ruaraka'),
                                    ('embakasiN', 'Embakasi North'),
                                    ('embakasiS', 'Embakasi South'),
                                    ('embakasiC', 'Embakasi Central'),
                                    ('embakasiE', 'Embakasi East'),
                                    ('embakasiW', 'Embakasi West'),
                                    ('makadara', 'Makadara'),
                                    ('kamkunji', 'Kamkunji'),
                                    ('starehe', 'Starehe'),
                                    ('mathare', 'Mathare')],
                           validators=[Required()])

    title = RadioField('Type of crime', choices=[('bribe', 'Bribery'),
                                                 ('bad', 'Bad Services'),
                                                 ('racism', 'Racism'),
                                                 ('nepotism', 'Nepotism'),
                                                 ('tribalism', 'Tribalism'),
                                                 ('harrasment', 'Harrasment')],
                       validators=[Required()])

    description = TextAreaField('Describe Crime', validators=[Required()])
    upvote = StringField('Upvote', validators=[Required()])
    downvote = StringField('Downvote', validators=[Required()])
    submit = SubmitField('Submit')


class CommentForm(FlaskForm):
    comment = TextAreaField('Comment', validators=[Required()])
    submit = SubmitField('Submit')
