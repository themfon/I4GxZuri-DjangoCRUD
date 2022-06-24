from django.urls import reverse_lazy
from django.views import generic
from .models import Post

# List view.
class PostListView(generic.ListView):
    model = Post

# Create view.
class PostCreateView(generic.CreateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")

# Detail view.
class PostDetailView(generic.DetailView):
    model = Post

# Update view.
class PostUpdateView(generic.UpdateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")

# Delete view.
class PostDeleteView(generic.DeleteView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")