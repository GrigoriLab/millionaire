from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import TemplateView
from models import Question
import random

# Create your views here.

class GamePlay(TemplateView):
    template_name='game/start.html'

    def get_context_data(self, **kwargs):
        context = super(GamePlay, self).get_context_data(**kwargs)

        questions = Question.objects.all()
        if 'used_questions' in self.request.session:
            questions = questions.exclude(id__in = self.request.session['used_questions'])
        else:
            self.request.session['used_questions'] = []

        question = random.choice(questions)
        self.request.session['used_questions'].append(question.id)

        context['question'] = question.question
        context['answers'] = question.choice_options.split(",")
        self.request.session['correct_answers'] = question.correct_answers.split(",")
        self.request.session['current_question_id'] = question.pk
        context['correct_answers'] = question.correct_answers.split(",")
        return context
    def post(self,request):

        answers = request.POST.getlist('checks')
        correct_answers = request.session['correct_answers']



        if not 'questions_count' in request.session:
            request.session['questions_count'] = 0
        elif request.session['questions_count'] > 5:
            request.session['questions_count'] = 0
            score = str(request.session['score'])
            request.session['score'] = 0
            request.session['used_questions'] = []
            return redirect('/game/won/' + score)
        else:
            request.session['questions_count'] += 1

        if all(elem in correct_answers  for elem in answers):
            if not 'score' in request.session:
                request.session['score'] = Question.objects.filter(pk=request.session['current_question_id']).get().score
            else:
                request.session['score'] += Question.objects.filter(pk=request.session['current_question_id']).get().score
            return redirect('/game/start')

        request.session['questions_count'] = 0
        score = request.session['score']
        request.session['score'] = 0
        request.session['used_questions'] = []

        context = {'correct_answers':correct_answers,
                   'score':score,
                   }
        return render(self.request, 'game/end.html', context)


def login_redirect(request):
    return redirect('/account/')

def start(request):
    answer_list = ['first answer','second answer','etc...']
    args = {'question': "test question", 'answers': answer_list}
    return render(request,'game/start.html', args)

def end(request):
    return render(request,'game/end.html')

def won(request, score):
    return render(request,'game/won.html',{'score':score})

