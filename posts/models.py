from django.db import models


class Article(models.Model):
	title = models.CharField(max_length=255, blank=True)
	content = models.TextField()
	date = models.DateTimeField(auto_now=True)
