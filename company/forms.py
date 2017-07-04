from django import forms
from .models import RegisterForm


class FormRegister(forms.ModelForm):
	class Meta:
		model=RegisterForm
		fields=('first_name','last_name','address','image')
		