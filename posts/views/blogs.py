from django.shortcuts import render
from django.views import View
from ..models import Post

class Blogs(View):
    def get(self, request):
        posts = Post.objects.all()
        context = {"blog_entries": posts}
        return render(request, "posts/homepage.html", context=context)

    def post(self, request):
        pass