from django.http import HttpResponse
from django.shortcuts import render, redirect

from blog.models import Post, Comment, Quiz
from blog.templates.forms import PostForm, CommentForm


def main_view(request):
    posts=Post.objects.all()
    for i in posts:
        print(i.title)

    if request.user.is_authenticated:
        if request.method == 'POST':
            data = request.POST
            print(data)
            form = PostForm(data)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.save()
                post_id = post.id
                return redirect(f"/post/{post_id}/")
        else:
            form = PostForm()
        return render(
            request,
            'main_page.html',
            {'pst': posts,
             'form': form,
             'user': request.user,},

        )
    else:
        return render(
            request,
            'main_page.html',
            {'pst': posts,
                    'user': request.user,})


def post_view(request,pk):
    qs = Post.objects.filter(pk=pk)
    post = qs.first()
    comments = Comment.objects.filter(to_post=post)
    comments = comments.all()
    form = CommentForm()
    if request.user.is_authenticated:
        if request.method == 'POST':
            data = request.POST
            print(data)
            form = CommentForm(data)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.author = request.user
                comment.to_post = post
                comment.save()

    return render(
        request,
        'one_post.html',
        {'post': post,
                'comments' : comments,
                'form':form,
                'user':request.user,
                }
    )

def quiz_list(request,):
    quizes= Quiz.objects.all()
    return render(
        request,
        'quizes_list.html',
        {'quizes': quizes,
         })

def quiz_detal(request,pk):
    quiz = Quiz.objects.filter(id=pk).first()
    quiz.questions = quiz.question_set.all()
    for question in quiz.questions:
        question.answers = question.answer_set.all()

    return render(request,"quiz_detail.html",
                  {
                      'quiz': quiz
                  })