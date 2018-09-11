from django.urls import path
from .views import *



urlpatterns = [
	path('', post_list, name='post_list_url'),
	path('post/<int:id>/', post_detail, name='post_detail_url'),
	path('post_new/', post_new, name='post_new_url'),
	path('post_edit/<int:id>', post_edit, name='post_edit_url'),
]