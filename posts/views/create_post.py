from django.views.generic import CreateView
from ..models import Post
from ..forms import CreateForm
from django.urls import reverse_lazy

class CreatePost(CreateView):
    model = Post
    form_class = CreateForm
    template_name = "posts/post_form.html"
    success_url = reverse_lazy("blog_posts")