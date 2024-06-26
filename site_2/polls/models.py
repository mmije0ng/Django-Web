from django.db import models
from django.utils import timezone
import datetime

# 설문조사 주제
class Question(models.Model):
    question_text = models.CharField(max_length=200) # 설문조사 주제 텍스트
    pub_date = models.DateTimeField('date published') # ‘date published’ : 관리자 페이지에서 보여질 항목명

    # Shell이나 관리자 페이지 등에서 DB Table 내의 데이터를 꺼냈을 때 보여지는 텍스트를 지정
    def __str__(self):
        return self.question_text
    
    # 현재 기준으로 하루 전 시점보다 더 이후에 등록된 Question인지 여부를 확인해주는 함수(True/False)
    def was_published_recently(self):
        now = timezone.now()
        
        # datetime.timedelta(days=1) : 하루어치
        # now - datetime.timedelta(days=1) : 현재 날짜에서 하루어치를 뺀 값
        # 주제가 등록된 시점이 함수가 호출되는 시점과 호출되는 시점의 하루이전의 사이에 있는지 여부
        return now >= self.pub_date >= now - datetime.timedelta(days=1)

# 설문조사 선택지
class Choice(models.Model):
    # 자동으로 Question table의 Primary key를 Foreign Key로 세팅
    # on_delete=models.CASCADE : Question(질문) 항목 삭제 시 관계된 선택지들도 모두 자동 삭제
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # 설문조사 주제의 id 값
    choice_text = models.CharField(max_length=200) # 설문조사 주제에 대한 선택지 텍스트
    votes = models.IntegerField(default=0) # 해당 선택지의 득표 수

    def __str__(self):
        return self.choice_text