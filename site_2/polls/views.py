from django.shortcuts import render, get_object_or_404, redirect # get_object_or_404: 클래스의 행이 없다면 404 에러
from django.http import HttpResponse, Http404
from .models import Question

# 메인페이지
# 모든 설문조사 주제를 보여줌
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date') # 날짜기준 내림차순, 최신순
    context = {'latest_question_list': latest_question_list}

    return render(request, 'polls/index.html', context)


# 설문지별 상세페이지
def detail(request, question_id): 
    # try:
    #     question = Question.objects.get(id=question_id)
    # except Question.DoesNotExist:
    #     # 404 에러를 터뜨리며 에러 문구 함께 리턴
    #     raise Http404('Question {} does not exist'.format(question_id))

    # list(QuerySet)가 return될 시에는 get_object_or_404 대신 get_list_or_404를 활용
    question = get_object_or_404(Question, id=question_id) # 클래스, 기준 값

    return render(request, 'polls/detail.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, id=question_id)

    try:
        selected_choice = question.choice_set.get(pk = request.POST['choice_select'])
        # request.POST['choice_select'] :
        # detail.html의 <input type="radio" name="choice_select" value="{{ choice.id }}">에서 날라온 값
        # form으로 제출된 POST Request 전체에서 'choice_select'가 name인 HTML 태그의 value를 꺼내는 코드
        # request.POST 는 {~~~, 'choice_select':7} 와 같은 dictionary 형태
    except:
        # request.POST['choice_select']값이 없을 경우, error_message를 가지고 details.html로 되돌아감
        context = {'question': question, 'error_message': "You didn't select a choice."}
        return render(request, 'polls/detail.html', context)
    else: 
        selected_choice.votes+=1
        selected_choice.save() # db에 저장
        return redirect('polls:results', question_id=question.id)


def results(request, question_id):
    response = "You're looking at the results of question {}."
    return HttpResponse(response.format(question_id))