from django import forms
from.models import Post


class PostForm(forms.ModelForm):
	"""Форма добавления новости"""
	
	class Meta:
		model = Post
		fields = ['title', 'text']