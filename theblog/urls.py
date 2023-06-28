from django.urls import path
# from . import views
from .views import HomeView, ArticleDetailView,AddPostView,UpdatePostVew,DeletePostView, AddCategorytView, CategoryView, CategoryListView, LikeView, AddCommentView
urlpatterns = [
    # path('', views.home, name="home"),
    path('',HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(),name="article-detail"),
    path('add_post/',AddPostView.as_view(), name="add_post"),
    path('article/edit/<int:pk>',UpdatePostVew.as_view(),name="update_post"),
    path('article/<int:pk>/remove',DeletePostView.as_view(),name="delete_post"),
    path('add_category/',AddCategorytView.as_view(), name="add_category"),
    path('category/<str:cats>/', CategoryView,name='category'),
    path('category-list/', CategoryListView,name='category_list'),
    path('like/<int:pk>',LikeView,name='like_post'),
    path('article/<int:pk>/comment',AddCommentView.as_view(),name='add_comment'),
]