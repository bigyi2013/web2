from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import log
from .models import Liuyan
from .models import Comment
from blog.models import Article
from .forms import LiuyanForm
def log_page(request):
    log_list=log.objects.order_by('-created_time')
    context = {'log_lists': log_list}
    return  render(request,'log/log_page.html',context)
def about(request):
    return render(request,'log/about.html')
def liuyan(request):
    # 先获取被评论的文章，因为后面需要把评论和被评论的文章关联起来。
    # 这里我们使用了 Django 提供的一个快捷函数 get_object_or_404，
    # 这个函数的作用是当获取的文章（Post）存在时，则获取；否则返回 404 页面给用户。
    form = LiuyanForm()
    liuyan_list = Liuyan.objects.order_by('-created_time')
    context = {'form': form,
               'liuyan_list': liuyan_list
               }
    # HTTP 请求有 get 和 post 两种，一般用户通过表单提交数据都是通过 post 请求，
    # 因此只有当用户的请求为 post 时才需要处理表单数据。
    if request.method == 'POST':
        # 用户提交的数据存在 request.POST 中，这是一个类字典对象。
        # 我们利用这些数据构造了 CommentForm 的实例，这样 Django 的表单就生成了。
        form = LiuyanForm(request.POST)

        # 当调用 form.is_valid() 方法时，Django 自动帮我们检查表单的数据是否符合格式要求。
        if form.is_valid():
            # 检查到数据是合法的，调用表单的 save 方法保存数据到数据库，
            # commit=False 的作用是仅仅利用表单的数据生成 Comment 模型类的实例，但还不保存评论数据到数据库。
            liuyan = form.save(commit=False)
            # 最终将评论数据保存进数据库，调用模型实例的 save 方法
            liuyan.save()


    return render(request, 'log/liuyan.html', context)

# Create your views here.
