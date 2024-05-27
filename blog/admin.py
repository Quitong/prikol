from django.contrib import admin

from blog.models import Post, Comment, Quiz, Question, Answer

class QuestionInline(admin.TabularInline):
    model = Question

class QuizAdmin(admin.ModelAdmin):
    inlines = (QuestionInline,)

admin.site.register(Quiz,QuizAdmin)

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Question)
admin.site.register(Answer)
