from msilib.schema import ListView
from operator import index
from pyexpat import model
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import Post, blog

class PostListView(ListView):
    model = Post

class PostCreateView(CreateView):
    model = Post
    fields = [
        "__all__"
    ]
    success_url: reverse_lazy("blog:all")

    template_name:  'index.html'

class PostDetailView("DetailView"):
    model = Post

class PostUpdateView("UpdateView"):
    model = Post
    fields = [
         "__all__"
         ]
    success_url  = reverse_lazy("blog:all")

class postDeleteView("DeleteView"):
    model = Post
    fields= [
        "__all__"
    ]
    success_url = reverse_lazy("blog:all")


