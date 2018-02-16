from flask import render_template, request, redirect, url_for, flash
from . import main
from .forms import ReportForm, CommentForm, VerifyForm, RecommendForm
from ..models import Reports, Comments, Community, Recommends
from flask_login import login_required, current_user
from ..email import mail_message
from .. import db, photos


@main.route('/', methods=['GET', 'POST'])
def index():
    """
    This function renders out home page and all its data
    """
    test = "Working"
    reports = Reports.query.all()
    report_form = ReportForm()
    recommends = Recommends.query.all()
    recommend_form = RecommendForm()
    community = Community.query.all()

# For report
    if report_form.validate_on_submit():
        location = report_form.location.data
        institution = report_form.institution.data
        department = report_form.department.data
        category = report_form.category.data
        title = report_form.title.data
        description = report_form.description.data
        if 'photo' in request.files:
            filename = photos.save(request.files['photo'])
            path = f'photos/{filename}'
            report.pic_path = path
            db.session.commit()
            new_report = Reports(location=location,
                                 institution=institution,
                                 department=department,
                                 category=category,
                                 title=title,
                                 description=description)
            db.session.add(new_report)
            db.session.commit()
            for person in community:
                mail_message("New Report!", "email/new_report", person.email)

            return redirect(url_for('main.index'))
        else:
            new_report = Reports(location=location,
                                 institution=institution,
                                 department=department,
                                 category=category,
                                 title=title,
                                 description=description)
        db.session.add(new_report)
        db.session.commit()
        flash(
            'Thank you for posting a report. We wil verify. Visit site to track update on post.')
        return redirect(url_for('main.index'))

# For recommends
    if recommend_form.validate_on_submit():
        location = recommend_form.location.data
        institution = recommend_form.institution.data
        department = recommend_form.department.data
        category = recommend_form.category.data
        title = recommend_form.title.data
        description = report_form.description.data
        if 'photo' in request.files:
            filename = photos.save(request.files['photo'])
            path = f'photos/{filename}'
            recommends.pic_path = path
            db.session.commit()
            new_recommends = Recommends(location=location,
                                        institution=institution,
                                        department=department,
                                        category=category,
                                        title=title,
                                        description=description)
            db.session.add(new_recommends)
            db.session.commit()
            for person in community:
                mail_message("New Report!", "email/new_report", person.email)

            return redirect(url_for('main.index'))
        else:
            new_recommends = Recommends(location=location,
                                        institution=institution,
                                        department=department,
                                        category=category,
                                        title=title,
                                        description=description)
        db.session.add(new_recommends)
        db.session.commit()
        flash(
            'Thank you for posting a report. We wil verify. Visit site to track update on post.')
        return redirect(url_for('main.index'))

    return render_template('index.html',
                           reports=reports,
                           test=test,
                           recommend_form=recommend_form,
                           report_form=report_form)


@main.route('/reportForm', methods=['GET', 'POST'])
def reportForm():

    return redirect(url_for('index') + '#myModal')


@main.route('/recommendForm', methods=['GET', 'POST'])
def recommendForm():

    return redirect(url_for('index') + '#myModal2')


@main.route('/reports', methods=['GET', 'POST'])
# @login_required
def report():
    # TODO: Add voting to this new page. So that comm members can vote.
    reports = Reports.query.all()
    verify = VerifyForm()
    # How to add and commit just one property to a class
    if verify.validate_on_submit():
        verification = Reports.query.filter_by(id=id).update(
            {"verification": verify.verification.data})
        db.session.add(verification)
        db.session.commit()
    return render_template('reports.html', reports=reports, verify=verify)


@main.route('/report/<int:id>', methods=['POST'])
@login_required
def update_report(id):
    report = Reports.query.filter_by(id).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        report.pic_path = path
        db.session.commit()
    return redirect(url_for('main.new'))


@main.route('/comment<int:id>')
@login_required
def comments(id):
    comment_form = CommentForm()
    report = Reports.query.filter_by(id=id)

    if comment_form.validate_on_submit():
        comment = comment_form.comment.data
        new_comment = Comments(comment=comment, user=current_user)
        db.session.commit(new_comment)
        return redirect(url_for('main.index'))

    return render_template('comments.html', report=report,
                           comment_form=comment_form)
