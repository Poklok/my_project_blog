from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def post_list(request):
    posts = Post.objects.all()
    paginator = Paginator(posts.order_by('-id'), 2)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'post_list.html', {'page_obj': page_obj, 'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})


def social_links(request):
    return render(request, 'social_links.html')
