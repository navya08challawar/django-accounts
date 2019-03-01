from django import forms
from . import models


class CreateArticle(forms.ModelForm):
	class Meta:
		model=models.Campus
		fields=['title','slug','body','thumb']

	