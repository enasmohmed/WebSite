from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from django.forms import ModelForm

from Myapp.models import Team, GameScore


class TeamForm(forms.Form):
    name = forms.CharField(label='اسم الفريق ')
    details = forms.CharField(label='تفاصيل الريق')


class TeamModelForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(TeamModelForm,self).__init__( *args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(Submit('submit','اضافة'))
    class Meta:
        model = Team
        fields = '__all__'
        labels = {
            'name': ' اسم الفريق ',
            'details': 'تفاصيل الفريق'
        }

        error_messages ={
            'name':{
                'unique':'هذا الفريق مكرر, يرجي التاكد من اسم الفريق',
            }
        }

class ScoreModelForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ScoreModelForm,self).__init__( *args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(Submit('submit','اضافة'))
    class Meta:
        model = GameScore
        exclude = ['game_date']

        labels = {
            'first_team_relation': 'الفريق الاول ',
            'second_team_relation': 'الفريق الثاني ',
            'first_team_score': 'نتيجة الفريق الاول',
            'second_team_score': 'نتيجة الفريق الثاني '
        }

