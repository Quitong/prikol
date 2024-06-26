"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from blog.views import main_view, post_view, quiz_list, quiz_detal
from shop.views import cat_goods_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_view),
    path('post/<int:pk>/', post_view),
    path('quiz/', quiz_list),
    path('quiz/<int:pk>/', quiz_detal),
    path ('shop/goods/category_<int:cat_id>/goods_<int:goods_id>/',cat_goods_view)
]
