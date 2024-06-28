from django.shortcuts import render
from django.http import HttpResponse
from .models import Question

# 메인페이지
# 모든 설문조사 주제를 보여줌
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date') # 날짜기준 내림차순, 최신순
    context = {'latest_question_list': latest_question_list}

    return render(request, 'polls/index.html', context)


# 설문지별 상세페이지
def detail(request, question_id): 

    return HttpResponse("You're looking at question {}.".format(question_id))

def vote(request, question_id):
    response = "You're looking at vote of question {}."
    return HttpResponse(response.format(question_id))

def results(request, question_id):
    response = "You're looking at the results of question {}."
    return HttpResponse(response.format(question_id))