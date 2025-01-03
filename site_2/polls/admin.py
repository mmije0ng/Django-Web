from django.contrib import admin
from .models import Question, Choice

# Question 추가 페이지에서 Choice까지 한번에 추가할 수 있도록
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 2 # Default로 보여줄 Choice 입력 slot의 수

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        # ('field 집합의 소제목', {'fields': ['field 이름 1', 'field 이름 2', ...]}),
        ("Question title", {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]

    inlines = [ChoiceInline]

    list_display = ('question_text', 'pub_date', 'was_published_recently') # 생성한 Question 리스트 페이지에서 question_text 이외의 정보들을 추가로 출력

    list_filter = ['pub_date'] # pub_date(설문조사 생성 시간)을 기준으로 필터 기능 추가
    search_fields = ['question_text'] # question_text(설문조사 주제)를 기준으로 검색 기능 추가

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)