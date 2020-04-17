
from django import forms
from app33.models import StudentModel,CourseModel

class StudentForm(forms.ModelForm):
    sid = forms.IntegerField(min_value=101)
    class Meta:
        model = StudentModel
        fields = "__all__"

class CourseForm(forms.ModelForm):
    cid = forms.IntegerField()
    class Meta:
        model = CourseModel
        fields = "__all__"

    def clean_cid(self):
        cno = self.cleaned_data["cid"]
        if cno > 0 and cno <= 100:
            return cno
        else:
            raise forms.ValidationError("Course ID Must be in 1 to 100")