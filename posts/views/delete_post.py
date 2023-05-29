from django.views.generic import DeleteView
from ..models import Post
from django.urls import reverse_lazy

class DeletePost(DeleteView):
    model = Post
    success_url = reverse_lazy("blog_posts")