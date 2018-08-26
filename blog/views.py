from django.shortcuts import get_object_or_404, render
from .models import Article
# Create your views here.
def index(request):
    articles=Article.objects.order_by()
    context = {'article_list': articles}
    return render(request,'blog/index.html',context)
def article(request,article_id):
    pk_article=get_object_or_404(Article,pk=article_id)
    return render(request,'blog/article.html',{'article':pk_article})