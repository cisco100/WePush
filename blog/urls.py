from django.urls import path,include
from blog import views
urlpatterns = [
    
    #User post...........................
    path("list-category/",views.user_category_list,name="user_category_list"),
    path("category-post/",views.category_post,name="category_post"),
    path("update-category-post/<str:id>/",views.update_category_post,name="update_category_post"),
    path("delete-category-post/<str:id>/",views.delete_category_post,name="delete_category_post"),
    path("list-post/",views.user_post_list,name="user_post_list"),
    path("list-category/",views.user_category_list,name="user_category_list"),
    path("create-post/",views.create_post,name="user_create_post"),
    path("update-post/<str:id>/",views.update_post,name="user_update_post"),
    path("delete-post/<str:id>/",views.delete_post,name="user_delete_post"),
    #Main blog......................
    path('feed/',views.feed_view,name='feed',),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('',views.home_view,name="home"),
    path('search/',views.search, name='search'),
    path('<slug:category_slug>/<slug:slug>/', views.detail, name='post_detail'),
    path('<slug:slug>/',views.category, name='category_detail'),  
    