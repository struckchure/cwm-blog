from django.shortcuts import render

from posts.forms import ArticleForm
from posts.models import Article

# Create your views here.

def index(request):
	template_name = 'index.html'
	all_articles = Article.objects.all()

	if request.method == "POST":
		article_form = ArticleForm(request.POST)
		if article_form.is_valid():
			article_form.save()

	article_form = ArticleForm()

	context = {
		'all_articles': all_articles
	}

	return render(request, template_name, context)
