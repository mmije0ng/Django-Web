from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'), # localhost:8000/polls/
    
    # 설문조사 주제 상세 페이지
    # localhost:8000/polls/1/
    path('<int:question_id>/', views.detail, name='detail'), 
    
    # 설문조사 선택지별 투표 post 요청
    # localhost:8000/polls/1/vote
    path('<int:question_id>/vote/', views.vote, name='vote'),

    # 설문조사 선택지별 투표 결과
    # localhost:8000/polls/1/results
    path('<int:question_id>/results/', views.results, name='results'),
]