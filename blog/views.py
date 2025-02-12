from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.urls import reverse_lazy

from .models import Post

class BlogDeleteView(DeleteView):
	model = Post
	template_name = 'post_delete.html'
	success_url = reverse_lazy('home')

class BlogUpdateView(UpdateView):
	model = Post
	template_name = 'post_new.html'
	fields = '__all__'

class BlogCreateView(CreateView):
	model = Post
	template_name = 'post_new.html'
	fields = '__all__'

class BlogListView(ListView):
	model = Post
	template_name = 'home.html'


class BlogDetailView(DetailView):
	model = Post
	template_name = 'post_detail.html'


