from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from blog.models import Comment,Post,Category

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('title','message')
        widgets={'body':CKEditorUploadingWidget}


class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields='__all__'

class UserPostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields='__all__'
        widgets={
            'intro':CKEditorUploadingWidget,
            'body':CKEditorUploadingWidget,
            }
