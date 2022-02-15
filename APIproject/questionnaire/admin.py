from django.contrib import admin
from .models import Questionnaire, Question, Answer, Option, Themes
# Register your models here.

class OptionInLine(admin.TabularInline):
    model = Option

class QuestionAdmin(admin.ModelAdmin):
    inlines = [OptionInLine]

# class QuestionInline(admin.TabularInline):
#     model = Question

# class AnswerAdmin(admin.ModelAdmin):
#     inlines = [QuestionInline]

admin.site.register(Questionnaire)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
admin.site.register(Themes)
# admin.site.register(Option)