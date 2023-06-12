from flask import Blueprint, render_template, request, flash,\
    redirect, url_for, abort, Markup
from flask_login import login_required, current_user

from microblog.models import db, Message
from microblog.forms import MailForm

mail_bp = Blueprint('mail', __name__)


@mail_bp.route('/<mailbox>')
@login_required
def index(mailbox):
    title = "Postalar"
    show_id = request.args.get('show', type=int)
    messages = current_user.received_messages if mailbox=='inbox' else current_user.sent_messages
    messages = messages.order_by(Message.read.asc(), Message.timestamp.desc())
    show_message = messages.filter_by(id=show_id).first()
    
    if show_message:
        show_message.read = True
        db.session.commit()

    return render_template('mail/index.html', title=title, messages=messages, mailbox=mailbox, show_message=show_message)

@mail_bp.route('/write', methods=['GET', 'POST'])
@login_required
def write():
    reply_id = request.args.get('reply_id', type=int)
    replied_message = current_user.received_messages.filter_by(id=reply_id).first()
    if not replied_message:
        abort(400, Markup('<b>bu ileti<b> size ait değil<i>sen ne yapıyorsun</i>'))

    title = "Postalar"
    form = MailForm()
    

    if request.method == 'POST':
        new_message = Message(
            title=form.title.data,
            body=form.body.data, 
            sender_id=current_user.id,
            )
        if replied_message:
            new_message.receiver_id = replied_message.sender_id
        else:
            new_message.receiver_id=int(form.receiver.data)

        db.session.add(new_message)
        db.session.commit()
        flash("Postanız gönderildi")
        return redirect(url_for('mail.index', mailbox='outbox'))

    elif replied_message:
        form.receiver.data = str(replied_message.sender_id)
        form.receiver.render_kw = {'disabled': 'disabled'}
        
        form.title.data = "Cevap: " + replied_message.title
        form.body.data = "\n{}, {} traihinde yazmıştı:\n> ".format(replied_message.sender.username, replied_message.timestamp.ctime()) + replied_message.body
    
    return render_template('mail/write.html', title=title, form=form)
