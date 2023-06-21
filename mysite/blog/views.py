from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from .forms import EmailPostForm


class PostListView(ListView):
    """
    Представление списка постов
    """
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'


# def post_list(request):
#     posts_list = Post.published.all()
#     # Постраничная разбивка с 3 постами на страницу
#     paginator = Paginator(posts_list, 3)
#     page_number = request.GET.get('page', 1)
#     try:
#         posts = paginator.page(page_number)
#     except PageNotAnInteger:
#         posts = paginator.page(1)
#     except EmptyPage:
#         posts = paginator.page(paginator.num_pages)
#     return render(request,
#                   'blog/post/list.html',
#                   context={
#                       'posts': posts,
#                   })


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post,
                             status=Post.Status.PUBLISHED,
                             slug=post,
                             publish__year=year,
                             publish__month=month,
                             publish__day=day
                             )
    return render(request,
                  'blog/post/detail.html',
                  context={
                      'post': post,
                  })


def post_share(request, post_id):
    # Извлечь пост по идентификатору id
    post = get_object_or_404(Post,
    id=post_id,
    status=Post.Status.PUBLISHED)
    if request.method == 'POST':
        # Форма была передана на обработку
        form = EmailPostForm(request.POST)
        if form.is_valid():
        # Поля формы успешно прошли валидацию
            cd = form.cleaned_data
        # ... отправить электронное письмо
    else:
        form = EmailPostForm()
    return render(request,
                  'blog/post/share.html',
                  context={
                      'post': post,
                      'form': form
                  })

