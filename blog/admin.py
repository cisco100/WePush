from django.contrib import admin
from blog.models import Post,Comment,Category
# Register your models here.

class CommentItemInline(admin.TabularInline):
    model = Comment
    raw_id_fields = ['post']

class PostAdmin(admin.ModelAdmin):
    search_fields = ['title', 'intro', 'author','body','category']
    list_display = ['title', 'author', 'user','category', 'created_at', 'updated','status']
    list_filter = ['category', 'created_at','updated', 'status']
    inlines = [CommentItemInline]
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Post,PostAdmin)



class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title']
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Category,CategoryAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ['title', 'post', 'created_at','user']
    list_filter = ( 'created_at',)
    search_fields = ('name', 'email', 'message',)

admin.site.register(Comment,CommentAdmin)
    


