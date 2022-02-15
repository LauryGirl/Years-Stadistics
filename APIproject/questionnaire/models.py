from django.db import models
from user.models import User

Question_Choices = (
    ('text', 'text'),
    ('multiple-choice', 'multiple-choice')
)

class Questionnaire(models.Model):
    name = models.CharField(max_length=128)
    pub_date = models.DateTimeField('date published')

    def get_questions(self):
        return self.question_set.all()

    def __str__(self):
        return f"{self.id} {self.name}"

    class Meta:
        verbose_name = "Questionnaire"
        verbose_name_plural = 'Questionnaires'

class Themes(models.Model):
    name = models.CharField(max_length=128)
    father = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)

    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Theme"
        verbose_name_plural = 'Themes'

class Question(models.Model):
    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE)
    theme = models.ForeignKey(Themes, on_delete=models.CASCADE, blank=True, null=True)
    text = models.TextField(blank=True, verbose_name=("Text"))
    # type = models.CharField(
    #     u'Type of question',
    #     max_length=32,
    #     choices=Question_Choices
    # )
    # sortid = models.IntegerField()

    def get_options(self):
        return self.option_set.all()

    def get_answers(self, user):
        return self.answer_set.get(user=user)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Question"
        verbose_name_plural = 'Questions'
        

class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    value = models.CharField(max_length=120)


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, help_text=u'The question that this is an answer to')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    answer = models.TextField(blank=True, verbose_name=("Answer"))
    
    def __str__(self):
        return f"question: {self.question.text}, answer: {self.answer}"

    