from django import forms
from posts.models import Article


class ArticleForm(forms.ModelForm):

	class Meta:
		model = Article
		fields = [
			'title',
			'content'
		]
