from django import forms
from .models import Lead


class LeadForm(forms.Form):
    frist_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    age = forms.IntegerField()


class LeadModelForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = (
            "frist_name",
            "last_name",
            "age",
            "source",
            "profile_image",
            "special_files",
            "agent",
        )
