from django.shortcuts import render,get_object_or_404, redirect
from rest_framework import mixins
from rest_framework import generics
from blog.forms import UserPostForm,CategoryForm,CommentForm
from rest_framework.filters import SearchFilter
from blog.models import Post,Comment,Category
from django.db.models import Q
from django.urls import reverse
from django.http import HttpResponse
import feedparser



#Main Blog
def home_view(request):
	posts = Post.objects.filter(status=Post.PUBLISHED)
	return render(request,'blog/main/home.html',{"posts":posts})



def detail(request, category_slug, slug):
    post = get_object_or_404(Post, slug=slug, status=Post.PUBLISHED)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('post_detail', category_slug=category_slug,slug=slug)
    else:
        form = CommentForm()

    return render(request, 'blog/main/detail.html', {'post': post, 'form': form})

def category(request, slug):
    categorys = get_object_or_404(Category, slug=slug)
    posts = categorys.posts.filter(status=Post.PUBLISHED)

    return render(request, 'blog/main/category.html', {'categorys': categorys, 'posts': posts})



def search(request):
    query = request.GET.get('query', '')

    posts = Post.objects.filter(status=Post.PUBLISHED).filter(Q(title__icontains=query) | Q(intro__icontains=query) | Q(body__icontains=query) | Q(author__icontains=query))

    return render(request, 'blog/main/search.html', {'posts': posts, 'query': query})






















# Create your views here.
def user_post_list(request):
	u_post=Post.objects.filter(user=request.user,status=Post.PUBLISHED)
	s_post=Post.objects.filter(user=request.user,status=Post.DRAFT)
	return render(request,'blog/user/user_blog_list.html',{'u_post':u_post,'s_post':s_post})





def user_category_list(request):
	u_cat=Category.objects.filter(user=request.user)
	
	return render(request,'blog/user/user_category_list.html',{'u_cat':u_cat,})

def category_post(request):
	if request.method == 'POST':
		form =CategoryForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('user_create_post')
		
	else:
		form = CategoryForm()
	return render(request,'blog/user/category_user.html',{'form':form})

def update_category_post(request,id):
	category=Category.objects.get(id=id)
	form=CategoryForm(instance=category)
	if request.method=='POST':
		form =CategoryForm(request.POST,instance=category)
		if form.is_valid():
			form.save()
			redirect(reverse("user_post_list"))
	return render(request,'blog/user/category_user.html',{'form':form})


def delete_category_post(request,id):
	category=Category.objects.get(id=id)
	category.delete()
	redirect(reverse("user_category_list"))
	return render(request,'blog/user/delete_category_post.html')


def create_post(request):

	if request.method == 'POST':
		form =UserPostForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
	
	form = UserPostForm()
	return render(request,'blog/user/create_update.html',{'form':form})

def update_post(request,id):
	post=Post.objects.get(id=id)
	form=UserPostForm(instance=post)
	if request.method=='POST':
		form =UserPostForm(request.POST,instance=post)
		if form.is_valid():
			form.save()
	return render(request,'blog/user/create_update.html',{'form':form})



def delete_post(request,id):
	post=Post.objects.get(id=id)
	post.delete()
	redirect(reverse("user_post_list"))
	return render(request,'blog/user/delete_post.html')









#/////////////Micalleneous//////////////////////
def robots_txt(request):
    text = [
        "User-Agent: *",
        "Disallow: /admin/",
    ]
    return HttpResponse("\n".join(text), content_type="text/plain")



def feed_view(request):
    feed=feedparser.parse(reverse('post_feed'))
    entries=feed.entries
    return render(request,'blog/main/feed.html',{'entries':entries})















