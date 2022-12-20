from django import forms


SHifts = (
    ("1", "Morning"),
    ("2", "Afternoon"),
    ("3", "Evening"),
)


class DemoForm(forms.Form):
    name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    shifts = forms.ChoiceField(choices=SHifts)
    time_log = forms.TimeField()
