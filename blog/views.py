from django.shortcuts import get_object_or_404, render
from .models import Article
# Create your views here.
def index(request):
    articles=Article.objects.order_by('-created_time')
    context = {'article_list': articles}
    return render(request,'blog/index.html',context)
def article_detail(request,article_id):
    article=get_object_or_404(Article,pk=article_id)
    # article.body=markdown.markdown(article.body,
    #                                extensions=[
    #                                    'markdown.extensions.extra',
    #                                    'markdown.extensions.codehilite',
    #                                    'markdown.extensions.toc',
    #                                ])
    return render(request, 'blog/article_detail.html', {'article':article})