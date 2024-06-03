from django.http import Http404
from django.shortcuts import render, redirect

from shop.models import Goods


# 'shop/goods/<int:cat_id>/<int:goods_id>/'
def cat_goods_view(request,cat_id,goods_id):

    qs=Goods.objects.filter(pk=goods_id, category__id=cat_id)
    if not qs.exists():
        raise Http404
    good=qs.first()
    return render(request,
    'cat_goods.html',
            dict(
                good=good,
                )
            )


