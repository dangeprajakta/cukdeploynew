from django import forms

class GeeksForm(forms.Form):
	#name = forms.CharField()
	file = forms.FileField()
	start_date= forms.DateField()
	end_date = forms.DateField()
	empno = forms.IntegerField()
