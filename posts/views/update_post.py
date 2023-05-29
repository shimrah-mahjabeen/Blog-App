from django.views.generic import UpdateView
from ..models import Post
from django.urls import reverse_lazy

class UpdatePost(UpdateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog_posts")