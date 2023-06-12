from flask import Blueprint, render_template, request
from flask_login import login_required, current_user

from microblog.models import db, User, Post
from microblog.forms import QuizForm

index_bp = Blueprint('index', __name__)


@index_bp.route('/')
@login_required
def index():

    title = "Benim Süper Sayfam"

    posts = current_user.posts.order_by(Post.timestamp.desc()).limit(5)

    return render_template('index/index.html', title=title, posts=posts)

@index_bp.route('/deneme')
def deneme():
    return "İşte bir deneme"


@index_bp.route('/quiz', methods=['GET', 'POST'])
def quiz():
    questions = [
        {'question': 'Aşağıdakilerden hangisi meyve değildir?', 
         'alternative_a': 'Elma',
         'alternative_b': 'Portakal',
         'alternative_c': 'Domates',
         'alternative_d': 'Marul',
         'answer': 'd',
         'point': 5
        },
        
        {'question': 'Aşağıdakilerden hangisi çiçek açmaz?', 
         'alternative_a': 'Madanoz',
         'alternative_b': 'Kiraz',
         'alternative_c': 'Kavak',
         'alternative_d': 'Kabak',
         'answer': 'a',
         'point': 3
        }
    ]

    form = QuizForm()

    if request.method == 'POST':
        score = 0
        answer_number = 0
        correct_answer_number = 0
        for i, item in enumerate(questions):
            answer_name = 'answer-{}'.format(i)
            if answer_name in request.form:
                answer_number += 1
                if request.form[answer_name] == item['answer']:
                    correct_answer_number += 1
                    score += item['point']

        return render_template('index/quiz_score.html', title="Test Puanı", answer_number=answer_number, correct_answer_number=correct_answer_number, score=score)
            

    return render_template('index/quiz.html', title="Deneme Testi", form=form, questions=questions)



@index_bp.app_template_filter()
def uppercase(text):
    return text[0]+'***'+text[-1]
