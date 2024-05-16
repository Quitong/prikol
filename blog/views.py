from django.http import HttpResponse
from django.shortcuts import render

from blog.models import Post, Comment


def main_view(request):
    posts=Post.objects.all()
    for i in posts:
        print(i.title)
    return render(
        request,
        'main_page.html',
        {'pst':posts},

    )

def post_view(request,pk):
    qs = Post.objects.filter(pk=pk)
    post = qs.first()
    comments = Comment.objects.filter(to_post=post)
    comments = comments.all()
    return render(
        request,
        'one_post.html',
        {'post': post,
                'comments' : comments},
    )