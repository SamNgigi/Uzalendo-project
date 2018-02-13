from flask import render_template, request, redirect, url_for
from . import main
from .forms import ReportForm, CommentForm
from ..models import Reports, Comments  # Community,
from flask_login import login_required, current_user
from .. import db, photos


@main.route('/')
def index():
    """
    This function renders out home page and all its data
    """
    test = "Working"
    reports = Reports.query.all()
    return render_template('index.html', reports=reports, test=test)


@main.route('/report')
def report():
    report_form = ReportForm()

    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        pic_path = path

    if report_form.validate_on_submit():
        location = report_form.location.data
        institution = report_form.institution.data
        department = report_form.department.data
        category = report_form.category.data
        title = report_form.title.data
        description = report_form.description.data
        upvote = report_form.downvote.data
        downvote = report_form.downvote.data
        new_report = Report(location=location,
                            institution=institution,
                            department=department,
                            category=category,
                            title=title,
                            description=description,
                            upvote=upvote,
                            downvote=downvote,
                            pic_path=pic_path)
        db.session.add(new_report)
        db.session.commit()
        return redirect(url_for('main.index'))

    return render_template('report.html', report_form=report_form)


@main.route('/comment<int:id>')
@login_required
def comments(id):
    comment_form = CommentForm()
    report = Report.query.filter_by(id=id)

    if comment_form.validate_on_submit():
        comment = comment_form.comment.data
        new_comment = Comments(comment=comment, user=current_user)
        db.session.commit(new_comment)
        return redirect(url_for('main.index'))

    return render_template('comments.html', report=report,
                           comment_form=comment_form)
