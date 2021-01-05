from djongo.models.fields import forms
from .models import Instructor, Student


class InstructorCreate(forms.ModelForm):
    class Meta:
        model = Instructor
        fields = '__all__'


class StudentCreate(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'


class StudentLoginForm(forms.Form):
    user = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Student
        fields = ['username', 'password']
