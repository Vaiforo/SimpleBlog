from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from .forms import AddPostForm, EditPostForm
from .models import Post


class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active'] = 'home'
        return context


class PostView(DetailView, DeleteView):
    model = Post
    template_name = 'blog/post.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active'] = 'post'
        return context


class PostCreateView(CreateView):
    form_class = AddPostForm
    template_name = 'blog/create_post.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active'] = 'create-post'
        return context


class PostEditView(UpdateView):
    model = Post
    form_class = EditPostForm
    template_name = 'blog/edit_post.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active'] = 'home'
        return context
