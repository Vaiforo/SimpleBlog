from django.urls import path

from .views import PostView, PostListView, PostCreateView, PostEditView

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('post/<int:pk>/', PostView.as_view(), name='post'),
    path('create-post/', PostCreateView.as_view(), name='create-post'),
    path('edit-post/<int:pk>/', PostEditView.as_view(), name='edit-post'),
]
